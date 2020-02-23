"""
Online prediction of hand motor imagery classes using virtual reality
author: Paul Baniqued (https://github.com/paulbaniqued)
shallowNN author: Max Townsend

################################# ONLINE SESSION #################################

Saves as 3D array (no_timesteps x no_channels x no_trials)
Working as of 06-02-2020"""

import logging
import importlib
importlib.reload(logging) # see https://stackoverflow.com/a/21475297/1469195
log = logging.getLogger()
log.setLevel('INFO')
import sys
import mne
from mne.io import concatenate_raws
import csv

logging.basicConfig(format='%(asctime)s %(levelname)s : %(message)s',
                     level=logging.INFO, stream=sys.stdout)

############################## Data formatting ################################
# EEG data should be formatted nDarray: nTrials * mChannels * tTimesteps
# labels should be formatted array: nTrials 
import numpy as np

# Enter participant ID
print("Experiment: Action Observation and Motor Imagery in Virtual Reality (ONLINE)")
pid = input("Please enter participant ID (e.g. nn000pp): ")
day = input("Please input the day of the session: (e.g. 5): ")

# Load training data
training_data = np.load(f"{day}_{pid}_training_data_vr.npy")
training_data = np.float32(training_data)
print(training_data)
print(np.shape(training_data))
print(training_data.dtype)

# Load labels
labels = np.load(f"{day}_{pid}_training_labels_vr.npy")
#labels = np.genfromtxt('labels_t.csv', delimiter=',')
labels = np.int64(labels)
print(labels)
print(np.shape(labels))
print(labels.dtype)

# Convert data from volt to millivolt
# Pytorch expects float32 for input and int64 for labels.
X = training_data
y = labels
# X.shape = nTrials * mChannels * tTimesteps
# y.shape = nTrials
# X.shape[1] and X.shape[2] are used to shape the spatial and temporal
# input layers of the network, respectively
print("array: ", X)
print("shape of data: ", np.shape(X))
print("labels: ", y)
print("shape of labels: ", np.shape(y))

############# Seperate training, testing, and validations sets ################
# SignalAndTarget returns a data structure which contains both the eeg data and 
# the labels.
from braindecode.datautil.signal_target import SignalAndTarget
train_set = SignalAndTarget(X[:40], y=y[:40])
print("train set: ", train_set)
valid_set = SignalAndTarget(X[20:40], y=y[20:40])
print("valid set: ", valid_set)

#################### Importing and setting up models ##########################

from torch import nn
from braindecode.torch_ext.util import set_random_seeds
from braindecode.torch_ext.optimizers import AdamW
import torch.nn.functional as F
# Set cuda = True if you want to use GPU
# You can also use torch.cuda.is_available() to determine if cuda is available on your machine.
cuda = False
set_random_seeds(seed=20170629, cuda=cuda)
n_classes = 2
in_chans = train_set.X.shape[1]
# final_conv_length = auto ensures we only get a single output in the time dimension
def getModel(size):
    if size == 1:
        from braindecode.models.deep4 import Deep4Net
        model = Deep4Net(in_chans=in_chans, n_classes=n_classes,
                        input_time_length=train_set.X.shape[2],
                        final_conv_length='auto')
        optimizer = AdamW(model.parameters(), lr=1*0.01, weight_decay=0.5*0.001) # these are good values for the deep model
    elif size == 0:
        from braindecode.models.shallow_fbcsp import ShallowFBCSPNet
        model = ShallowFBCSPNet(in_chans=in_chans, n_classes=n_classes,
                        input_time_length=train_set.X.shape[2],
                        final_conv_length='auto')
        optimizer = AdamW(model.parameters(), lr=0.0625 * 0.01, weight_decay=0) # values for shallow model

    else:
        sys.exit('Error in input to model() ----- please enter 0 for shallow, or 1 for deep')
    if cuda:
        model.cuda()   
    #Compile network into graph (like tensorflow)     
    model.compile(loss=F.nll_loss, optimizer=optimizer, iterator_seed=1,)
    return model

############################## Choose Model ###################################

# 0 = shallow net; 1 = deep net 
# shallow should work better when using small data sets, absent pretraining.
net = 0 
model = getModel(net)   

########################### training and validation ###########################

model.fit(train_set.X, train_set.y, epochs=20, batch_size=64, scheduler='cosine',
         validation_data=(valid_set.X, valid_set.y),)

########################### plotting the result ###############################

# get numpy ndarray from the dataframe
results = model.epochs_df.values
validLoss = [i[1] for i in results]
validError = [i[3] for i in results]
trainLoss = [i[0] for i in results]
trainError = [i[2] for i in results]

# plot validation loss & error

import matplotlib.pyplot as plt

ax=plt.subplot(1,2,1)
ax.set_title('Training & Validation Error by Epoch')
ax.set_ylabel('Error (%)')
ax.set_xlabel('Epoch')
plt.plot(validError, label="validError")
plt.plot(trainError, label="trainError")
plt.legend(loc="upper right")

ax=plt.subplot(1,2,2)
ax.set_title('Training & Validation Loss by Epoch')
ax.set_ylabel('Loss')
ax.set_xlabel('Epoch')
plt.plot(validLoss, label="validLoss")
plt.plot(trainLoss, label="trainLoss")
plt.legend(loc="upper right")

fig = plt.gcf()
fig.set_size_inches(10.5, 3.5)
plt.savefig(f"{pid}_NN training results") # to save .png
#plt.show()

################################## Testing ####################################
Xo = X[0:1]
print(np.shape(Xo))
yo = y[0:1]
print(np.shape(yo))

test_set = SignalAndTarget(X=Xo, y=yo)
print("test set: ", test_set)

output = model.evaluate(test_set.X,test_set.y)
loss = output['loss']
error = output['misclass']
acc = 1 - error
print("Test loss: ", loss)
print("Test error: ", error)
print("Test accuracy: ", acc)
predictedLabels = model.predict_classes(test_set.X)
print(predictedLabels)
actualLabels = test_set.y
#to see predicted and actual labels
print("predicted labels vs actual", [predictedLabels,actualLabels])


"""Background EEG Acquisition Handler and ERD/ERS processor for Hand AOMI2 Experiment (virtual reality)
(SL) Surface Laplacian
Saves as 3D array (no_timesteps x no_channels x no_trials)
Working as of 06-02-2020"""

from pylsl import StreamInlet, resolve_stream, StreamInfo, StreamOutlet
#import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt, sosfreqz, filtfilt
#import numpy as np
#import mne
#import sys
import time

# LSL Outlet for Feedback
info = StreamInfo('MyFeedbackStream', 'Feedback', 1, 10, 'float32', 'myuidw5050')
StreamInfo()
outlet = StreamOutlet(info)

""" SETTINGS """


import json
settings = json.load(open('aomi_settings.json'))

startup_duration = settings["startup_duration"]
baseline_duration = settings["baseline_duration"]
cue_duration = settings["cue_duration"]
rest_duration = settings["rest_duration"]
sampling_duration = baseline_duration + cue_duration

# Sample rate and desired cutoff frequencies (in Hz).
sampling_frequency = settings["sampling_frequency"]
fs = sampling_frequency

no_trials = settings["num_training_trials"]
no_channels = settings["num_channels"] # change to 2 if surface_laplacian() == true
padding_samples = settings["padding_samples"] # 250 = 0.5 seconds
actual_baseline = baseline_duration - int(padding_samples/fs)
no_rawtimesteps_i = int(sampling_frequency*sampling_duration + padding_samples) # 5250 (-250 after filter)
no_rawtimesteps = int(sampling_frequency*sampling_duration)
streaming_duration = int(sampling_duration + rest_duration)
no_streamingtimesteps = int(sampling_frequency*streaming_duration)
no_newtimesteps = settings["num_newtimesteps"]


""" FUNCTIONS """

# Create Array for Channels

def empty_channels():

    C3 = np.array([])
    C4 = np.array([])
    FC5 = np.array([])
    FC6 = np.array([])
    C1 = np.array([])
    C2 = np.array([])
    CP5 = np.array([])
    CP6 = np.array([])
    return C3, C4, FC5, FC6, C1, C2, CP5, CP6

# Set Dimensions for Data

def data_structure(no_trials, no_channels, no_newtimesteps):
    ds_eeg = np.ndarray(shape=(no_trials, no_channels, no_newtimesteps), dtype=float)
    return ds_eeg

# Surface Laplacian

def surface_laplacian(ch1, ch2, ch3, ch4):
    oc_x = 4*ch1 - 1*ch2 - 1*ch3 - 1*ch4
    return oc_x 

# Bandpass Filter

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band', analog = False)
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    #nyq = 0.5 * fs
    #low = lowcut / nyq
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

def zero_order_butterworth(data, order, fs, lowcut, highcut):
    x = np.empty(data.shape)
    x = butter_bandpass_filter(data, lowcut, highcut, fs, order=4)
    return x

# Spectral Bandpower

def spectral_bandpower(data):
    # Should add log(1 + x)?
    return np.square(data)

# Moving Average

def moving_average(data, sampling_frequency, no_rawtimesteps, no_newtimesteps):
    ave_duration = 1*sampling_frequency
    ave_interval = 0.1*sampling_frequency
    
    ave_point = round(ave_duration*0.5)
       
    eeg_ave = np.ndarray([no_channels,no_newtimesteps])
    ave_counter = 0
    
    for i in range(no_newtimesteps):
        ave_start = round(ave_point - ave_duration*(0.5))
        ave_end = round(ave_point + ave_duration*(0.5))
        epoch = data[:, ave_start:ave_end]
        get_ave = np.ndarray.tolist(epoch.mean(axis=1))
        eeg_ave[:,ave_counter] = get_ave
        ave_point = round(ave_point + ave_interval)
        ave_counter = ave_counter + 1

    print("eeg average")
    print(eeg_ave)
    return eeg_ave

# Baseline Correction

def basecorr(data, actual_baseline, no_channels, no_newtimesteps):
    baseline = data[:,0:int(actual_baseline*10)]
    baseline_ave = baseline.mean(axis=1)
    channel_base = 0
    eeg_basecorr = np.ndarray(shape=(no_channels, no_newtimesteps), dtype=float)
    print(baseline_ave)

    for channel in range(no_channels):
        eeg_basecorr[channel_base,:] = data[channel_base,:] - baseline_ave[channel_base]
        channel_base = channel_base + 1
    
    return eeg_basecorr, baseline_ave

# ERD/ERS Relative Power

def erds(data, baseline_ave, no_channels, no_newtimesteps):
    channel_base = 0
    eeg_erds = np.ndarray(shape=(no_channels, no_newtimesteps), dtype=float)

    for channel in range(no_channels):
        eeg_erds[channel_base,:] = (data[channel_base,:]/baseline_ave[channel_base])*100
        channel_base = channel_base + 1

    return eeg_erds


""" MAIN PROCESS PIPELINE """
print("starting main process pipeline...")
time.sleep(1)

print("creating data channels...")
C3, C4, FC5, FC6, C1, C2, CP5, CP6 = empty_channels()
trial_count = 0
ds_eeg = data_structure(no_trials, no_channels, no_newtimesteps)
labels = np.array([])
time.sleep(1)

while True:

    try:

        # Resolve an EEG stream on the lab network
        print("looking for EEG and marker streams...")
        streams = resolve_stream('type', 'EEG')
        streams2 = resolve_stream('type', 'Markers')
            
        # Create a new inlet to read from the stream
        inlet = StreamInlet(streams[0]) #EEG
        get_ready = StreamInlet(streams2[0]) #marker
        print("Found EEG stream...")

        while True:

            now_ready = get_ready.pull_sample()[0][0]
            now_ready = int(now_ready)
            print(now_ready)
            print(type(now_ready))

            if now_ready == 1:
                print("Found markers stream... NOW READY!!!")

            elif now_ready == 2:
                print("sampling EEG... ")
                for i in range(no_streamingtimesteps-1): # 1750 N (3.5s) baseline, 3250 N (6.5s) trial, 1250 N (2.5s) rest for a total of 6250
                    sample, timestamp = inlet.pull_sample()
                    C3 = np.append(C3, sample[0])
                    C4 = np.append(C4, sample[1])
                    FC5 = np.append(FC5, sample[2])
                    FC6 = np.append(FC6, sample[3])
                    C1 = np.append(C1, sample[4])
                    C2 = np.append(C2, sample[5])
                    CP5 = np.append(CP5, sample[6])
                    CP6 = np.append(CP6, sample[7])
                    eeg_raw = np.array([C3, C4, FC5, FC6, C1, C2, CP5, CP6])

                print("sampling ended...")

            elif now_ready == 3:
                print("Cue Left")
                yo = np.int64([0])
                labels = np.append(labels, int(0))
                actual_hand = "Actual Hand: LEFT"

            elif now_ready == 4:
                print("Cue Right")
                yo = np.int64([1])
                labels = np.append(labels, int(1))
                actual_hand = "Actual Hand: RIGHT"
            
            elif now_ready == 5:
                
                # Get padded samples for baseline and cue only, remove padding after filter
                eeg_rawtrials = eeg_raw[:,0:no_rawtimesteps_i]
                print(np.shape(eeg_rawtrials))

                # # Plotting Raw
                # fig = plt.figure(trial_count+1)
                # ax1 = fig.add_subplot(231)
                # ax2 = fig.add_subplot(232)
                # ax3 = fig.add_subplot(233)
                # ax4 = fig.add_subplot(212)

                # x_point1 = np.arange(no_rawtimesteps_i)
                # ax1.plot(x_point1, eeg_rawtrials[0,:])
                # ax1.plot(x_point1, eeg_rawtrials[1,:])
                # ax1.plot(x_point1, eeg_rawtrials[2,:])
                # ax1.plot(x_point1, eeg_rawtrials[3,:])
                # ax1.plot(x_point1, eeg_rawtrials[4,:])
                # ax1.plot(x_point1, eeg_rawtrials[5,:])
                # ax1.plot(x_point1, eeg_rawtrials[6,:])
                # ax1.plot(x_point1, eeg_rawtrials[7,:])

                # Surface Laplacian

                C3_oc = surface_laplacian(C3, FC5, C1, CP5)
                C4_oc = surface_laplacian(C4, FC6, C2, CP6)
                oc = np.array([C3_oc, C4_oc])
                print(oc)
                print(oc.shape)

                # Bandpass Filter to Mu (500Hz, 8-12Hz)
                lowcut = 8.5
                highcut = 11.5

                eeg_filtered = zero_order_butterworth(oc, 4, fs, lowcut, highcut)
                print(eeg_filtered)
                print(np.shape(eeg_filtered))


                # Plotting Filtered (USE TO COMPARE PADDING) ------------------- 
                #f, ax = plt.subplots()
                #x_point = np.arange(no_rawtimesteps_i)
                #ax.plot(x_point, eeg_filtered[0,:])
                #ax.plot(x_point, eeg_filtered[1,:])
                #ax.plot(x_point, eeg_filtered[2,:])
                #ax.plot(x_point, eeg_filtered[3,:])
                #ax.plot(x_point, eeg_filtered[4,:])
                #ax.plot(x_point, eeg_filtered[5,:])
                #ax.plot(x_point, eeg_filtered[6,:])
                #ax.plot(x_point, eeg_filtered[7,:])
                #plt.show()

                eeg_filtered = eeg_filtered[:,padding_samples:no_rawtimesteps_i]
                print(eeg_filtered)
                print(np.shape(eeg_filtered))

                # # Plotting Filtered
                # x_point2 = np.arange(no_rawtimesteps)
                # ax2.plot(x_point2, eeg_filtered[0,:])
                # ax2.plot(x_point2, eeg_filtered[1,:]) 
                
                # if SL not enabled
                # ax2.plot(x_point2, eeg_filtered[2,:])
                # ax2.plot(x_point2, eeg_filtered[3,:])
                # ax2.plot(x_point2, eeg_filtered[4,:])
                # ax2.plot(x_point2, eeg_filtered[5,:])
                # ax2.plot(x_point2, eeg_filtered[6,:])
                # ax2.plot(x_point2, eeg_filtered[7,:])

                # Get Mu Power
                eeg_powered = spectral_bandpower(eeg_filtered)
                print("Mu power: ")
                print(eeg_powered)

                # # Plotting Powered
                # x_point3 = np.arange(no_rawtimesteps)
                # ax3.plot(x_point3, eeg_powered[0,:])
                # ax3.plot(x_point3, eeg_powered[1,:])

                # if SL not enabled
                # ax3.plot(x_point3, eeg_powered[2,:])
                # ax3.plot(x_point3, eeg_powered[3,:])
                # ax3.plot(x_point3, eeg_powered[4,:])
                # ax3.plot(x_point3, eeg_powered[5,:])
                # ax3.plot(x_point3, eeg_powered[6,:])
                # ax3.plot(x_point3, eeg_powered[7,:])

                # Averaging Over Time
                eeg_ave = moving_average(eeg_powered, sampling_frequency, no_rawtimesteps, no_newtimesteps)
                print("Averaging over time: ")
                print(eeg_ave)

                # Baseline Correction
                eeg_basecorr, baseline_ave = basecorr(eeg_ave, actual_baseline, no_channels, no_newtimesteps)
                print("EEG Baseline-corrected: ")
                print(eeg_basecorr)

                # ERD / ERS percent change
                eeg_erds = erds(eeg_basecorr, baseline_ave, no_channels, no_newtimesteps)
                print("ERD / ERS Percent Change: ")
                print(eeg_erds)
                print(np.shape(eeg_erds))

                # # Plotting
                # x_point4 = np.arange(no_newtimesteps)
                # ax4.plot(x_point4, eeg_erds[0,:])
                # ax4.plot(x_point4, eeg_erds[1,:])

                # if SL not enabled
                # ax4.plot(x_point4, eeg_erds[2,:])
                # ax4.plot(x_point4, eeg_erds[3,:])
                # ax4.plot(x_point4, eeg_erds[4,:])
                # ax4.plot(x_point4, eeg_erds[5,:])
                # ax4.plot(x_point4, eeg_erds[6,:])
                # ax4.plot(x_point4, eeg_erds[7,:])

                # Show Plots
                #plt.show()

                # Compile Data
                ds_eeg[trial_count,:,:] = eeg_erds[:,:]

                feedback = data_structure(1, no_channels, no_newtimesteps)
                feedback[0,:,:] = eeg_erds[:,:]

                Xo = feedback
                print(np.shape(Xo))
                print(np.shape(yo))

                test_set = SignalAndTarget(X=Xo, y=yo)
                print("test set: ", test_set)

                output = model.evaluate(test_set.X,test_set.y)
                loss = output['loss']
                error = output['misclass']
                acc = 1 - error
                print("Test loss: ", loss)
                print("Test error: ", error)
                print("Test accuracy: ", acc)
                predictedLabels = model.predict_classes(test_set.X)
                print(predictedLabels)
                actualLabels = test_set.y
                #to see predicted and actual labels
                print("predicted labels vs actual", [predictedLabels,actualLabels])

                if predictedLabels[0] == 0:
                    predicted_hand = "Predicted Hand: LEFT"
                    outlet.push_sample([0.0])
                elif predictedLabels[0] == 1:
                    predicted_hand = "Predicted Hand: RIGHT"
                    outlet.push_sample([1.0])

                print(predicted_hand, ", ", actual_hand)

                # Reset
                C3, C4, FC5, FC6, C1, C2, CP5, CP6 = empty_channels()
                print("C3 bin empty?: ", C3, C3.shape)

                trial_count = trial_count + 1

            elif now_ready == 6:
                print("end of trials...")
                print(ds_eeg)
                print(np.shape(ds_eeg))

                # Save as CSV
                np.save(f"{day}_{pid}_online_data_vr.npy", ds_eeg)
                np.save(f"{day}_{pid}_online_labels_vr.npy", labels)

                print("Online session saved to C:\mnpdeb")
                
                sys.exit()
    
    except KeyboardInterrupt:
        print("Closing program...")
    
    finally:
        sys.exit()