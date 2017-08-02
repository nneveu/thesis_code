# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:23:58 2016

@author: nneveu
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


#data = np.loadtxt('BF_550.T7', skiprows=5)
data = np.loadtxt('../OPAL/AWAFieldFiles/Drive/Gun&Sol/M_440.T7', skiprows=5)

plt.plot(data[:,1][0:50])

print np.min(data[:,1])
#==============================================================================
 
# import sys
# sys.path.append('/Users/nneveu/Documents/PythonScripts')
# import myplots as mplt
# 
# 
# #Find Min in Mag file
# #old = np.loadtxt('M_440.T7', skiprows= 3)
# #new = np.loadtxt('BFS_501.T7', skiprows=2)
# 
# #print 'old max = ', np.min(old[:,1])
# #print 'new max = ', np.min(new[:,1])
# 
# 
# csr1 = mplt.load('rectDipoleCSR1.stat', 57)
# #csr2 = mplt.load('OUTAnlysGun2.mat')
# 
# 
# plottype = 'energy'
# 
# mplt.plotformat(ptype=plottype, x1=0.0, x2=3.0, y1 = 100.4, y2 =100.55, sigma=1)
# mplt.plotting(csr1, ptype=plottype,  mylabel='OPAL', legendloc='lower right', sigma=1)
# 
# 
# plt.savefig('Energy.pdf', bbox_inches='tight')
#==============================================================================


