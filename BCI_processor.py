"""Background EEG Processor 
From Raw Data to 2-channel Mu Power
Saves as 3D array (no_timesteps x no_channels x no_trials)
Working as of 22-11-2019"""

from pylsl import StreamInlet, resolve_stream
from scipy.signal import butter, lfilter
import numpy as np
import mne
import matplotlib.pyplot as plt
import time

#create trial list for channels
C3 = np.zeros([])
C4 = np.zeros([])
FC5 = np.zeros([])
FC6 = np.zeros([])
C1 = np.zeros([])
C2 = np.zeros([])
CP5 = np.zeros([])
CP6 = np.zeros([])

#create overall data structure session array (N trials)
sampling_freq = 500 
no_timesteps = 5000 # 10 seconds of data
new_timesteps = 100 # reduced to averaged data (10 seconds of data)
baseline_duration = 35 # samples from new sampling frequency
no_channels = 2
no_trials = 20
trial_count = 0 # init
ds_eeg = np.ndarray(shape=(no_trials, no_channels, new_timesteps), dtype=float)




""" FUNCTIONS """

# Surface Laplacian

def surface_laplacian(ch1, ch2, ch3, ch4):
    oc_x = 4*ch1 - 1*ch2 - 1*ch3 - 1*ch4
    return oc_x 

# Bandpass Filter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    eeg_filtered = lfilter(b, a, data)
    return eeg_filtered

# Spectral Bandpower

def spectral_bandpower(data):
    eeg_powered = np.square(data)
    # Should add log(1 + x)?
    return eeg_powered

# Moving Average

def moving_average(data, sampling_freq):
    ave_duration = 1*sampling_freq
    ave_interval = 0.1*sampling_freq
    new_timesteps = round(no_timesteps/ave_interval)
    
    ave_point = round(ave_duration*0.5)
       
    eeg_ave = np.ndarray([no_channels,new_timesteps])
    ave_counter = 0
    
    for i in range(new_timesteps):
        ave_start = round(ave_point - ave_duration*(0.5))
        ave_end = round(ave_point + ave_duration*(0.5))
        epoch = data[:, ave_start:ave_end]
        get_ave = np.ndarray.tolist(epoch.mean(axis=1))
        eeg_ave[:,ave_counter] = get_ave
        ave_point = round(ave_point + ave_interval)
        ave_counter = ave_counter + 1

    print("eeg average")
    print(eeg_ave)
    return eeg_ave, new_timesteps

# Baseline Correction (NOT COMPLETE!)

def baseline_correction(data, bs_duration):
    baseline = data[:,0:bs_duration]
    ave_baseline = baseline.mean(axis=1)
    print(ave_baseline) # [data data]
    eeg_basecorr = np.zeros([])
    eeg_basecorr[0].append([i - ave_baseline[0] for i in data[0,:]])
    eeg_basecorr[1] = [i - ave_baseline[1] for i in data[1,:]]
    return eeg_basecorr


""" MAIN PROCESS PIPELINE """

while True:
    # Resolve an EEG stream on the lab network
    # print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
    streams2 = resolve_stream('type', 'Markers')
        
    # Create a new inlet to read from the stream
    inlet = StreamInlet(streams[0]) #EEG
    get_ready = StreamInlet(streams2[0]) #marker

    while True:

        now_ready = get_ready.pull_sample()
        now_ready2 = now_ready[0]
        now_ready3 = now_ready2[0]

        if now_ready3 == 2:
            print("working...  EEG ")
            time.sleep(10)
            print("ended...")
            


    #get_readycue = input("Start sampling? Y/N: ") # Replace with LSL Receive String Marker for Get Ready
    """
    if now_ready3 == 2:

        # Data Acquisition from LSL stream
        while True:
            for i in range(no_timesteps-1): # 1750 samples (3.5s) baseline, 3500 samples (6.5s) trial, total of 5000 (change no_timesteps)
                sample, timestamp = inlet.pull_sample()
                C3 = np.append(C3, sample[0])
                C4 = np.append(C4, sample[1])
                FC5 = np.append(FC5, sample[2])
                FC6 = np.append(FC6, sample[3])
                C1 = np.append(C1, sample[4])
                C2 = np.append(C2, sample[5])
                CP5 = np.append(CP5, sample[6])
                CP6 = np.append(CP6, sample[7])
            break

        print("C3 raw: ")
        print(C3)

        # Surface Laplacian
        C3_oc = surface_laplacian(C3, FC5, C1, CP5)
        C4_oc = surface_laplacian(C4, FC6, C2, CP6)
        oc = np.array([C3_oc, C4_oc])
        print("Output Channels: ")
        print(oc)
        print("Dimensions: ")
        print(oc.shape)

        # Bandpass Filter to Mu (500Hz, 9-11Hz)
        fs = 500.0
        lowcut = 9.0
        highcut = 11.0

        eeg_filtered = butter_bandpass_filter(oc, lowcut, highcut, fs, order=5)
        print("Mu signal: ")
        print(eeg_filtered)

        # Get Mu Power
        eeg_powered = spectral_bandpower(eeg_filtered)
        print("Mu power: ")
        print(eeg_powered)
        
        # Averaging over time
        eeg_ave, new_timesteps = moving_average(eeg_powered, sampling_freq)
        print("Averaging over time: ")
        print(eeg_ave)

        # Baseline Correction (3.5 secs = 35 samples)                                   comment out
        eeg_basecorr = baseline_correction(eeg_ave, baseline_duration)
        print("Baseline corrected: ")
        print(eeg_basecorr)
        
        # Save time series for C3 and C4 in trials array (3rd D)
        # Dimensions; (no_trials x no_channels x new_timesteps)

        ds_eeg[trial_count,0,:] = eeg_ave[0,:]
        ds_eeg[trial_count,1,:] = eeg_ave[1,:]

        # Plotting
        f, ax = plt.subplots(1)
        x_point = np.arange(new_timesteps)
        ax.plot(x_point, eeg_ave[0,:], 'ro')
        ax.plot(x_point, eeg_ave[1,:], 'bo')
        plt.show()

        # Clear Memory
        # send something to Test_excel
        trial_count = trial_count + 1
        C3 = np.zeros([])
        C4 = np.zeros([])
        FC5 = np.zeros([])
        FC6 = np.zeros([])
        C1 = np.zeros([])
        C2 = np.zeros([])
        CP5 = np.zeros([])
        CP6 = np.zeros([])
       """ 

    #elif get_readycue == "":
        #print("okay")
        #print(ds_eeg)
        #break