using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerCue : MonoBehaviour
{
    public Animator HandLeft;
    public Animator HandRight;

    float trialTime = 4;

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown("left"))
        {
            Debug.Log("trigger left key down");
            HandLeft.SetTrigger("Grasp");
            StartCoroutine(ResetHands());

        }
        if (Input.GetKeyDown("right"))
        {
            Debug.Log("trigger right key down");
            HandRight.SetTrigger("Grasp");
            StartCoroutine(ResetHands());
        }
        
    }
    IEnumerator ResetHands()
    {
        yield return new WaitForSeconds(trialTime);
        HandLeft.SetTrigger("Idle");
        HandRight.SetTrigger("Idle");
    }
}
