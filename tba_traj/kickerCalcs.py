# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:43:13 2016

Kicker field calculations

@author: nneveu
"""
import numpy as np
import matplotlib.pyplot as plt

V = 50*10.0**3.0  # Kicker voltage in Volts
Vp = V/2
R = 50.0          # Resistance in ohms
I = V/R           # Current in Amps

h = np.array([0.04])#, 0.035, 0.03, 0.025])
#h = np.array([0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05])          # Distance between plates in Meters
w = (377.0/50.0)*h  # Width of kicker in Meters 
L = 1.0          # Length of kicker in Meters

munot = 4*np.pi*10**-7

p = 50.0*10.0**6.0    #Kinetic energy in GeV 
c = 2.99*10.0**8.0 # speed of light

Brho = 3.33564*(p/(10**9))

"""
B field from Current
"""
#Bi = munot*(I/w)

"""
B and E field from Voltage
"""
Ev = V/h
Bv = Ev / c 


"""
Kick from Ev
"""
thetaErad = (V*L)/(h*p)
thetaEdeg = thetaErad*(180/np.pi)


"""
Kick from Bv and Bi
"""
thetaBrad = (Bv*L)/(Brho)
thetaBdeg = thetaBrad*(180/np.pi)

totalkickdeg = thetaEdeg*2
totalkickrad = thetaErad*2

totalkickdeg2 = thetaBdeg+thetaEdeg

rho = (p/(3*10**8))/(Bv +Ev/c)
rho2 = L/totalkickrad
xoffset2 =(1-np.cos(totalkickrad))*rho2*10**3
xoffset =(1-np.cos(totalkickrad))*rho*10**3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
const    = L/h
energies = np.array([45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0]) *10**6

v20 = const*(40.0*10**3/energies)*(180/np.pi)*2
v25 = const*(50.0*10**3/energies)*(180/np.pi)*2
v23 = const*(46.0*10**3/energies)*(180/np.pi)*2
v30 = const*(60.0*10**3/energies)*(180/np.pi)*2

radtotal20 = const*(40.0*10**3/energies)*2
radtotal25 = const*(50.0*10**3/energies)*2
radtotal30 = const*(60.0*10**3/energies)*2

xoffset20 = (1-np.cos(radtotal20))*(L/radtotal20)*10**3 #L/radtotal = rho
xoffset25 = (1-np.cos(radtotal25))*(L/radtotal25)*10**3
xoffset30 = (1-np.cos(radtotal30))*(L/radtotal30)*10**3


#Calculating Z drift needed for 7-10 mm
z20 = (30-xoffset20)/np.tan(radtotal20)*10**-3
z25 = (30-xoffset25)/np.tan(radtotal25)*10**-3
z30 = (30-xoffset30)/np.tan(radtotal30)*10**-3


eplot = np.array([45, 50, 55, 60, 65, 70, 75, 80]) 

plt.figure()
plt.grid('on')
plt.title('Angle Given by Kicker \n vs. Beam Energy', size = 20)
plt.ylabel('Kicker Angle [Degrees]', size=18)
plt.xlabel('Beam Energy [MeV]', size=18)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.plot(eplot, v30, '-o', label = '30 kV')
plt.plot(eplot, v25, '-o', label = '25 kV')
plt.plot(eplot, v23, '-o', label = '23 kV')
plt.plot(eplot, v20, '-o', label = '20 kV')
plt.plot((45.0, 80.0), (2.0, 2.0), 'k-')
plt.legend(loc='lower left')
plt.axis((45, 80, 0.0, 4.5))
plt.savefig('AngleVsEnergy.pdf', bbox_inches='tight')

plt.figure()
plt.title('X Offset Given by Kicker \n vs. Beam Energy', size = 20)
plt.ylabel('X Offset [mm]', size=18)
plt.xlabel('Beam Energy [MeV]', size=18)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.plot((45.0, 80.0), (20, 20), 'k-')
plt.plot(eplot, xoffset30, '-o', label = '30 kV')
plt.plot(eplot, xoffset25, '-o', label = '25 kV')
plt.plot(eplot, xoffset20, '-o', label = '20 kV')
plt.legend(loc='lower left')
plt.axis((45, 80, 0.0, 45))
plt.savefig('XoffsetVsEnergy.pdf', bbox_inches='tight')


plt.figure()
plt.title('Drift Distances Needed After Kicker \n vs. Beam Energy', size = 20)
plt.ylabel('Z [m]', size=18)
plt.xlabel('Beam Energy [MeV]', size=18)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.plot((45.0, 80.0), (20, 20), 'k-')
plt.plot(eplot, z30, '-o', label = '30 kV')
plt.plot(eplot, z25, '-o', label = '25 kV')
plt.plot(eplot, z20, '-o', label = '20 kV')
plt.legend(loc='upper left')
plt.axis((50, 80, 0.0, 1.0))
plt.savefig('zdrift.pdf', bbox_inches='tight')





