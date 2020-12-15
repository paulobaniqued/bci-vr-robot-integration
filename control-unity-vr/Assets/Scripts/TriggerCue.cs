using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TriggerCue : MonoBehaviour
{
    public Animator LeftAnimator;
    public Animator RightAnimator;

    GameObject LeftArrow;
    GameObject RightArrow;
    GameObject FixationCross;

    float trialTime = 4;

    void Awake()
    {
        LeftArrow = GameObject.Find("LeftArrow");
        RightArrow = GameObject.Find("RightArrow");
        FixationCross = GameObject.Find("FixationCross");
        StartCoroutine(ResetHands());
    }

    // Update is called once per frame
    void Update()
    {

        if (Input.GetKeyDown(KeyCode.Keypad4))
        {
            Debug.Log("debug left key down");
            LeftArrow.SetActive(true);
            LeftAnimator.SetTrigger("Grasp");
            StartCoroutine(ResetHands());

        }
        if (Input.GetKeyDown(KeyCode.Keypad6))
        {
            Debug.Log("debug right key down");
            RightArrow.SetActive(true);
            RightAnimator.SetTrigger("Grasp");
            StartCoroutine(ResetHands());
        }
        if (Input.GetKeyDown(KeyCode.Keypad5))
        {
            Debug.Log("debug fixation cross");
            FixationCross.SetActive(true);
            StartCoroutine(ResetHands());
        }
        
    }
    IEnumerator ResetHands()
    {
        yield return new WaitForSeconds(trialTime);
        LeftAnimator.ResetTrigger("Grasp");
        RightAnimator.ResetTrigger("Grasp");
        LeftArrow.SetActive(false);
        RightArrow.SetActive(false);
        FixationCross.SetActive(false);
    }
}
