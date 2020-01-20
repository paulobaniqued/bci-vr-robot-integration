"""Motor Imagery Stimuli Presentation
by Michal Pelikan and Paul Baniqued
Working as of 13-12-2019"""

#/////////////////////////////////////////////////////////////////////////PREPARED WORKSHEET
import xlsxwriter
import os, sys
import time
import random 
import numpy as np
from tkinter import *
from pylsl import StreamInlet, resolve_stream, StreamInfo, StreamOutlet


# LSL Outlet for Markers
info = StreamInfo('MyMarkerStream', 'Markers', 1, 100, 'string', 'myuidw43536')
outlet = StreamOutlet(info)

# Save as CSV
TestWorkbook = xlsxwriter.Workbook('./EEGspreadsheet/test_data.xlsx') #Creates an excel file called "test_data"
SamplesWorksheet = TestWorkbook.add_worksheet( 'data' ) #Creates a spreadsheet within "test_data" called "data"

# GUI (Obtained from Peter Valber https://www.youtube.com/watch?v=ivcF1acxMF8)
# Needs 4 image files on the same folder
buttonFont = ('Helvetica', 12, 'bold', 'roman')

root = Tk()
root.title('Graz Motor Imagery')
root.resizable(width=True, height=True)
root.geometry('1080x1080')
root.configure(bg='black')

BlankImage = PhotoImage(file='1_Blank.png')
BaselineImage = PhotoImage(file='2_Baseline.png')
CueLeftImage = PhotoImage(file='3_CueLeft.png')
CueRightImage = PhotoImage(file='4_CueRight.png')

GUI_Counter = Label(root, fg="white", bg="darkblue", font=buttonFont)
GUI_Counter.pack(side=TOP, expand=YES)

#GUI_Button = Button(root, text='Exit', bg='deepskyblue', width=6, height=2, activebackground='gray', font=buttonFont, command=root.destroy)
#GUI_Button.pack(side=TOP, expand=YES)

GUI_Label = Label(root, fg='black', text=None, width=1080, height=720)
GUI_Label.pack(side=TOP, expand=YES)
GUI_Label.config(image=BlankImage)


""" SESSION SETTINGS """
startup_duration = 10
baseline_duration = 3.5
cue_duration = 6.5
rest_duration = 2.5
sampling_duration = baseline_duration + cue_duration

# 5R & 5L trials
trial_list = ["R","R","R","R","R","L","L","L","L","L","R","R","R","R","R","L","L","L","L","L","R","R","R","R","R","L","L","L","L","L","R","R","R","R","R","L","L","L","L","L","R","R","R","R","R","L","L","L","L","L","R","R","R","R","R","L","L","L","L","L","R","R","R","R","R","L","L","L","L","L","R","R","R","R","R","L","L","L","L","L"]
random.shuffle(trial_list)
#print("Trial list: ", trial_list)
trial_order = np.flip(trial_list)
labels = np.array([])
for label in trial_order:
    if label == "L":
        labels = np.append(labels, 0)
    elif label == "R":
        labels = np.append(labels, 1)
labels = np.int64(labels)
np.flip(labels)
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
    GUI_Label.config(image=BlankImage)
    root.update()
    time.sleep(startup_duration)
    #os.system('cls')

def succ_trials(trial_number, baseline_duration, cue_duration):
    outlet.push_sample(['2']) #Marker2
    print("Get ready.")
    print("trial ", trial_number)
    GUI_Label.config(image=BaselineImage)
    GUI_Counter.config(text="Trial: " + str(trial_number) + " of " + str(no_trials))
    root.update()
    time.sleep(baseline_duration)
    #os.system('cls')
    
    SamplesWorksheet.write(("A" + str(trial_number)), trial_number)

    cue_feeder = trial_list.pop()

    if cue_feeder == "L":
        
        outlet.push_sample(['3']) #Marker3
        print("L")
        GUI_Label.config(image=CueLeftImage)
        root.update()
        #os.system('cls')
        SamplesWorksheet.write(("B" + str(trial_number)), "C3") #update workbook with value from the EEGprocessor for C3
        SamplesWorksheet.write(("C" + str(trial_number)), "C4") #update workbook with value from the EEGprocessor for C4
        SamplesWorksheet.write(("D" + str(trial_number)), "L") #update workbook with 'L' classification 
        time.sleep(cue_duration)

    elif cue_feeder == "R":
        
        outlet.push_sample(['4']) #Marker4
        print("R")
        GUI_Label.config(image=CueRightImage)
        root.update()
        #os.system('cls')
        SamplesWorksheet.write(("B" + str(trial_number)), "C3") #update workbook with value from the EEGprocessor for C3
        SamplesWorksheet.write(("C" + str(trial_number)), "C4") #update workbook with value from the EEGprocessor for C4
        SamplesWorksheet.write(("D" + str(trial_number)), "R") #update workbook with 'R' classification
        time.sleep(cue_duration)

def rest(rest_duration):
    print("Rest")
    outlet.push_sample(['5']) #Marker5
    GUI_Label.config(image=BlankImage)
    root.update()
    time.sleep(rest_duration)

def end_session():
    print("End of trials") 
    outlet.push_sample(['6']) #Marker6
    TestWorkbook.close() #close workbook so that the training data file saves
    sys.exit()




""" ACTUAL SEQUENCE """

while True:

    try:

        #session = input("Start session? y/n: ")
        session = 'y'

        if session == 'y':

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

                        if trial_number == no_trials + 1:
                            end_session() # End of session, save data, send marker 6

        elif session == 'n':
            print("not ready...")

        root.mainloop()
    
    except KeyboardInterrupt:
        print("Closing program...")
        time.sleep(1.5)

    finally:
        sys.exit()