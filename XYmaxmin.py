# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 12:32:42 2016

@author: nneveu

x and y max, min trajectories 
"""


import numpy as np
import matplotlib.pyplot as plt
import sys
import h5py

sys.path.append('/Users/nneveu/Documents/PythonScripts')
import myplots as mplt

run = 'zoomedin'


myfile = 'dipoleKicker20m.h5'
angledata = mplt.load('dipoleKicker20m.stat', 56)


hf = h5py.File(myfile, 'r')
steps = len(hf.keys())-1
#steps = 120
xmin = np.zeros((steps,1))
xmax = np.zeros((steps,1))
ymin = np.zeros((steps,1))
ymax = np.zeros((steps,1))
avez = np.zeros((steps,1))


for i in np.arange(0,steps):
    
    x  = np.asarray(hf.get('/Step#'+str(i)+'/x' ))*10.0**3.0
    #px  = np.asarray(hf.get('/Step#'+str(steps-1)+'/px' ))*0.511
    #py  = np.asarray(hf.get('/Step#'+str(steps-1)+'/py' ))*0.511
    y  = np.asarray(hf.get('/Step#'+str(i)+'/y'))*10.0**3.0
    z  = np.asarray(hf.get('/Step#'+str(i)+'/z'))

    xmin[i,0] = min(x)
    xmax[i,0] = max(x)
    ymin[i,0] = min(y)
    ymax[i,0] = max(y)
    avez[i,0] = np.average(z)

#==============================================================================
# plt.figure(2)
# plt.show(block=False) 
# plt.axis((15, 16.2, 0, 20))
# plt.title( r'Beam Size, 2 $^\circ$ Kick' , size=18)
# plt.xlabel(r'z [m]', size=18)
# plt.ylabel(r' [mm]', size=18)
# plt.plot(angledata['z'], 3*angledata['xrms'], 'b-', label = '3$\sigma_x$')
# plt.plot(angledata['z'], 3*angledata['yrms'], 'b--', label = '3$\sigma_y$')
# plt.plot(angledata['z'], angledata['xmax'], 'r-', label = 'xmax')
# plt.plot(angledata['z'], angledata['ymax'], 'r--', label = 'ymax')
# 
# plt.plot((15.3, 15.3), (0.0, 15.0), 'k-')
# plt.plot((15.9, 15.9), (0.0, 15.0), 'k-')
# plt.plot((15.3, 15.9), (15.0, 15.0), 'k-', label=r'Kicker')
# 
# 
# 
# plottitle = 'XminXmax' +run +'.pdf'
# plt.legend(loc='best')
# plt.savefig(plottitle, bbox_inches='tight')
#==============================================================================



#MAX MIN PLOTS 
plt.figure(2)
#plt.plot(angledata['z'], 3*angledata['xrms'], 'b-', label = '3$\sigma_x$')
#plt.plot(angledata['z'], 3*angledata['yrms'], 'b--', label = '3$\sigma_y$')

plt.plot(avez, xmax, 'b', label='xmax and xmin')
plt.plot(avez, ymax, 'g-', label='ymax and ymin')
plt.plot(avez, xmin, 'b')
plt.plot(avez, ymin, 'g-')
plt.legend(loc = 'best')


#==============================================================================
# plt.plot((15.3, 15.3), (-15.0, 15.0), 'r-')
# plt.plot((15.9, 15.9), (-26.0, 4.0), 'r-')
# plt.plot((15.3, 15.9), (-15.0, -26.0), 'r-', label=r'Kicker')
# plt.plot((15.3, 15.9), (15.0, 4.0), 'r-')
#==============================================================================

plt.plot((15.3, 15.3), (-9.0, 21.0), 'k-')
plt.plot((15.9, 15.9), (-21, 9.0), 'k-')
plt.plot((15.3, 15.9), (-9.0, -21), 'k-', label=r'Kicker')
plt.plot((15.3, 15.9), (21.0, 9.0), 'k-')

#plt.plot((15.3, 15.9), (6.0, 6.0), 'k--')

#plt.show(block=False) 
plt.axis((15, 16.2, -40, 40))
#plt.axis((0, 20, -40, 40))
plt.title( r'Max and Min Particle Locations, 2 $^\circ$ Kick' , size=18)
plt.xlabel(r'z [m]', size=18)
plt.ylabel(r'[mm]', size=18)
plt.savefig('maxminzoom.pdf', bbox_inches='tight')








