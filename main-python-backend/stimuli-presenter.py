"""BCI Stimuli Presenter for NeuroPype"""
import uuid # universally unique identifier
import time
import random
from tkinter import *
from pylsl import StreamInfo, StreamOutlet

# Set parameters
labels = ['L', 'R']
markers = ['left', 'right']
trials_per_class = 25
warmup_duration = 15
getready_duration = 2
cue_duration = 4
feedback_duration = 1
rest_duration = [1, 2, 3]
pause_every = 25
pause_duration = 15

# Set labstreaminglayer: outbound
info = StreamInfo('cue_markers', 'Markers', 1, 0, 'string')
outlet = StreamOutlet(info)

# Set Tkinter GUI
root = Tk()
root.title('Graz Motor Imagery')
root.resizable(width=False, height=False)
root.geometry('1080x1080')
root.configure(bg='black')
BlankImage = PhotoImage(file='1_Blank.png')
BaselineImage = PhotoImage(file='2_Baseline.png')
CueLeftImage = PhotoImage(file='3_CueLeft.png')
CueRightImage = PhotoImage(file='4_CueRight.png')
blinkLabel = Label(root, fg='black', text=None, width=1080, height=720)
blinkLabel.pack(side=TOP, expand=1)
blinkLabel.config(image=BlankImage)

# Start session
print("Press [Enter] to begin.")
x = input()

outlet.push_sample(['1']) # start
print("START")
blinkLabel.config(image=BlankImage)
root.update()
time.sleep(warmup_duration)
trial_counter = 0

try:
    for trial in range(1, trials_per_class*len(labels)+2):
        
        trial_counter += 1
        print("Trial: ", trial_counter)
        outlet.push_sample(['2']) # get ready
        print("GET READY")
        blinkLabel.config(image=BaselineImage)
        root.update()
        time.sleep(getready_duration)

        choice = random.choice(range(len(labels))) # select random cue

        # tkinter cue update
        if markers[choice] == 'left':
            outlet.push_sample(['3']) #Marker '3' for left
            print("LEFT")
            blinkLabel.config(image=CueLeftImage)
            root.update()

        if markers[choice] == 'right':
            outlet.push_sample(['4']) #Marker '4' for left
            print("RIGHT")
            blinkLabel.config(image=CueRightImage)
            root.update()

        time.sleep(cue_duration) # cue duration 

        # tkinter feedback and rest update
        blinkLabel.config(image=BlankImage)
        root.update()

        print("FEEDBACK")
        time.sleep(feedback_duration) # feedback processing and presentation
        
        outlet.push_sample(['5']) #Marker '5' for rest
        rest_choice = random.choice(rest_duration) # rest can either be 1, 2 or 3 seconds
        print("REST for ", rest_choice, "s")
        time.sleep(rest_choice) # rest duration
        
        if trial % pause_every == 0:
            print("PAUSE for ", pause_duration, " seconds")
            time.sleep(pause_duration)
        
except Exception as e:
    print(e)

outlet.push_sample(['6']) # end
print("END")