import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
sys.path.append('/Users/nneveu/Documents/PythonScripts')
import myplots as mplt


#matplotlib.rc('font',family='Times New Roman')
matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 

dataopal1 = mplt.load('1nCR0pt75LaserAstraM273.stat')

fig, ax1 = plt.subplots()
ax1.plot(dataopal1['z'], dataopal1['Ez'], 'k-', label='Electric field, Ez')
ax1.set_xlabel('Z [m]', size=18)
ax1.axis([0.0,0.5,-60,5.0])
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Electric Field [MV/m]', color='k', size=18)
ax1.tick_params('y', colors='k')

ax2 = ax1.twinx()
ax2.plot(dataopal1['z'], dataopal1['Bz'], 'b--', label='Magnetic field, Bz')
ax2.set_ylabel('Magnetic Field [T]', color='b', size=18)
ax2.tick_params('y', colors='b')
ax2.axis([0.0,0.5,-0.4,0.05]) 

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='lower right')


fig.tight_layout()
plt.savefig('./gun_EM_fields.pdf', format='pdf', dpi=1000, bbox_inches='tight')

plt.show()

