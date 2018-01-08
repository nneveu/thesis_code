# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import math
#import matplotlib
#import matplotlib.pyplot as plt

'''
x = np.array([1,100])
y = np.array([1.5,8])
plt.plot(x,y)
plt.savefig('test.pdf')


print(np.sqrt(40))
'''
c   = 3.0*10.0**8.0
Ld  = 0.3 #30.0 cm long decelerating cavity
La  = 0.15#*10.0**-2.0  #3.3cm long accelerating cavity

rqd = 4300.0    #Shunt impeadance over Quality factor - decelerator 
rqa = 9400.0    #Shunt impeadance over Quality factor - accelerator

Q   = 18.75*10.0**-9.0   #charge in each bunch [nC]
Tb  = 0.769*10.0**-9.0    #Time between bunches [nS]
I   = Q/Tb  #Beam current

vgd = 0.195*c        #Group velocity decelerator
vga = 0.068*c      #Group velocity accelerator


f        = 11.7*10.0**9.0       #Fundamental mode frequency in structure
omega    = 2.0*np.pi*f          #angular frequency in structure
lambdaz  = c/f                  #Wavelength in structure
kz       = (2.0*np.pi)/ lambdaz #wave number in structure
qualityd = 3706.0


sigmaz   = 1.5*10.0**-3.0       #rms bunch length
hold     = -(kz*sigmaz)**2.0 

formfactor  = math.exp(hold/2)      #form factor for Guassian bunch length

alpha = omega / (2.0*qualityd*vgd)  #Loss coefficent

hold2 = (1-math.exp(-alpha*Ld))/ alpha

powertrain = ( (omega*(I**2.0)*rqd)/(4.0*vgd) )*(hold2**2)*(formfactor**2)*0.965

electricField = np.sqrt( (rqa*powertrain*omega)/vga)

gradient = electricField #in MV/m

denergy = gradient*2*La #in MeV


'''
WAVEGUIDE LOSS

sigmacopper = 5.8*10**7
munot = 4*np.pi*10**-7

Rs = np.sqrt( (omega*munot)/(2*sigmacopper))
'''

#==============================================================================
# lam = 299792458 / 26e9
# kz = (2*np.pi)/lam
# 
# sigmaz = np.arange(0.0,0.0031, 0.0001)
# 
# holder = (kz*sigmaz)**2
# 
# formfact = np.exp(-holder/2)
# 
# bunchdep = formfact**2
# 
# plt.figure()
# plt.title("% Power vs. Bunch Length \n for 26 Ghz", size=20)
# plt.xlabel('Bunch Length [mm]', size=18)
# plt.ylabel('% Power Generated', size=18)
# plt.plot(sigmaz*10**3, bunchdep*100, '-', linewidth=3) #, label = 'Form Factor Sq')
# plt.legend()
# plt.grid()
# plt.savefig('formfactorsqrd.pdf', bbox_inches='tight')
# 
# plt.figure()
# plt.title("Form Factor vs. Bunch Length \n for 26 Ghz", size=20)
# plt.xlabel('Bunch Length [mm]', size=18)
# plt.ylabel('Form Factor', size=18)
# plt.plot(sigmaz*10**3, formfact*100, '-', linewidth=3, label='Form Factor') 
# plt.grid()
# plt.savefig('formfactor.pdf', bbox_inches='tight')
# 
#==============================================================================







