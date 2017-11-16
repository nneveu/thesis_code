import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os, sys, glob

design_path = "tba_DesignPath.dat"
files = glob.glob('*.dat')


keyList = []
dataList = []
x = []
z = []
with open(design_path,'r') as f:
    for line in f:
        #print(line)
        if line.startswith("#"):
            #key, comment = line.split(',')
            #keyList.append(key[1:])
            header = line
        else: # it must be data
            #print(line)
            data = line.split('\t')
            data = data[0].split(' ')
            hold = []
            for num in data: 
                try:
                    num = float(num)
                    hold.append(num)
                except:
                    count = 1
            z.append(hold[0])
            x.append(hold[1])

x = np.array(x)*1000
z = np.array(z)
#print(x)
#print(plt.style.available)
#plt.axvline(x=16.0, color='k', linestyle='--')
#plt.text(14.4, -0.25, 'End of \nEEX dipole')

plt.axvline(x=16.5, color='k', linestyle='--')
plt.text(16.4, 5, 'Entrance \nof kicker')

plt.axvline(x=17.5, color='k', linestyle='--')
#plt.text(17.9, 0.3, 'Exit \nof kicker')

plt.axvline(x=18.5, color='k', linestyle='--')
plt.text(18.4, 5, 'Entrance \n of septum')

plt.axvline(x=18.75, color='k', linestyle='--')
#plt.text(20.8, 0.8, 'Exit \n of septum')

plt.style.use('classic')
plt.grid('on')
plt.axis([19,16, -140, 80])
plt.xticks(np.arange(16.0, 20, 0.5))
plt.yticks(np.arange(-200, 100, 20))

plt.xlabel('Distance in z [m]')
plt.ylabel('Offset in x [mm]')
plt.title('Trajectory 65 MeV, total 15$^{\circ}$ bend')
plt.plot(z, x, '-', label="Ref Traj")
plt.legend(loc='lower right')
plt.savefig('test.pdf', bbox_inches='tight')

      
