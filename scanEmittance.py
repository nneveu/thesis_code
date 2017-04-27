# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:00:51 2016

@author: nneveu

Scan .stat files for lowest emittance
"""

import sys
import glob
import numpy as np
#import matplotlib.pyplot as plt
sys.path.append('/Users/nneveu/Documents/PythonScripts')
import myplots as mplt


#Making a list of SDDS files
files = glob.glob( 'C:/Users/nneveu/Desktop/Scripts/benchmark/gridcompare/*3D*.stat')

emittanceMin    = 1000000
filemin         = '.'

#Looping through every .stat file
for filename in files:
    #filename = 'optLinac.stat'
    #print filename.split('.')[0]
    data    = mplt.load(filename)
    zloc    = np.argmax(data['z']>0.3)    
    #zloc    = np.where(data['z']>0.3)[0][0]
    tempmin = np.min(data['xemit'][zloc:])
    print(filename)
    print(tempmin)
    #print tempmin
    
    if tempmin < emittanceMin:
        emittanceMin    = tempmin
        filemin         = filename
    
    #print data['z'][np.where(data['xemit']==emittanceMin)[0]]
    #print emittanceMin
    #print filemin.split('\\')[1]
    

