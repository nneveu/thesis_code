import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os, sys

#sys.path.append("/home/neveu/Document/opal_stuff/pyOPALTools")
#from utils import tableau20
#from utils import SddsReader

def orbit_files(origfile, centerfile, offaxisfile):
    f1 = open(origfile, 'r')
    f2 = open(centerfile, 'w')
    f3 = open(offaxisfile, 'w')

    for line in f1: 
        start = line.split(' ')[0]
        if start == "ID1":
            f2.write("\t".join(line.split()[1:]) + "\n") 
        elif start == 'ID2':
            f3.write("\t".join(line.split()[1:]) + "\n")
        elif start == '#': 
            f2.write(line)
            f3.write(line)

    f1.close()
    f2.close()
    f3.close()


data = 'tba-trackOrbit_65MeV.dat'
center = 'tba_center_orbit_65MeV.dat'
offaxis = 'tba_offaxis_orbit_65MeV.dat'

orbit_files(data, center, offaxis)
data1 = np.loadtxt(center, skiprows=2)
data2 = np.loadtxt(offaxis, skiprows=2)

centerz = data1[:,0]
offaxisz= data2[:,0]

centerx = data1[:,1]*39.3701
offaxisx = data2[:,1]*39.3701

#print(plt.style.available)
plt.axvline(x=14.5, color='k', linestyle='--')
plt.text(14.4, -0.25, 'End of \nEEX dipole')

plt.axvline(x=17.0, color='k', linestyle='--') 
plt.text(16.9, -0.25, 'Entrance \nof kicker')  

plt.axvline(x=18.0, color='k', linestyle='--')
plt.text(17.9, 0.3, 'Exit \nof kicker') 

plt.axvline(x=19.55, color='k', linestyle='--') 
plt.text(19.45, -0.2, 'Entrance \n of septum')  

plt.axvline(x=19.8, color='k', linestyle='--')
plt.text(20.8, 0.8, 'Exit \n of septum')

plt.style.use('classic')
plt.grid('on')
plt.axis([21.0, 14.0,1.5,-1])
plt.xticks(np.arange(14.0, 22, 1.0))
#plt.yticks(np.arange(, max(x)+1, 1.0))

plt.xlabel('Distance in z [m]')
plt.ylabel('Offset in x [inches]')
plt.title('Trajectory 68 MeV, total 15$^{\circ}$ bend')
plt.plot(centerz, centerx, '-', label="Center Particle")
plt.plot(offaxisz, offaxisx, 'g-', label="Off Center Particle")
plt.legend(loc='lower right')
plt.savefig('test.pdf', bbox_inches='tight')
