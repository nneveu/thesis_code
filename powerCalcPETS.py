# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

def form_fact(freq=11.7*10.0**9, sigmaz=1.5*10.0**-3.0)
    #Calculating form factor
    #sigmaz = bunch length
    c   = 3.0*10.0**8.0 # Speed of light
    lambdaz   = c/freq #Wavelength in structure
    kz        = (2.0*np.pi)/ lambdaz #wave number in structure
    holder    = (kz*sigmaz)**2
    formfact  = np.exp(-holder/2)
    powerperc = formfact**2
    return (formfact)   


def power_calc(freq=11.7*10.0**9, Q=40, tb=769*10**-12, vg, RQ, L, Qc) 
    c       = 3.0*10.0**8.0
    I       = Q/Tb   #Beam current
    lambdaz = c/freq #Wavelength in structure
    omega   = 2.0*np.pi*f          #angular frequency in structure
    alpha = omega / (2.0*Qc*vg)  #Loss coefficent
    hold2 = (1-math.exp(-alpha*L))/ alpha
    formfactor = form_fact()
    powertrain = ( (omega*(I**2.0)*RQ)/(4.0*vg) )*(hold**2)*(formfactor**2)*0.965
    return(powertrain)


c   = 3.0*10.0**8.0 # Speed of light

Lm  = 0.3 # metallic
Ld  = 0.3 #30.0 cm long decelerating cavity
La  = 0.15#*10.0**-2.0  #3.3cm long accelerating cavity

rqm = 3920.0
rqd = 4320.0    #Shunt impeadance over Quality factor - decelerator 
rqa = 9400.0    #Shunt impeadance over Quality factor - accelerator

vgm = 0.22*c
vgd = 0.195*c      #Group velocity decelerator
vga = 0.068*c      #Group velocity accelerator

qm  = 6500
qd  = 3706


#Calculate power 
#11.7 GHz = #vg, R, L, Q
power_metallic = power_calc(vm, rqm, Lm, qm)
power_diel = power_calc(vd, rqd, Ld, qd)

print(power_metallic)
print(power_diel)

'''
WAVEGUIDE LOSS

sigmacopper = 5.8*10**7
munot = 4*np.pi*10**-7

Rs = np.sqrt( (omega*munot)/(2*sigmacopper))
'''

#==============================================================================
# 
# sigmaz   = np.arange(0.0,0.005, 0.0001)
#plt.figure(1)
#plt.title("% Power vs. Bunch Length \n for 11.7 Ghz", size=20)
#plt.xlabel('Bunch Length [mm]', size=18)
#plt.ylabel('% Power Generated', size=18)
#plt.plot(sigmaz*10**3, bunchdep*100, '-', linewidth=3) #, label = 'Form Factor Sq')
#plt.grid()
#plt.savefig('formfactorsqrd.pdf', bbox_inches='tight')
#
#plt.figure(2)
#plt.title("Form Factor vs. Bunch Length \n for 11.7 Ghz", size=20)
#plt.xlabel('Bunch Length [mm]', size=18)
#plt.ylabel('Form Factor', size=18)
#plt.plot(sigmaz*10**3, formfactor*100, '-', linewidth=3, label='Form Factor') 
#plt.grid()
#plt.savefig('formfactor_test.pdf', bbox_inches='tight')
# 
#==============================================================================







