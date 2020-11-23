#%%
import os
import numpy as np
import mne
#from mne.preprocessing import compute_current_source_density
%matplotlib qt

#%%
# Load data
sample_data_raw_file = '1.edf'
raw = mne.io.read_raw_edf(sample_data_raw_file,preload=True)
print(raw.info)
data = raw.get_data()
print(data)
print(raw.ch_names)

#%%
new_data = data[0:8, :]
print(new_data.shape)










#%%
# Let's pick the EEG channels
raw.pick_types(eeg=True,meg=False,stim=True,eog=True)
#%%

#%%
# Plot the power spectrum
raw.plot_psd(fmin=1,fmax=60,n_fft=2**10,spatial_colors=True)
#%%

#%%
# Plot the first five seconds of data
raw.plot(duration=5, n_channels=30,show=True)
#%%

#%%
# Train independent component analysis (ICA) and plot components
ica = mne.preprocessing.ICA(n_components=10, random_state=97, max_iter=800)
ica.fit(raw)
ica.plot_components()
#%%

#%%
# Make a copy of the original raw data and apply the ICA to one of the copies (reject artifact components)
orig_raw = raw.copy()
ica.apply(raw)
#%%

#%%
# Plot the original raw data and the new data with ICA applied
orig_raw.plot(start=0, duration=5,block=False)
raw.plot(start=0, duration=5,block=True)
#%%

#%%
# Find the events (markers/triggers) in the data
events = mne.events_from_annotations(raw)
print(events[:5])
#%%

#%%
# Give the events names as a dictionary
event_dict = {'play' : 0, 'begin': 1, 'get ready': 2, 'trigger left': 3,
              'trigger right': 4, 'rest': 5, 'end': 6}
#%%


#%%
# Use convenience function to plot the events over the time of the entire recording
fig = mne.viz.plot_events(events, event_id=event_dict, sfreq=raw.info['sfreq'],
                          first_samp=raw.first_samp)
#%%


#%%
# Define signal amplitudes that are too large to originate from the brain
# We want to exclude epochs of data where the signal exceeds these amplitudes
reject_criteria = dict(eeg=150e-6,       # 150 µV
                       eog=250e-6)       # 250 µV
#%% 

#%%
# Construct epochs of data, excluding epochs with large signal amplitudes
epochs = mne.Epochs(raw, events, event_id=event_dict, tmin=-0.2, tmax=0.5,
                    reject=reject_criteria, preload=True)
#%%

#%%
# Takes an equal number of trials for each condition for a fair comparison
epochs.equalize_event_counts(['auditory/left', 'auditory/right','visual/left', 'visual/right'])
aud_epochs = epochs['auditory']
vis_epochs = epochs['visual']
#%%

#%%
# Plot the epochs for auditory and visual stimulation separately
aud_epochs.plot_image(picks=['EEG 021'])
vis_epochs.plot_image(picks=['EEG 059'])
#%%

#%%
# Create a time-frequency analysis of the auditory epochs via Morlet wavelets
frequencies = np.arange(7, 30, 3)
power = mne.time_frequency.tfr_morlet(aud_epochs, n_cycles=2, return_itc=False,
                                      freqs=frequencies, decim=3)
power.plot(picks=['EEG 021'])
#%%

#%%
# Construct evoked responses from the epochs by averaging across trials
aud_evoked = aud_epochs.average()
vis_evoked = vis_epochs.average()
#%%

#%%
# Plot the evoked responses across all sensors for auditory stimulation
aud_evoked.plot_joint(picks='eeg')
#%%

#%%
# Plot the evoked response for auditory stimulation as a topographical map at selected timepoints
aud_evoked.plot_topomap(times=[0., 0.08, 0.1, 0.12, 0.2], ch_type='eeg')
#%%

#%%
# Plot the evoked response across all sensors for visual stimulation
vis_evoked.plot_joint(picks='eeg')
#%%

#%%
# Plot the evoked response for visual stimulation as a topographical map at selected timepoints
vis_evoked.plot_topomap(times=[0., 0.08, 0.1, 0.12, 0.2], ch_type='eeg')
#%%

#%%
# Plot the evoked response at a topographical map at all timepoints
vis_evoked.plot_topo(color='r', legend=False)
#%%

#%%
# Try different reference channels to see how they influence visual evoked respones
vis_evoked.plot_joint(picks='eeg')
vis_evoked.set_eeg_reference(ref_channels='average').plot_joint(picks='eeg')
#%%