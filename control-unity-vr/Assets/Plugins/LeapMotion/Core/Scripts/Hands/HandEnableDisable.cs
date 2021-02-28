/******************************************************************************
 * Copyright (C) Ultraleap, Inc. 2011-2020.                                   *
 *                                                                            *
 * Use subject to the terms of the Apache License 2.0 available at            *
 * http://www.apache.org/licenses/LICENSE-2.0, or another agreement           *
 * between Ultraleap and you, your company or other organization.             *
 ******************************************************************************/

using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System;
using System.Text;
using System.IO;
using Leap;
using UnityEngine.UI;

namespace Leap.Unity{
  public class HandEnableDisable : HandTransitionBehavior {

    public List<string> htresults = new List<string>{};

    public System.DateTime startTime;
    
    protected override void Awake() {
      base.Awake();
      gameObject.SetActive(false);
    }

  	protected override void HandReset() {
      gameObject.SetActive(true);
      startTime = System.DateTime.UtcNow;
    }

    protected override void HandFinish() {
      gameObject.SetActive(false);
      System.TimeSpan ts = System.DateTime.UtcNow - startTime;
      Debug.Log(ts.Seconds.ToString());
      htresults.Add(ts.Seconds.ToString());

    }

  }
}
