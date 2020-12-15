using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using LSL;

public class TriggerFeedback : MonoBehaviour
{
    public ParticleSystem SparkleLeft;
    public ParticleSystem SparkleRight;
    public string StreamType = "feedback";
    liblsl.StreamInfo[] streamInfos;
    liblsl.StreamInlet streamInlet;
    float[] sample;
    private int channelCount = 0;

    GameObject LeftBar;
    GameObject RightBar;

    void Awake()
    {
        LeftBar = GameObject.Find("LeftBar");
        RightBar = GameObject.Find("RightBar");

        LeftBar.SetActive(false);
        RightBar.SetActive(false);
    }

    void Update()
    {
        // Manual Feedback Trigger
        if (Input.GetKeyDown(KeyCode.Keypad3)) // Correct Feedback Right
        {
            Debug.Log("trigger up key down");
            SparkleRight.Simulate(0.0f, true, true);
            SparkleRight.Play();
            RightBar.SetActive(true);
            StartCoroutine(ManuallyResetBars());
        }
        if (Input.GetKeyDown(KeyCode.Keypad1)) // Correct Feedback Left
        {
            Debug.Log("trigger down key down");
            SparkleLeft.Simulate(0.0f, true, true);
            SparkleLeft.Play();
            LeftBar.SetActive(true);
            StartCoroutine(ManuallyResetBars());
        }

        IEnumerator ManuallyResetBars()
        {
            yield return new WaitForSeconds(1.0f);
            LeftBar.SetActive(false);
            RightBar.SetActive(false);
        }

        // LSL Feedback Trigger
        if (streamInlet == null)
        {
            streamInfos = liblsl.resolve_stream("type", StreamType, 1, 0.0);
            if (streamInfos.Length > 0)
            {
                streamInlet = new liblsl.StreamInlet(streamInfos[0]);
                channelCount = streamInlet.info().channel_count();
                streamInlet.open_stream();
            }
        }

        if (streamInlet != null)
        {
            sample = new float[channelCount];
            double lastTimeStamp = streamInlet.pull_sample(sample, 0.0f);

            float lastFeedback = sample[0];

            if (lastFeedback == 300.0) // Correct Feedback Right
            {
                Debug.Log("CORRECT RIGHT FEEDBACK");
                SparkleRight.Simulate(0.0f, true, true);
                SparkleRight.Play();
                RightBar.SetActive(true);
                StartCoroutine(ResetBars());
            }
            if (lastFeedback == 200.0) // Correct Feedback Left
            {
                Debug.Log("CORRECT LEFT FEEDBACK");
                SparkleLeft.Simulate(0.0f, true, true);
                SparkleLeft.Play();
                LeftBar.SetActive(true);
                StartCoroutine(ResetBars());
            }
            if (lastFeedback == 30.0) // Incorrect Feedback Right
            {
                Debug.Log("INCORRECT RIGHT FEEDBACK");
                RightBar.SetActive(true);
                StartCoroutine(ResetBars());
            }
            if (lastFeedback == 20.0) // Incorrect Feedback Left
            {
                Debug.Log("INCORRECT LEFT FEEDBACK");
                LeftBar.SetActive(true);
                StartCoroutine(ResetBars());
            }
            if (lastFeedback == 100.0) // No Prediction
            {
                Debug.Log("NO PREDICTION");
            }

            IEnumerator ResetBars()
            {
                yield return new WaitForSeconds(1.0f);
                LeftBar.SetActive(false);
                RightBar.SetActive(false);
            }



        }
    }
}