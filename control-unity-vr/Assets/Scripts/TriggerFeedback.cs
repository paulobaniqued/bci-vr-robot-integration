using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerFeedback : MonoBehaviour
{
    public ParticleSystem SparkleLeft;
    public ParticleSystem SparkleRight;

    // Update is called once per frame
    void Update()
    {
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
        
    }
}
