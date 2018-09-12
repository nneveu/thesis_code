import numpy as np

#The data in the next three lines was aquired
#by running "python3 images_kicker.py"
#This script is in the same folder, and can be found on the repo
voltage = np.array((18, 20,22, 24, 26))
xoffset = np.array((16.08281818, 18.39087455, 21.31531992, 23.58201852, 25.49657292))
angles  = np.arcsin(np.abs(xoffset/1000))
angles_deg = (180.0/np.pi)*angles

#predicted angles:
const = 1.0/0.05
angle75 = const*(voltage*10**3/75)*2
angle65 = const*(voltage*10**3/65)*2

xoff75 = (1-np.cos(angle75))*(L/angle75)*10**3  
xoff65 = (1-np.cos(angle65))*(L/angle65)*10**3

deg75 = angle75*(180/np.pi)
deg65 = angle65*(180/np.pi)

plt.title('Kicker Deflection, $30 \pm 0.5$ nC Beam', size=20)
plt.xlabel('Kicker Voltage [kV]', size=18)
plt.ylabel('Horizontal Deflection [mm]', size=18)
plt.errorbar(voltage, xoffset, deviations, fmt='bo', markersize=3, label='Data')
#plt.plot(voltage, line, 'k--', label='Linear Fit')
plt.plot(voltage, xoff75)
plt.plot(voltage, xoff75)
plt.legend(loc='upper right')
plt.grid('on')
plt.savefig('kicker_linearity.pdf', dpi=1000, bbox_inches='tight')

