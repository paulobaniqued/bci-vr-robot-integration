using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerCue : MonoBehaviour
{
    public Animator LeftAnimator;
    public Animator RightAnimator;

    float trialTime = 4;

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown("left"))
        {
            Debug.Log("trigger left key down");
            LeftAnimator.SetTrigger("Grasp");
            StartCoroutine(ResetHands());

        }
        if (Input.GetKeyDown("right"))
        {
            Debug.Log("trigger right key down");
            RightAnimator.SetTrigger("Grasp");
            StartCoroutine(ResetHands());
        }
        
    }
    IEnumerator ResetHands()
    {
        yield return new WaitForSeconds(trialTime);
        LeftAnimator.ResetTrigger("Grasp");
        RightAnimator.ResetTrigger("Grasp");
    }
}
