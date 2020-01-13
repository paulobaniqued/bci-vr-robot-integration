import numpy as np

# Load training data
training_data = np.load('training_data_raw_1.npy')
training_data = np.float32(training_data)
print(training_data)
print(np.shape(training_data))
print(training_data.dtype)

# Load labels
labels = np.load('training_labels_1.npy')
print(labels)
print(np.shape(labels))
print(labels.dtype)

trial = training_data[10,:,:]
print(trial)
print(np.shape(trial))