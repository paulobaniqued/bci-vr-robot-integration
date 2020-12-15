using UnityEngine;
using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using Assets.LSL4Unity.Scripts.AbstractInlets;

namespace Assets.LSL4Unity.Scripts.Examples
{
    /// <summary>
    /// Just an example implementation for a Inlet recieving float values
    /// </summary>
    public class ExampleFloatInlet : AFloatInlet
    {
        public Animator LeftAnimator;
        public Animator RightAnimator;

        GameObject LeftArrow;
        GameObject RightArrow;
        GameObject FixationCross;

        float trialTime = 4.0f;
        float getreadyTime = 1.5f;

        public string lastSample = String.Empty;

        void Awake()
        {
            LeftArrow = GameObject.Find("LeftArrow");
            RightArrow = GameObject.Find("RightArrow");
            FixationCross = GameObject.Find("FixationCross");
        }

        protected override void Process(float[] newSample, double timeStamp)
        {
            // just as an example, make a string out of all channel values of this sample
            lastSample = string.Join(" ", newSample.Select(c => c.ToString()).ToArray());

            //Debug.Log(newSample[0]);
            float cue = newSample[0];

            Debug.Log(cue);
            
            if (cue == 2.0)
            {
                Debug.Log("FIXATION CROSS");
                FixationCross.SetActive(true);
                StartCoroutine(ResetCross());
            }
            
            if (cue == 3.0)
            {
                Debug.Log("TRIGGER LEFT");
                LeftAnimator.SetTrigger("Grasp");
                LeftArrow.SetActive(true);
                StartCoroutine(ResetHands());
            }
            else if(cue == 4.0)
            {
                Debug.Log("TRIGGER RIGHT");
                RightAnimator.SetTrigger("Grasp");
                RightArrow.SetActive(true);
                StartCoroutine(ResetHands());
            }

            IEnumerator ResetCross()
            {
                yield return new WaitForSeconds(getreadyTime);
                FixationCross.SetActive(false);
            }

            IEnumerator ResetHands()
            {
                yield return new WaitForSeconds(trialTime);
                LeftAnimator.ResetTrigger("Grasp");
                RightAnimator.ResetTrigger("Grasp");
                LeftArrow.SetActive(false);
                RightArrow.SetActive(false);
            }   


        }
    }
}