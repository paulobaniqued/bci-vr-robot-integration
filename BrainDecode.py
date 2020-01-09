# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:29:24 2019

@author: max

Much of the code is from https://tntlfreiburg.github.io/braindecode/notebooks/Trialwise_Decoding.html
Go there to get a better understanding
I've added some comments, the getModel() function, and the plots

For trialling your own eeg data on this, seperate your data into train_set and
valid_set (see tutorial for info on data structure), choose deep (1) or shallow (0) 
model, and run!
"""

import logging
import importlib
importlib.reload(logging) # see https://stackoverflow.com/a/21475297/1469195
log = logging.getLogger()
log.setLevel('INFO')
import sys
import mne
from mne.io import concatenate_raws

logging.basicConfig(format='%(asctime)s %(levelname)s : %(message)s',
                     level=logging.INFO, stream=sys.stdout)

############################## Data formatting ################################
# EEG data should be formatted nDarray: nTrials * mChannels * tTimesteps
# labels should be formatted array: nTrials 
import numpy as np

# Load training data
training_data = np.load('training_data_raw.npy')
training_data = np.float32(training_data)
print(training_data)
print(np.shape(training_data))
print(training_data.dtype)

# Load labels
labels = np.load('training_labels.npy')
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
valid_set = SignalAndTarget(X[40:60], y=y[40:60])
print("valid set: ", valid_set)
test_set = SignalAndTarget(X[60:], y=y[60:])
print("test set: ", test_set)

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

model.fit(train_set.X, train_set.y, epochs=40, batch_size=64, scheduler='cosine',
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
#plt.savefig('EEGnet results') # to save .png
plt.show()

################################## Testing ####################################

output = model.evaluate(test_set.X,test_set.y)
loss = output['loss']
error = output['misclass']
acc = 1 - error
print("Test loss: ", loss)
print("Test error: ", error)
print("Test accuracy: ", acc)
predictedLabels = model.predict_classes(test_set.X)
actualLabels = test_set.y
#to see predicted and actual labels
print("predicted labels vs actual", [predictedLabels,actualLabels])