# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:05:36 2016

@author: nneveu
"""


'''Important'''
#   Make sure that the folder you saved ReadScopeTracesSDDSAvg.py in 
#    is listed in the path.append line. This will allow you to import 
#    and use the ICT charge script. 
#The following two lines add a folder to pythons path. 
import sys
sys.path.append('/Users/nneveu/Desktop/Scripts/dataAnalysis')

import glob
#Importing ICT function
import ReadScopeTracesSDDSAvg

import numpy as np


#Making a list of SDDS files
files = glob.glob( 'C:/Users/nneveu/Desktop/Scripts/dataAnalysis/*.sdds')

i=0
minvolts = np.zeros([1,8])
charges = np.zeros([30,2])
#Looping through every file
for filenames in files:
    #Printing charge information to the output line
    [voltage, charge] = ReadScopeTracesSDDSAvg.ICTcharge(filenames)  
    #print np.min(voltage['ch1'])
    #charges[i,0] = charge['ch1']
    #charges[i,1] = charge['ch2']
    i=i+1
    
#Note: 
#   Pdfs of all the voltage curves will be saved in the same 
#   folder as the sdds file, and the charge values will be printed to the terminal. 
#   However, all of the voltage and charge values are NOT saved to variables.
#   Only the last file's data is saved. If you want to look at a specific
#    file's data, in variable form, use the follwoing format in triple quotes('''):
    
'''
filename = 'nameOfSDDSfile.sdds'
[voltage, charge] = ReadScopeTracesSDDSAvg.ICTcharge(filename)   
'''   

#file = 'C:/Users/nneveu/Desktop/Scripts/dataAnalysis/DY1_M190_NicoleLC584AL.sdds'
#[voltage, charge] = ReadScopeTracesSDDSAvg.ICTcharge(file)  
#print np.min(voltage['ch1'])

#print np.average(charges[:,0])
#print np.average(charges[:,1])