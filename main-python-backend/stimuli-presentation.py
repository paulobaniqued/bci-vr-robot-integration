import uuid # universally unique identifier
import time
import random
from tkinter import *
from pylsl import StreamInfo, StreamOutlet

trials_per_class = 25

warmup_duration = 15
getready_duration = 2
cue_duration = 4
feedback_duration = 1
rest_duration = 1

pause_every = 25
pause_duration = 15
labels = ['L', 'R']
markers = ['left', 'right']

info = StreamInfo('cue_markers', 'Markers', 1, 0, 'string', 'myuidw43536')
outlet = StreamOutlet(info)

print("Press [Enter] to begin.")
x = input()

# Tkinter GUI
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

outlet.push_sample(['1']) # start
print('START')
blinkLabel.config(image=BlankImage)
root.update()
time.sleep(warmup_duration)

try:
    for trial in range(1, trials_per_class*len(labels)+1):
        
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
        
        # tkinter rest update
        outlet.push_sample(['5']) #Marker '5' for rest
        print("REST") 
        blinkLabel.config(image=BlankImage)
        root.update()

        time.sleep(rest_duration) # rest duration
        
        if trial % pause_every == 0:
            print("HALFWAY PAUSE")
            time.sleep(pause_duration)
        
except Exception as e:
    print(e)
outlet.push_sample(['6']) # end