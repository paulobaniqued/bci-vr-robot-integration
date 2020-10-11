# %%
# Import packages
import mne
import numpy as np
from scipy.io import loadmat

#%%
# Import file
file = loadmat('E:/brain-io-hack/P1_pre_training.mat')
file.keys()
raw_eeg = np.array(file['y'])
events = np.array(file['trig'])
fs = int(file['fs'])
trial_duration = 8 #seconds
timesteps = fs*trial_duration
n_channels = int(16)
events = events[timesteps:]
padding = np.zeros(timesteps).reshape(timesteps,1)
events = np.concatenate((events, padding))

eeg = np.concatenate((events, raw_eeg), axis=1)
eeg = eeg[eeg[:,0] != 0]
left_raw = eeg[eeg[:,0] == 1]
left_raw = left_raw[:,1:]
right_raw = eeg[eeg[:,0] == -1]
right_raw = right_raw[:,1:]

# compensate for missing values
lh_trials = 40
rh_trials = 39
left_raw = left_raw[:timesteps*lh_trials,:] 
right_raw = right_raw[:timesteps*rh_trials,:] 

# transpose (n_channels x timesteps)
left_raw = np.transpose(left_raw)
right_raw = np.transpose(right_raw)

def data_structure(trials, n_channels, timesteps):
    ds_eeg = np.ndarray(shape=(trials, n_channels, timesteps), dtype=float)
    return ds_eeg

#%%
# Organise tensor per class
left_tidy = data_structure(lh_trials, n_channels, timesteps)
trial_count = 0
ts_begin = 0
ts_end = timesteps

for i in range(lh_trials):
    left_trial = left_raw[:,ts_begin:ts_end]
    left_tidy[trial_count,:,:] = left_trial[:,:]
    trial_count = trial_count + 1
    ts_begin = ts_begin + timesteps
    ts_end = ts_end + timesteps

right_tidy = data_structure(rh_trials, n_channels, timesteps)
trial_count = 0
ts_begin = 0
ts_end = timesteps

for i in range(rh_trials):
    right_trial = right_raw[:,ts_begin:ts_end]
    right_tidy[trial_count,:,:] = right_trial[:,:]
    trial_count = trial_count + 1
    ts_begin = ts_begin + timesteps
    ts_end = ts_end + timesteps

# %%
# Notch Filter at 50 Hz
left_notch = mne.filter.notch_filter(left_tidy, fs, 49)
right_notch = mne.filter.notch_filter(right_tidy, fs, 49)

# Bandpass Filter at 8-30 Hz
left_bp = mne.filter.filter_data(data=left_notch, sfreq=fs, l_freq=8, h_freq=30.5, method='iir', fir_design='firwin')
right_bp = mne.filter.filter_data(data=right_notch, sfreq=fs, l_freq=8, h_freq=30.5, method='iir', fir_design='firwin')

# %%
# Common Spatial Patterns (CSP) github.com/spolsley/common-spatial-patterns

import scipy.linalg as la

def CSP(*tasks):
	if len(tasks) < 2:
		print("Must have at least 2 tasks for filtering.")
		return (None,) * len(tasks)
	else:
		filters = ()
		# CSP algorithm
		# For each task x, find the mean variances Rx and not_Rx, which will be used to compute spatial filter SFx
		iterator = range(0,len(tasks))
		for x in iterator:
			# Find Rx
			Rx = covarianceMatrix(tasks[x][0])
			for t in range(1,len(tasks[x])):
				Rx += covarianceMatrix(tasks[x][t])
			Rx = Rx / len(tasks[x])

			# Find not_Rx
			count = 0
			not_Rx = Rx * 0
			for not_x in [element for element in iterator if element != x]:
				for t in range(0,len(tasks[not_x])):
					not_Rx += covarianceMatrix(tasks[not_x][t])
					count += 1
			not_Rx = not_Rx / count

			# Find the spatial filter SFx
			SFx = spatialFilter(Rx,not_Rx)
			filters += (SFx,)

			# Special case: only two tasks, no need to compute any more mean variances
			if len(tasks) == 2:
				filters += (spatialFilter(not_Rx,Rx),)
				break
		return filters

# covarianceMatrix takes a matrix A and returns the covariance matrix, scaled by the variance
def covarianceMatrix(A):
	Ca = np.dot(A,np.transpose(A))/np.trace(np.dot(A,np.transpose(A)))
	return Ca

# spatialFilter returns the spatial filter SFa for mean covariance matrices Ra and Rb
def spatialFilter(Ra,Rb):
	R = Ra + Rb
	E,U = la.eig(R)

	# CSP requires the eigenvalues E and eigenvector U be sorted in descending order
	ord = np.argsort(E)
	ord = ord[::-1] # argsort gives ascending order, flip to get descending
	E = E[ord]
	U = U[:,ord]

	# Find the whitening transformation matrix
	P = np.dot(np.sqrt(la.inv(np.diag(E))),np.transpose(U))

	# The mean covariance matrices may now be transformed
	Sa = np.dot(P,np.dot(Ra,np.transpose(P)))
	Sb = np.dot(P,np.dot(Rb,np.transpose(P)))

	# Find and sort the generalized eigenvalues and eigenvector
	E1,U1 = la.eig(Sa,Sb)
	ord1 = np.argsort(E1)
	ord1 = ord1[::-1]
	E1 = E1[ord1]
	U1 = U1[:,ord1]

	# The projection matrix (the spatial filter) may now be obtained
	SFa = np.dot(np.transpose(U1),P)
	return SFa.astype(np.float32)

csp_filtered = CSP(left_bp, right_bp) # outputs a 16 x 16 matrix per class
