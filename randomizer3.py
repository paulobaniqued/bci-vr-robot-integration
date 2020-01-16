import os
import time
import random
from tkinter import *
from pylsl import StreamInfo, StreamOutlet


info = StreamInfo('MyMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')
outlet = StreamOutlet(info)

#20R & 20L trials
trial_list = ["R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L"]

# Initialise GUI
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

#Key for initiating the display function
play = "play"


#the cue feeder randomizes the list and feeds one item from the list
def cue_feeder():
    if int(len(trial_list)) > 0:
        random.shuffle(trial_list)
        cue = trial_list.pop()
        return cue


#once the display is initiated there will be a 20s preparation time
#the display will play the previously agreed sequence until all of the items from the cue list are displayed
def display(key):
  
    outlet.push_sample(['1']) #Marker1
    print("Playing...") 
    blinkLabel.config(image=BlankImage)
    root.update()
    time.sleep(5)
    os.system('cls')
    
    while key == "play" and len(trial_list) > 0:
       
        outlet.push_sample(['2']) #Marker2
        print("Get ready.")
        blinkLabel.config(image=BaselineImage)
        root.update()
        time.sleep(3.5)
        os.system('cls')

        if cue_feeder() == "L":
            outlet.push_sample(['3']) #Marker3
            print("L")
            blinkLabel.config(image=CueLeftImage)
            root.update()
            time.sleep(6)
            os.system('cls')

        elif cue_feeder() == "R":
            outlet.push_sample(['4']) #Marker4
            print("R")
            blinkLabel.config(image=CueRightImage)
            root.update()
            time.sleep(6)
            os.system('cls')

        outlet.push_sample(['5']) #Marker5
        print("Rest") 
        blinkLabel.config(image=BlankImage)
        root.update()
        time.sleep(2.5)
        os.system('cls')
    
    outlet.push_sample(['6']) #Marker6
    print("End of trials") 

display("play")













       

