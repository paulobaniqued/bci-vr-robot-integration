"""Background EEG Processor 
From Raw Data to 2-channel Mu Power"""

from pylsl import StreamInlet, resolve_stream
import numpy as np

while True:
    # Resolve an EEG stream on the lab network
    # print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
        
    # Create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])
    
    #create trial list
    C3 = np.array([])
    C4 = np.array([])
    FC5 = np.array([])
    FC6 = np.array([])
    C1 = np.array([])
    C2 = np.array([])
    CP5 = np.array([])
    CP6 = np.array([])
    
    get_readycue = input("Start sampling? Y/N: ")

    if get_readycue == "Y":

        # Data Acquisition from LSL stream
        while True:
            for i in range(4250): # 1 second for now
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
        C3_oc1 = 4*C3 - 1*FC5 - 1*C1 - 1*CP5
        C4_oc2 = 4*C4 - 1*FC6 - 1*C2 - 1*CP6
        print("Output Channel 1: ")
        print(C3_oc1)
        print("Dimensions: ")
        print(C3_oc1.shape)

    elif get_readycue == "N":
        print("okay")
        break
