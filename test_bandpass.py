import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt, sosfreqz, filtfilt

""" WORKING Band-pass filter as of 13-Jan-2020 """

# Sample rate and desired cutoff frequencies (in Hz).
fs = 500.0
lowcut = 7.5
highcut = 11.5

def butter_lowpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band', analog = False)
    return b, a

def butter_lowpass_filter(data, lowcut, highcut, fs, order=4):
    #nyq = 0.5 * fs
    #low = lowcut / nyq
    b, a = butter_lowpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

def zero_order_butterworth(data, order, fs, low_cutoff, high_cutoff):
    x = np.empty(trial.shape)
    x = butter_lowpass_filter(data, 7.5, 11.5, fs, order=4)
    return x

# Load training data
training_data = np.load('training_data_raw_1.npy')
training_data = np.float32(training_data)
print(training_data)
print(np.shape(training_data))
print(training_data.dtype)

trial_number = 56
#choose from 0 - 79

trial = training_data[trial_number,:,1:5000]
print(trial)
print(np.shape(trial))

# Plotting Raw
f, ax = plt.subplots()
x_point = np.arange(4999)
ax.plot(x_point, trial[0,:])
ax.plot(x_point, trial[1,:])
ax.plot(x_point, trial[2,:])
ax.plot(x_point, trial[3,:])
ax.plot(x_point, trial[4,:])
ax.plot(x_point, trial[5,:])
ax.plot(x_point, trial[6,:])
ax.plot(x_point, trial[7,:])
plt.show()

eeg_filtered = zero_order_butterworth(trial, 4, fs, lowcut, highcut)
print(eeg_filtered)

# Plotting Filtered
f, ax = plt.subplots()
x_point = np.arange(4999)
ax.plot(x_point, eeg_filtered[0,:])
ax.plot(x_point, eeg_filtered[1,:])
ax.plot(x_point, eeg_filtered[2,:])
ax.plot(x_point, eeg_filtered[3,:])
ax.plot(x_point, eeg_filtered[4,:])
ax.plot(x_point, eeg_filtered[5,:])
ax.plot(x_point, eeg_filtered[6,:])
ax.plot(x_point, eeg_filtered[7,:])
plt.show()