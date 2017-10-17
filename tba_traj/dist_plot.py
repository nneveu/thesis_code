import numpy as np
import matplotlib.pyplot as plt

#_________________plot distribution_______________
dist_file = 'distribution.data'
dist = np.loadtxt(dist_file, skiprows=1)

#0-x
#1-px
#2-y
#3-py
#4-t
#5-pz
x = dist[:,0]*10**3
y = dist[:,2]*10**3 
t = dist[:,4]*10**3

plt.figure(1)
plt.hist2d(x, y, bins = 200, range=[[-10.0,10.0], [-10.0,10.0]], cmin=1)
#plt.plot(dist[:,0], dist[:,2], markersize=0.5)
plt.title('Initial Distribution')
plt.ylabel('Y [mm]')
plt.xlabel('X [mm]')
plt.savefig('mydist_xy.pdf')


plt.figure(2)
plt.hist2d(t, y, bins = 200, range=[[0.0,0.8], [-10.0,10.0]], cmin=1)
#plt.plot(dist[:,0], dist[:,2], markersize=0.5)
plt.title('Initial Distribution')
plt.ylabel('Y [mm]')
plt.xlabel('T [ms]')
plt.savefig('mydist_yt.pdf')

plt.figure(3)
plt.hist2d(t, x, bins = 200, range=[[0.0,0.8], [-10.0,10.0]], cmin=1)
#plt.plot(dist[:,0], dist[:,2], markersize=0.5)
plt.title('Initial Distribution')
plt.ylabel('X [mm]')
plt.xlabel('T [ms]')
plt.savefig('mydist_xt.pdf')


