using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.IO;
using System.Text;
using UnityEditor;
using UnityEngine;
using UnityEngine.UI;

/// <summary>
/// Put this component on the <see cref="Button"/>.
/// <para>Stores all log messages during runtime by registering a listener for <see cref="Application.logMessageReceivedThreaded"/>.</para>
/// <para>Adds a callback to <see cref="Button.onClick"/> and saves the logged messages including the timestamp to a file.</para>
/// see https://docs.unity3d.com/ScriptReference/Application-logMessageReceivedThreaded.html
/// </summary>
[RequireComponent(typeof(Button))]
public class LogExportButton : MonoBehaviour
{
    #region Inspector
#pragma warning disable 0649 // Disable never assigned warnings
    /// <summary>
    /// Reference to the <see cref="Button"/> component
    /// </summary>
    [Tooltip("The button component, if possible already reference this via the Inspector in Unity")]
    [SerializeField] private Button _button;

    /// <summary>
    /// The filename where to store the log file.
    /// </summary>
    [Tooltip("The filename where to store the log file.\n"
             + "In the Unity Editor the file will be placed in the folder Assets/StreamingAssets\n"
             + "In a built app it will be written to the persistentDataPath")]
    [SerializeField] private string _fileName = "DebugLogExport.txt";
#pragma warning restore 0649
    #endregion

    /// <summary>
    /// Path to the folder where to store the file.
    /// <para>In the Unity Editor returns <see cref="Application.streamingAssetsPath"/></para>
    /// <para>In a built app returns <see cref="Application.persistentDataPath"/></para>
    /// </summary>
    /// <remarks>
    /// <para>See</para>
    /// <list type="bullet">
    /// <item>https://docs.unity3d.com/ScriptReference/Application-isEditor.html</item>
    /// <item>https://docs.unity3d.com/ScriptReference/Application-persistentDataPath.html</item>
    /// <item>https://docs.unity3d.com/ScriptReference/Application-streamingAssetsPath.html</item>
    /// </list>
    /// </remarks>
    private string _folderName => Application.isEditor ? Application.streamingAssetsPath : Application.persistentDataPath;

    /// <summary>
    /// The final absolute system file path
    /// </summary>
    private string _filePath => Path.Combine(_folderName, _fileName);

    /// <summary>
    /// Thread-safe queue for storing received log messages
    /// </summary>
    private readonly ConcurrentQueue<string> _newestThreadSafeMessages = new ConcurrentQueue<string>();

    /// <summary>
    /// In case you export multiple times on runtime this stores the messages from the last export
    /// </summary>
    private readonly List<string> _allMessages = new List<string>();

    private void Awake()
    {
        // as fallback get the reference on runtime
        if (!_button) _button = GetComponent<Button>();

        // add the callback for the button
        _button.onClick.AddListener(ExportLogFile);

        // Adds a callback to call a method every time a log is added to the Unity console
        Application.logMessageReceivedThreaded += OnLogMessageReceived;
    }

    ///<summary>
    ///TODO: Just for testing generating some debug logs
    /// <para>TODO: Remove this!</para>
    /// </summary>
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.L))
        {
            Debug.Log("The L key was pressed!", this);
        }

        if (Input.GetKeyDown(KeyCode.E))
        {
            Debug.LogError("The E key was pressed!", this);
        }

        if (Input.GetKeyDown(KeyCode.X))
        {
            Debug.LogException(new NotImplementedException("But the X key was pressed!"), this);
        }

        if (Input.GetKeyDown(KeyCode.W))
        {
            Debug.LogWarning("The W key was pressed!", this);
        }
    }

    /// <summary>
    /// Called when the <see cref="_button"/> is pressed
    /// <para>Writes received messages to the file</para>
    /// </summary>
    private void ExportLogFile()
    {
        if (Application.isEditor && !Directory.Exists(_folderName))
        {
            Directory.CreateDirectory(_folderName);
        }

        Debug.Log($"Exporting Log File to {_filePath}");

        if (File.Exists(_filePath))
        {
            File.Delete(_filePath);
        }

        using (var file = File.Open(_filePath, FileMode.OpenOrCreate, FileAccess.Write))
        {
            using (var writer = new StreamWriter(file))
            {
                // In case of mutiple exports first add the possibly threaded messages from the queue to the list
                // This automatically removes them from the queue that's why ;)
                while (_newestThreadSafeMessages.TryDequeue(out var message))
                {
                    _allMessages.Add(message);
                }
                var builder = new StringBuilder();
                // then go through all messages and build our final file content
                foreach (var message in _allMessages)
                {
                    builder.Append(message).Append('\n');
                }

                // finally write this to the file
                // Do it async so it doesn't block the app too much
                writer.WriteAsync(builder.ToString());
            }
        }

#if UNITY_EDITOR
        // Only in the Unity Editor refresh so the new added folder and file(s) appear
        AssetDatabase.Refresh();
#endif
    }

    /// <summary>
    /// Called for every message logged in the Unity console
    /// <para>NOTE: Might be called in a different Thread so this method has to be thread-safe!</para>
    /// </summary>
    /// <param name="logString"></param>
    /// <param name="stackTrace"></param>
    /// <param name="type"></param>
    private void OnLogMessageReceived(string logString, string stackTrace, LogType type)
    {
        // Here of course it depends totally on you what you need out of the logs.
        // I will now only go with the timestamp, the type and the message
        // If you need it you could as well include the stackTrace

        // Also the timestamp depends on you of course
        // You could go with time since app started or like me go with the actual time
        var time = DateTime.Now;
        // e.g. 04:02:01.023
        var timeStamp = $"{time.Hour:D2}:{time.Minute:D2}:{time.Second:D2}.{time.Millisecond:D3}";

        // I used a format like e.g.
        //
        // ## 01:02:03.045 Log
        // Message here below
        //
        // in order to easily find messages also if the log itself contains line-breaks
        var fullMessage = $"## {timeStamp} {type}\n{logString}\n\n";

        // add the new message to the queue
        _newestThreadSafeMessages.Enqueue(fullMessage);
    }
}