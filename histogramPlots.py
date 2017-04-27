# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 18:52:25 2016

@author: nneveu
Histogram plots
"""
import h5py 
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import rc

sys.path.append('/Users/nneveu/Documents/PythonScripts')
import myplots as mplt

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

myfile = 'dipoleKicker20m.h5'
zloc = '18.0'
run = 'px-'+zloc

#==============================================================================
# i = 148 #15.9 m 
# i = 150 #16.13 m 
# i = 160 #17.03 m
#==============================================================================
i = 171 #18.0



hf = h5py.File(myfile, 'r')
x  = np.asarray(hf.get('/Step#'+str(i)+'/x' ))*10.0**3.0
px  = np.asarray(hf.get('/Step#'+str(i)+'/px' ))*0.511
#py  = np.asarray(hf.get('/Step#'+str(steps-1)+'/py' ))*0.511
#y  = np.asarray(hf.get('/Step#'+str(i)+'/y'))*10.0**3.0
z  = np.asarray(hf.get('/Step#'+str(i)+'/z'))


print np.average(z)

fig = plt.figure()

plt.plot((15, 15.0), (-15.0, 15.0), 'k-')
plt.plot((-15.0, -15.0), (-15.0, 15.0), 'k-', label=r'Kicker')

#plt.hist2d(x, y, bins=200.0, range=[[-15.0,15.0], [-15.0,15.0]], cmin=1)#, cmap=plt.cm.jet)
#plt.hist2d(x, y, bins=200, range=[[-10.0,10.0], [-10.0,10.0]], cmin = 5)
plt.hist2d(x, px, bins = 200, range=[[-10.0,10.0], [-0.3,0.3]], cmin=5)
#plt.hist2d(y, py, bins = 200, range=[[-10.0,10.0],[-0.3,0.3]], norm = LogNorm())

#==============================================================================
# plt.hist2d(x, y, bins=500.0, range=[[-15.0,15.0], [-15.0,15.0]])#, cmap=plt.cm.jet)
# plt.hist2d(x, y, bins=500.0, range=[[-10.0,10.0], [-10.0,10.0]])#, cmap=plt.cm.jet)
#==============================================================================
#==============================================================================
# plt.axis((-20, 20, -20, 20))
# plt.ylabel('Y [mm]', size = 18.0)
# plt.xlabel('X [mm]', size = 18.0)
# plt.title('Kicker Exit \n 2 $^\circ$ Kick, z = 15.9 [m] ', size=18.0)
# plt.colorbar()
# pdffile = run+'.pdf'
# plt.savefig(pdffile, bbox_inches='tight')
#==============================================================================


plt.title('Beam After Kicker \n z = '+zloc+' [m] ', size=24.0)
#plt.ylabel('Y [mm]', size = 20.0)
plt.ylabel('Px [MeV/c]', size = 20.0)
plt.xlabel('X [mm]', size = 20.0)
#plt.xticks(np.arange(-.015, .016, .005))
#plt.yticks(np.arange(-.015, .016, .005))
plt.colorbar()
pdffile = run+'.pdf'
plt.savefig(pdffile, bbox_inches='tight')


# fig = plt.figure()
# #The first two numbers adjust the position of the plot in x and y. 
# #The second set of numbers set the x and y size of the plot. 
# ax = fig.add_axes([0.25, 0.15, 0.45, 0.7])
# #ax.axis((-0.015, 0.01, -0.015, 0.01))
# plt.title('Beam After Kicker, 20 m after Cathode \n 2 Degrees, Dipole Fringe', size=12)
# #plt.xticks(np.arange(-.015, .016, .005))
# #plt.yticks(np.arange(-.015, .016, .005))
# #ax.set_xlabel('x [mm]', size=18)
# #ax.set_ylabel('y [mm]', size=18)
# 
# 
# #ax.plot(z,x)
# #ax.plot(z2,x2)
#==============================================================================
