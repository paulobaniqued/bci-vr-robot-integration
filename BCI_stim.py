#/////////////////////////////////////////////////////////////////////////PREPARED WORKSHEET
import xlsxwriter
import os
import time
import random 
import xlsxwriter

from pylsl import StreamInfo, StreamOutlet


info = StreamInfo('MyMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')
outlet = StreamOutlet(info)

TestWorkbook = xlsxwriter.Workbook('./EEGspreadsheet/test_data.xlsx') #Creates an excel file called "test_data"
SamplesWorksheet = TestWorkbook.add_worksheet( 'data' ) #Creates a spreadsheet within "test_data" called "data"


#///////////////////////////////////////////////////////////////////////////FILLING IN THE WORKSHEET BASED ON A COUNTER




#20R & 20L trials
trial_list = ["R","R","R","R","R","R","R","R","R","R","L","L","L","L","L","L","L","L","L","L"]
random.shuffle(trial_list)
print(trial_list)
print(len(trial_list))

#Key for initiating the display function
play = "play"


#once the display is initiated there will be a 20s preparation time
#the display will play the previously agreed sequence until all of the items from the cue list are displayed
def display(key):
  
    outlet.push_sample(['1']) #Marker1
    
    print("Playing...") 
    
    time.sleep(5)
    #os.system('cls')
    trial_number = 1

    while key == "play":

        for letter in range(len(trial_list)):

            outlet.push_sample(['2']) #Marker2
            print("Get ready.") 
            time.sleep(3.5)
            #os.system('cls')
            
            SamplesWorksheet.write(("A" + str(trial_number)), trial_number)

            cue_feeder = trial_list.pop()

            if cue_feeder == "L":
                
                outlet.push_sample(['3']) #Marker3
                print("L")
                time.sleep(6.5)
                #os.system('cls')
                SamplesWorksheet.write(("B" + str(trial_number)), "C3") #update workbook with value from the EEGprocessor for C3
                SamplesWorksheet.write(("C" + str(trial_number)), "C4") #update workbook with value from the EEGprocessor for C4
                SamplesWorksheet.write(("D" + str(trial_number)), "L") #update workbook with 'L' classification 
                trial_number += 1

            elif cue_feeder == "R":
                
                outlet.push_sample(['4']) #Marker4
                print("R")
                time.sleep(6.5)
                #os.system('cls')
                SamplesWorksheet.write(("B" + str(trial_number)), "C3") #update workbook with value from the EEGprocessor for C3
                SamplesWorksheet.write(("C" + str(trial_number)), "C4") #update workbook with value from the EEGprocessor for C4
                SamplesWorksheet.write(("D" + str(trial_number)), "R") #update workbook with 'R' classification 
                trial_number += 1

            else:
                print("blank")
            

            outlet.push_sample(['5']) #Marker5
            print("Rest")
            time.sleep(2.5)
            #os.system('cls')

        break
    
    outlet.push_sample(['6']) #Marker6
    print("End of trials") 
    TestWorkbook.close() #close workbook so that the training data file saves
    

display(play)
