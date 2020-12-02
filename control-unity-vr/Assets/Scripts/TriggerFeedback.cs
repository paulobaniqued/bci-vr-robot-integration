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

    void Update()
    {
        // Manual Feedback Trigger
        if (Input.GetKeyDown("up")) // Correct Feedback Right
        {
            Debug.Log("trigger up key down");
            SparkleRight.Simulate(0.0f, true, true);
            SparkleRight.Play();

        }
        if (Input.GetKeyDown("down")) // Correct Feedback Left
        {
            Debug.Log("trigger down key down");
            SparkleLeft.Simulate(0.0f, true, true);
            SparkleLeft.Play();

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
            Debug.Log(sample[0]);

        }
    }
}