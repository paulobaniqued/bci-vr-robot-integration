"""Motor Imagery Stimuli Presentation
by Michal Pelikan and Paul Baniqued
Working as of 13-12-2019"""

#/////////////////////////////////////////////////////////////////////////PREPARED WORKSHEET
import xlsxwriter
import os, sys
import time
import random 
import numpy as np
from pylsl import StreamInlet, resolve_stream, StreamInfo, StreamOutlet

# LSL Outlet for Markers
info = StreamInfo('MyMarkerStream', 'Markers', 1, 100, 'string', 'myuidw43536')
outlet = StreamOutlet(info)

# Save as CSV
TestWorkbook = xlsxwriter.Workbook('./EEGspreadsheet/test_data.xlsx') #Creates an excel file called "test_data"
SamplesWorksheet = TestWorkbook.add_worksheet( 'data' ) #Creates a spreadsheet within "test_data" called "data"




""" SESSION SETTINGS """
startup_duration = 5
baseline_duration = 4.5
cue_duration = 5.5
rest_duration = 2.5
sampling_duration = baseline_duration + cue_duration

# 5R & 5L trials
trial_list = ["R","R","R","R","R","L","L","L","L","L"]
random.shuffle(trial_list)
print("Trial list: ", trial_list)
trial_order = trial_list
trial_order.reverse()
labels = np.array([])
for label in trial_order:
    if label == "L":
        labels = np.append(labels, 0)
    elif label == "R":
        labels = np.append(labels, 1)
labels = np.int64(labels)
print("Trial order: ", trial_order)
print("Labels: ", labels)
np.save("training_labels.npy", labels)
no_trials = len(trial_list)
print("Number of trials: ", no_trials)
time.sleep(1)



""" FUNCTIONS """

def first_trials(startup_duration):
    print("Playing...") 
    outlet.push_sample(['1']) #Marker1
    time.sleep(startup_duration)
    #os.system('cls')

def succ_trials(trial_number, baseline_duration, cue_duration):
    outlet.push_sample(['2']) #Marker2
    print("Get ready.")
    print("trial ", trial_number)
    time.sleep(baseline_duration)
    #os.system('cls')
    
    SamplesWorksheet.write(("A" + str(trial_number)), trial_number)

    cue_feeder = trial_list.pop()

    if cue_feeder == "L":
        
        outlet.push_sample(['3']) #Marker3
        print("L")
        #os.system('cls')
        SamplesWorksheet.write(("B" + str(trial_number)), "C3") #update workbook with value from the EEGprocessor for C3
        SamplesWorksheet.write(("C" + str(trial_number)), "C4") #update workbook with value from the EEGprocessor for C4
        SamplesWorksheet.write(("D" + str(trial_number)), "L") #update workbook with 'L' classification 
        time.sleep(cue_duration)

    elif cue_feeder == "R":
        
        outlet.push_sample(['4']) #Marker4
        print("R")
        #os.system('cls')
        SamplesWorksheet.write(("B" + str(trial_number)), "C3") #update workbook with value from the EEGprocessor for C3
        SamplesWorksheet.write(("C" + str(trial_number)), "C4") #update workbook with value from the EEGprocessor for C4
        SamplesWorksheet.write(("D" + str(trial_number)), "R") #update workbook with 'R' classification
        time.sleep(cue_duration)

def rest(rest_duration):
    print("Rest")
    outlet.push_sample(['5']) #Marker5
    time.sleep(rest_duration)

def end_session():
    print("End of trials") 
    outlet.push_sample(['6']) #Marker6
    TestWorkbook.close() #close workbook so that the training data file saves
    sys.exit()




""" ACTUAL SEQUENCE """

session = input("Start session? Y/N: ")

if session == 'Y':

    # Resolve a Stimulator Stream
    print("looking for a Stimulator stream...")
    streams = resolve_stream('type', 'Stimulator')
    inlet = StreamInlet(streams[0]) #stimulator
    time.sleep(1)
    print("found Stimulator stream")

    while True:
        
        stim_status = inlet.pull_sample()[0][0]

        if stim_status == "100":
            print(stim_status, "Creating empty channels... setting data structure")
        
        elif stim_status == "200":
            print(stim_status, "Connecting to LSL...")

        elif stim_status == "300":
            print("Connected. Starting session...")
            outlet.push_sample(['0']) #Marker1

            # Initialise trial number and index counter
            trial_number = 1
            index_counter = 0

            while True:
                # Starting session
                first_trials(startup_duration) # Startup idle time, send marker 1

                for trial in range(no_trials): 
                    succ_trials(trial_number, baseline_duration, cue_duration)
                    # Get ready and cue, send markers 2, 3, 4
                    trial_number = trial_number + 1
                    rest(rest_duration) # Rest, send marker 5

                if trial_number == 11:
                    end_session() # End of session, save data, send marker 6

elif session == 'N':
    print("not ready...")