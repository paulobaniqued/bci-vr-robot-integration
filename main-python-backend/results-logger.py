"""Test prediction stream output from NeuroPype."""

from time import sleep
from threading import *
import concurrent.futures
from pylsl import StreamInlet, resolve_stream

print("looking for a Truth stream...")
truths = resolve_stream('name', 'Truth')
truths_inlet = StreamInlet(truths[0])
print("Found Truths!")

print("looking for a Prediction stream...")
predictions = resolve_stream('type', 'Prediction')
pred_inlet = StreamInlet(predictions[0])
print("Found Predictions!")

def truths_stream(truths_inlet):

    while True:
        truth_value = truths_inlet.pull_sample()
        truth_value = truth_value[0][0]
        #print("Truth is ", truth_value)
        return truth_value
    
def predictions_stream(pred_inlet):

    while True:

        sample = pred_inlet.pull_sample()
        left_prediction = sample[0][0]
        right_prediction = sample[0][1]
        #print("Left ", left_prediction)
        #print("Right ", right_prediction)
        return left_prediction, right_prediction

while True:

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_truths = executor.submit(truths_stream, truths_inlet)
        future_predictions = executor.submit(predictions_stream, pred_inlet)
    
        truth = future_truths.result()
        left, right = future_predictions.result()
        print("The truth is... ", truth, " / The predictions are... left=", left, " right=", right)

    sleep(1)
