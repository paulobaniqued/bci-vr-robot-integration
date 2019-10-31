"""Background EEG Processor 
From Raw Data to 2-channel Mu Power"""

from pylsl import StreamInlet, resolve_stream
from scipy.signal import butter, lfilter
import numpy as np
import mne
import matplotlib.pyplot as plt

#create trial list for channels
C3 = np.array([])
C4 = np.array([])
FC5 = np.array([])
FC6 = np.array([])
C1 = np.array([])
C2 = np.array([])
CP5 = np.array([])
CP6 = np.array([])




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
    return eeg_powered




""" MAIN PROCESS PIPELINE """

while True:
    # Resolve an EEG stream on the lab network
    # print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
        
    # Create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    get_readycue = input("Start sampling? Y/N: ")

    if get_readycue == "Y":

        # Data Acquisition from LSL stream
        while True:
            for i in range(4750): # 1750 samples (3.5s) baseline, 3000 samples (6.0s) trial
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
        C3_oc1 = surface_laplacian(C3, FC5, C1, CP5)
        C4_oc2 = surface_laplacian(C4, FC6, C2, CP6)
        oc = np.array([C3_oc1, C4_oc2])
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
        plt.plot(eeg_powered)

    elif get_readycue == "N":
        print("okay")
        break