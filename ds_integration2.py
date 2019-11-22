# Generate random numbers and arrange in 3D array (no_timesteps x no_channels x no_trials)
# Plot each trial
# Working as of 22-11-2019
import numpy as np
import random
import matplotlib.pyplot as plt

no_timesteps = 100
no_channels = 2
no_trials = 10

trial_counter = 0
sample_counter = 0

ds_eeg = np.ndarray(shape=(no_timesteps, no_channels, no_trials), dtype=float)

for i in range(no_trials):
    x_point = [i for i in range(0,100)]
    y_point_1 = []
    y_point_2 = []

    for x in range(no_timesteps): #C3
        signal_value = np.random.random_sample()
        ds_eeg[sample_counter,0,trial_counter] = signal_value
        y_point_1.append(signal_value)
        sample_counter = sample_counter + 1

    sample_counter = 0

    for x in range(no_timesteps): #C4
        signal_value = np.random.random_sample()
        ds_eeg[sample_counter,1,trial_counter] = signal_value
        y_point_2.append(signal_value)
        sample_counter = sample_counter + 1

    sample_counter = 0
    trial_counter = trial_counter + 1

    f, ax = plt.subplots(1)
    ax.plot(x_point, y_point_1, 'ro')
    ax.plot(x_point, y_point_2, 'bo')

print(ds_eeg)
plt.show()


