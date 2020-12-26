#%%
"""BCI Stimuli Presenter for NeuroPype (VR-only condition, Serial disabled)"""
import time
import random
from tkinter import *
from pylsl import StreamInfo, StreamOutlet
import itertools
from playsound import playsound

# Set parameters
labels = ['left', 'right']
trials_per_class = 10 # per block (T=20)
blocks = 3
warmup_duration = 15
getready_duration = 2
cue_duration = 4
feedback_duration = 1
rest_duration = [1, 2, 3]
pause_duration = 15

trial_list = list(itertools.chain.from_iterable(itertools.repeat(x, trials_per_class) for x in labels))
random.shuffle(trial_list)

# Set labstreaminglayer: outbound
info = StreamInfo('cue_markers', 'Markers', 1, 0, 'string')
outlet = StreamOutlet(info)

# Set Tkinter GUI
root = Tk()
root.title('Graz Motor Imagery')
root.resizable(width=False, height=False)
root.geometry('1080x1080')
root.configure(bg='black')
BlankImage = PhotoImage(file='E:\\bci\\assets\\1_Blank.png')
BaselineImage = PhotoImage(file='E:\\bci\\assets\\2_Baseline.png')
CueLeftImage = PhotoImage(file='E:\\bci\\assets\\3_CueLeft.png')
CueRightImage = PhotoImage(file='E:\\bci\\assets\\4_CueRight.png')
blinkLabel = Label(root, fg='black', text=None, width=1080, height=720)
blinkLabel.pack(side=TOP, expand=1)
blinkLabel.config(image=BlankImage)

outlet.push_sample(['1']) # start
print("START")
blinkLabel.config(image=BlankImage)
root.update()
time.sleep(warmup_duration)
trial_counter = 0
block_counter = 1
left_counter = 0
right_counter = 0

while block_counter <= blocks:

    random.shuffle(trial_list)

    for trial in range(0, len(trial_list)):
        
        trial_counter += 1
        print("Trial: ", trial_counter)
        outlet.push_sample(['2']) # get ready
        #print("GET READY")
        playsound("E:\\bci\\assets\\ready.wav", False)
        blinkLabel.config(image=BaselineImage)
        root.update()
        time.sleep(getready_duration)

        choice = trial_list[trial] # select from shuffled trial list

        # tkinter cue update
        if choice == 'left':
            outlet.push_sample(['3']) #Marker '3' for left
            print("LEFT")
            playsound("E:\\bci\\assets\\cue.wav", False)
            blinkLabel.config(image=CueLeftImage)
            root.update()
            left_counter += 1

        if choice == 'right':
            outlet.push_sample(['4']) #Marker '4' for left
            print("RIGHT")
            playsound("E:\\bci\\assets\\cue.wav", False)
            blinkLabel.config(image=CueRightImage)
            root.update()
            right_counter += 1

        time.sleep(cue_duration) # cue duration 

        # tkinter feedback and rest update
        blinkLabel.config(image=BlankImage)
        root.update()

        #print("FEEDBACK")
        time.sleep(feedback_duration) # feedback processing and presentation
        
        outlet.push_sample(['5']) #Marker '5' for rest
        rest_choice = random.choice(rest_duration) # rest can either be 1, 2 or 3 seconds
        #print("REST for ", rest_choice, "s")
        time.sleep(rest_choice) # rest duration
        
        if (trial_counter == block_counter*trials_per_class*2) :
            if (trial_counter == blocks*trials_per_class*2):
                print("Blocks completed")
                playsound('E:\\bci\\assets\\complete.wav', False)
                outlet.push_sample(['6']) # end
                print("END")
                print("Left Trials: ", left_counter)
                print("Right Trials: ", right_counter)
                print("Total: ", trial_counter)
            else:
                print("Block ended, PAUSE for ", pause_duration, " seconds")
                time.sleep(pause_duration)
                block_counter += 1
            
time.sleep(60)