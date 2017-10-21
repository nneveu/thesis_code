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
from glob import glob
import myplots as mplt

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
rc('axes', axisbelow=True)

files = glob('*.h5')

for f in files:
    name = f.split('.')[0]
    hf = h5py.File(f, 'r')
    x  = np.asarray(hf.get('/Step#0/x' ))*10.0**3.0
    #px  = np.asarray(hf.get('/Step#0/px' ))*0.511
    #py  = np.asarray(hf.get('/Step#0s-1)+'/py' ))*0.511
    y  = np.asarray(hf.get('/Step#0/y'))*10.0**3.0
    z  = np.asarray(hf.get('/Step#0/z'))
    zloc = str(np.average(z))
    print(len(x))
    
    #Plotting histogram
    plt.figure(f)
    plt.xticks(np.arange(-25, 25, 5))
    plt.yticks(np.arange(-25, 25, 5))
    plt.grid(True)
    plt.hist2d(x, y, bins=200.0, range=[[-25.0,25.0], [-25.0,25.0]], cmin=1, zorder=2)#, cmap=plt.cm.jet)
    #plt.rcParams['axes.axisbelow'] = True
    #plt.grid()
    #plt.hist2d(x, y, bins=200, range=[[-10.0,10.0], [-10.0,10.0]], cmin = 5)
    #plt.hist2d(x, px, bins = 200, range=[[-10.0,10.0], [-0.3,0.3]], cmin=5)
    #plt.hist2d(y, py, bins = 200, range=[[-10.0,10.0],[-0.3,0.3]], norm = LogNorm())


    plt.title(name+ '\n z = '+zloc+' [m] ', size=24.0)
    plt.ylabel('Y [mm]', size = 20.0)
    #plt.ylabel('Px [MeV/c]', size = 20.0)
    plt.xlabel('X [mm]', size = 20.0)
    #plt.xticks(np.arange(-25, 25, 5))
    #plt.yticks(np.arange(-25, 25, 5))
    plt.colorbar()
    pdffile = name+'.pdf'
    plt.savefig(pdffile, bbox_inches='tight')
    plt.show()

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
