# %%
import pyxdf
import pandas as pd
import numpy as np
import math
from braindecode.datautil import create_from_X_y
from IPython.display import display

# %%
# Create dataset

data, header = pyxdf.load_xdf('E:\\bci\\data\\test.xdf')

# %%
data, header = pyxdf.load_xdf('E:\\bci\\data\\test2.xdf')

# %%

# Extract EEG
eeg = data[0]['time_series']

# Extract events
extract_events = data[1]['time_series']
events = []

for event in extract_events:
    event = int(event[0])
    events.append(event)

events = events[1:] # remove practice trial
print(events)


#%%
# Get events
eeg_time_stamps = pd.DataFrame(data[0]['time_stamps'])
eeg_time_stamps = eeg_time_stamps.round(decimals=3) # shift offset to even numbers
eeg_merg = pd.concat([pd.DataFrame(eeg_time_stamps), pd.DataFrame(eeg)], axis=1)
eeg_merg.columns = ["time", "C3", "C4", "FC5", "FC6", "C1", "C2", "CP5", "CP6"]
event_time_stamps = data[1]['time_stamps']
event_time_stamps = event_time_stamps[1:]
event_time_stamps = event_time_stamps.round(decimals=2)
event_merg = pd.concat([pd.DataFrame(event_time_stamps), pd.DataFrame(events)], axis=1)
event_merg.columns = ["time", "events"]
eeg_events = eeg_merg.merge(event_merg, on='time', how='left')
print(eeg_events)
event_index = eeg_events.index[(eeg_events['events'] == 0) | (eeg_events['events'] == 1)].tolist()
print(event_index)

# %%
# Generate labels
labels = pd.DataFrame.dropna(pd.DataFrame(eeg_events['events']))
labels = labels.values.tolist()
y = []
for label in labels:
    label = np.int64(label[0])
    y.append(label)

print(y)

# Epoching
sfreq = 500
epoch_start = 0.5 * sfreq # before trial cue
epoch_end = 4.5 * sfreq

epoched_trials = np.ndarray(shape=(len(y),8,2500), dtype=float)
trial = 0

# %%

for epoch in event_index:
    epoch_start_index = int(epoch - epoch_start)
    epoch_end_index = int(epoch + epoch_end)
    epoch_x = np.array(eeg_events[epoch_start_index:epoch_end_index])[:,1:9]
    epoch_x = np.transpose(epoch_x)
    epoched_trials[trial,:,:] = epoch_x[:,:]
    trial += 1

X = np.float32(epoched_trials)

print(np.shape(X))
print(np.shape(y))

# Create dataset for BrainDecode
ch_names = ["C3", "C4", "FC5", "FC6", "C1", "C2", "CP5", "CP6"]

windows_dataset = create_from_X_y(
    X, y, drop_last_window=False, sfreq=sfreq, ch_names=ch_names,
    window_stride_samples=500,
    window_size_samples=500,
)














# %%
# Split dataset into 2 for training and validation
ds_1 = list(range(40))
ds_2 = list(range(12))
splitted = windows_dataset.split([ds_1, ds_2])

train_set = splitted['0']
valid_set = splitted['1']

display(splitted)
display(splitted['0'].description)
display(splitted['1'].description)

# %%
# Create a model

import torch
from braindecode.util import set_random_seeds
from braindecode.models import ShallowFBCSPNet

cuda = torch.cuda.is_available()  # check if GPU is available, if True chooses to use it
device = 'cuda' if cuda else 'cpu'
if cuda:
    torch.backends.cudnn.benchmark = True
seed = 20200220  # random seed to make results reproducible
# Set random seed to be able to reproduce results
set_random_seeds(seed=seed, cuda=cuda)

n_classes=2

# Extract number of chans and time steps from dataset
n_chans = train_set[0][0].shape[0]
input_window_samples = train_set[0][0].shape[1]

model = ShallowFBCSPNet(
    n_chans,
    n_classes,
    input_window_samples=input_window_samples,
    final_conv_length='auto',
)

# Send model to GPU
if cuda:
    model.cuda()

# %%
# Train Neural Network

from skorch.callbacks import LRScheduler
from skorch.helper import predefined_split

from braindecode import EEGClassifier
# These values we found good for shallow network:
lr = 0.0625 * 0.01
weight_decay = 0

# For deep4 they should be:
# lr = 1 * 0.01
# weight_decay = 0.5 * 0.001

batch_size = 64
n_epochs = 12

clf = EEGClassifier(
    model,
    criterion=torch.nn.NLLLoss,
    optimizer=torch.optim.AdamW,
    train_split=predefined_split(valid_set),  # using valid_set for validation
    optimizer__lr=lr,
    optimizer__weight_decay=weight_decay,
    batch_size=batch_size,
    callbacks=[
        "accuracy", ("lr_scheduler", LRScheduler('CosineAnnealingLR', T_max=n_epochs - 1)),
    ],
    device=device,
)
# Model training for a specified number of epochs. `y` is None as it is already supplied
# in the dataset.
clf.fit(train_set, y=None, epochs=n_epochs)

# %%
# Plot results

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd
# Extract loss and accuracy values for plotting from history object
results_columns = ['train_loss', 'valid_loss', 'train_accuracy', 'valid_accuracy']
df = pd.DataFrame(clf.history[:, results_columns], columns=results_columns,
                  index=clf.history[:, 'epoch'])

# get percent of misclass for better visual comparison to loss
df = df.assign(train_misclass=100 - 100 * df.train_accuracy,
               valid_misclass=100 - 100 * df.valid_accuracy)

plt.style.use('seaborn')
fig, ax1 = plt.subplots(figsize=(8, 3))
df.loc[:, ['train_loss', 'valid_loss']].plot(
    ax=ax1, style=['-', ':'], marker='o', color='tab:blue', legend=False, fontsize=14)

ax1.tick_params(axis='y', labelcolor='tab:blue', labelsize=14)
ax1.set_ylabel("Loss", color='tab:blue', fontsize=14)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

df.loc[:, ['train_misclass', 'valid_misclass']].plot(
    ax=ax2, style=['-', ':'], marker='o', color='tab:red', legend=False)
ax2.tick_params(axis='y', labelcolor='tab:red', labelsize=14)
ax2.set_ylabel("Misclassification Rate [%]", color='tab:red', fontsize=14)
ax2.set_ylim(ax2.get_ylim()[0], 85)  # make some room for legend
ax1.set_xlabel("Epoch", fontsize=14)

# where some data has already been plotted to ax
handles = []
handles.append(Line2D([0], [0], color='black', linewidth=1, linestyle='-', label='Train'))
handles.append(Line2D([0], [0], color='black', linewidth=1, linestyle=':', label='Valid'))
plt.legend(handles, [h.get_label() for h in handles], fontsize=14)
plt.tight_layout()
# %%
