import numpy as np
import matplotlib.pyplot as plt
#The data in the next three lines was aquired
#by running "python3 images_kicker.py"
#This script is in the same folder, and can be found on the repo
voltage = np.array((18.0, 20.0,22.0, 24.0, 26.0))
xoffset = np.array((16.08281818, 18.39087455, 21.31531992, 23.58201852, 25.49657292))
deviations = np.array((0.71676416,  0.66506895, 0.74493582, 0.91352114, 0.49975501))
#Calculating angles
#angles  = np.arcsin(np.abs(xoffset/1000))
#angles_deg = (180.0/np.pi)*angles

#predicted angles:
L = 1.0 #m
h = 0.05 #m
#const = L/h
#angle75 = const*((voltage*10**3.0)/(75.0*10**6))*2
#angle65 = const*((voltage*10**3.0)/(65.0*10**6))*2
#
#xoff75 = (1-np.cos(angle75))*(L/angle75)*10**3  
#xoff65 = (1-np.cos(angle65))*(L/angle65)*10**3
#
#deg75 = angle75*(180/np.pi)
#deg65 = angle65*(180/np.pi)
yagL   = 0.25
const  = L/h
e75 = np.array([75.0]) *10**6
e65 = np.array([65.0]) *10**6

deg75 = const*(2*voltage*10**3/e75)*(180/np.pi)*2
deg65 = const*(2*voltage*10**3/e65)*(180/np.pi)*2

print(const)
radtotal75 = const*(2*voltage*10**3/e75)*2
radtotal65 = const*(2*voltage*10**3/e65)*2

xoffset75 = (1-np.cos(radtotal75))*(L/radtotal75)*10**3 + yagL*np.tan(radtotal75)*10**3#L/radtotal = rho
xoffset65 = (1-np.cos(radtotal65))*(L/radtotal65)*10**3 + yagL*np.tan(radtotal65)*10**3

print(e65, deg65[1], radtotal65[1], xoffset65[1])

plt.title('Kicker Deflection, $30 \pm 0.5$ nC Beam', size=20)
plt.xlabel('Kicker Voltage [kV]', size=18)
plt.ylabel('Horizontal Deflection [mm]', size=18)
plt.errorbar(voltage, xoffset, deviations, fmt='bo', markersize=3, label='Data')
#plt.plot(voltage, line, 'k--', label='Linear Fit')
plt.plot(voltage, xoffset75, 'b.-', label='75 MeV')
plt.plot(voltage, xoffset65, 'y--', label='65 Mev')
plt.legend(loc='lower right')
plt.grid('on')
plt.savefig('kicker_deflection_comparison.pdf', dpi=1000, bbox_inches='tight')

