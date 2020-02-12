"""Background EEG Acquisition Handler and ERD/ERS processor for Hand AOMI2 Experiment (virtual reality)
(SL) Surface Laplacian enabled
author: Paul Baniqued (https://github.com/paulbaniqued)

################################# TRAINING SESSION #################################

Saves as 3D array (no_timesteps x no_channels x no_trials)
Working as of 06-02-2020"""

from pylsl import StreamInlet, resolve_stream, StreamInfo, StreamOutlet
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt, sosfreqz, filtfilt
import numpy as np
import mne
import sys
import time

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
print("Experiment: Action Observation and Motor Imagery in Virtual Reality (TRAINING)")
pid = input("Please enter participant ID: ")

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

            elif now_ready == 3: # LEFT trial
                labels = np.append(labels, int(0))
                print("left trial recorded", "trial: ", trial_count+1)

            elif now_ready == 4: # RIGHT trial
                labels = np.append(labels, int(1))
                print("right trial recorded", "trial: ", trial_count+1)

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
                print("data compiled to tensor")

                # Reset
                C3, C4, FC5, FC6, C1, C2, CP5, CP6 = empty_channels()
                print("C3 bin empty?: ", C3, C3.shape)
                trial_count = trial_count + 1

            elif now_ready == 6:
                print("end of trials...")
                print("training data: ", ds_eeg)
                print(np.shape(ds_eeg))
                print("labels: ", labels)
                print(np.shape(labels))
                print(type(labels))

                # Save as CSV
                np.save(f"{pid}_training_data_vr.npy", ds_eeg)
                np.save(f"{pid}_training_labels_vr.npy", labels)

                print("Training session saved to C:\mnpdeb")
                
                sys.exit()
    
    except KeyboardInterrupt:
        print("Closing program...")
    
    finally:
        sys.exit()

