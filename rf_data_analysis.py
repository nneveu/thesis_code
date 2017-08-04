# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 10:23:59 2017

@author: nneveu

Script to analyze RF csv files
"""

import csv 
import glob
import matplotlib.pyplot as plt
import pandas as pd

#Total number of files = 60

datadir = "./data"
ict_curves         = glob.glob('./data/C3*')
rf_curves_withbeam = glob.glob('./data/C2*[3][4-9].*')

rf_curves_zoom     = glob.glob('./data/C2*[3][0-3].*')
rf_curves_zoom.extend(glob.glob('./data/C2*[2][6-9].*'))

rf_curves_norm     = glob.glob('./data/C2*[2][0-5].*')
rf_curves_norm.extend(glob.glob('./data/C2*000[0-9].*'))
rf_curves_norm.extend(glob.glob('./data/C2*001[0-9].*'))

header1 = 'Time'
header2 = 'Ampl'

for filename in rf_curves_zoom:
    df = pd.read_csv(filename, skiprows=3, header=1)
    plt.figure()
    
    
    #ICT bounds
    #plt.axis((0.00000715,0.00000735,-2.4,1.5))
    plt.plot(df.Time, df.Ampl)
    #time = df.Time
    #ampl = df.Ampl
    #plt.plot()


