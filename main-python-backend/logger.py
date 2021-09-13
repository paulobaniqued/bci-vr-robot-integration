### LOGGER.py MODULE ### 
### by: Paul Dominick E. Baniqued
### Website: paulobaniqued.github.io
"""Test prediction stream output from NeuroPype."""
import numpy as np
import pandas as pd
import time
from threading import *
import concurrent.futures
from pylsl import StreamInlet, resolve_stream, StreamInfo, StreamOutlet
import json
import os
from playsound import playsound

with open('E:/bci/session/ids.json','r') as fp:
    session_key = json.load(fp)

day = input("\n\n What session is it today? ")
session_id = session_key.get(day) + ".csv"
data_path = 'E:\\bci\\data\\'

column_names = ['trial','truth','prediction','prob_left','prob_right','score']
session_log = pd.DataFrame(columns=column_names)
trial_counter = 1
score = 0
left_counter = 0
right_counter = 0

print("looking for a Truth stream...")
truths = resolve_stream('name', 'Truth')
truths_inlet = StreamInlet(truths[0])
print("Found Truths!")

print("looking for a Prediction stream...")
predictions = resolve_stream('type', 'Prediction')
pred_inlet = StreamInlet(predictions[0])
print("Found Predictions!")

# Set labstreaminglayer: outbound
info = StreamInfo('feedback', 'feedback', 1, 0) # float32 default 
outlet = StreamOutlet(info)

def truths_stream(truths_inlet):

    while True:
        truth_value = truths_inlet.pull_sample()
        truth_value = truth_value[0][0]
        return truth_value
    
def predictions_stream(pred_inlet):

    while True:

        sample = pred_inlet.pull_sample()
        left_prediction = sample[0][0]
        right_prediction = sample[0][1]
        return left_prediction, right_prediction

def print_trial_counts():
    print("Left Trials: ", left_counter)
    print("Right Trials: ", right_counter)
    print("Total: ", trial_counter)

while True:

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_truths = executor.submit(truths_stream, truths_inlet)
        future_predictions = executor.submit(predictions_stream, pred_inlet)

        print("Trial ", trial_counter)
    
        truth = future_truths.result()
        if truth == 'left':
            left_counter += 1
        elif truth == 'right':
            right_counter += 1

        left, right = future_predictions.result()

        thresh = 0.6

        if left > right and left >= thresh:
            prediction = 'left'
            pred_prob = left
        elif left < right and right >= thresh:
            prediction = 'right'
            pred_prob = right
        else:
            prediction = 'none'
            pred_prob = [left, right]

        if truth == prediction:
            if truth == 'left':
                outlet.push_sample([200]) # correct left
            elif truth == 'right':
                outlet.push_sample([300]) # correct right
            playsound('E:\\bci\\assets\\correct.wav', False)
            score += 1
        elif truth != prediction:
            if prediction == 'left':
                outlet.push_sample([20]) # incorrect left predicted
                playsound('E:\\bci\\assets\\error.wav', False)
            elif prediction == 'right':
                outlet.push_sample([30]) # incorrect right predicted
                playsound('E:\\bci\\assets\\error.wav', False)
            elif prediction == 'none':
                outlet.push_sample([100]) # indecisive
                playsound('E:\\bci\\assets\\error.wav', False)


        results = pd.DataFrame([[trial_counter, truth, prediction, left, right, score]], columns=column_names)
        print("Results obtained")
        #print(results) # Don't display scores

        session_log = session_log.append(results, ignore_index=True)
        print("Session logged")
        #print(session_log) # Don't display scores

        session_log.to_csv(os.path.join(data_path,session_id), index=False)

        trial_counter += 1

        if trial_counter == 61:
            playsound('E:\\bci\\assets\\complete.wav', False)
            print("60 trials reached")
            print_trial_counts()
            time.sleep(2)
            exit()


        
