# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:16:13 2016

@author: nneveu
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

import myplots as mplt

run = 'dipole_test'

#opalfilebase = 'dipoleKickerBaselineK0-0pt012'
#file1 = mplt.load('optLinac_weight3.stat')
#file1 = mplt.load('optLinac_weight5_linacon.stat')
#file2 = mplt.load('optLinac_weight5_linacon.stat')

file1 = mplt.load('./data/optLinac3Dgun3DLinac.stat')
file2 = mplt.load('./data/optLinac3Dgun3DLinac.stat')

file1_label = 'weight 3'#'Linac on'#
file2_label = 'weight 5'#'weight 5'


for i in np.arange(6, 8, 1): 
    
    if i ==1: 
        #Energy Plot
        plt.figure(1)
        #plt.show(block=False) 
        #plt.axis((0, 20, 0, 70))
        plt.title( r'Energy Vs. Z' , size=18)
        plt.xlabel(r'z [m]', size=18)
        plt.ylabel(r'$\gamma mc^2$ [MeV]', size=18)
        plt.plot(file1['z'], file1['E'], 'b-', label = file1_label)
        plt.yticks(np.arange(0, 70, 5.0))
        plt.grid('on')
        plt.plot(file2['z'], file2['E'], 'g--', label = file2_label)
        plottitle = 'Energy_' +run +'.pdf'
        
    
    elif i ==2:
        #XRMS Plot
        plt.figure(2)
        #plt.show(block=False) 
        #plt.axis((0, 20, 0, 45))
        plt.title( r'Beam Size Vs. Z' , size=18)
        plt.xlabel(r'z [m]', size=18)
        plt.ylabel(r'$3\sigma$ [mm]', size=18)
        plt.plot(file1['z'], 3*file1['xrms'], 'b-',  label = file1_label + '- 3$\sigma_{x}$ ')
        plt.plot(file1['z'], 3*file1['yrms'], 'b--', label = file1_label + '- 3$\sigma_y$')
        plt.plot(file2['z'], 3*file2['xrms'], 'g-',  label = file2_label + '- 3$\sigma_{x}$ ')
        plt.plot(file2['z'], 3*file2['yrms'], 'g--', label = file2_label + '- 3$\sigma_y$')

#==============================================================================
#         plt.plot(dataoff['z'], dataoff['xrms'], 'b-', label = 'M260')
#         plt.plot(dataon['z'], dataon['xrms'],  'g-', label='M265')
#==============================================================================
        plottitle = 'XRMS3sigma_' +run +'.pdf'
    
    elif i ==3:
        #XEMIT Plot
        plt.figure(3)
        #plt.show(block=False)
        #plt.axis((0.0, 20.0, 0.0, 150)) 
        plt.title( r'Emittance Vs. Z' , size=18) 
        plt.xlabel(r'z [m]', size=18) 
        plt.ylabel(r'$\epsilon_{nx}$ [mm-mrad]', size=18)
        plt.plot(file1['z'], file1['xemit'], 'b-', label = file1_label)
        #plt.plot(file2['z'], file2['xemit'], 'g-', label = file2_label)

#==============================================================================
#         plt.plot(dataoff['z'], dataoff['xemit'], 'b-', label = 'M260')
#         plt.plot(dataon['z'], dataon['xemit'],  'g-', label='M265')
#==============================================================================
        plottitle = 'Emittance_'+run+'.pdf'
        
    elif i ==4:
        #Bunch Length Plot
        plt.figure(4)
        #plt.show(block=False)
        #plt.axis((0.0, 20.0, 0, 3)) 
        plt.title( r'Bunch Length' , size=18) 
        plt.xlabel(r'z [m]', size=18) 
        plt.ylabel(r'$\sigma_{z}$ [mm]', size=18)
        plt.plot(file1['z'], file1['zrms'], 'b-', label = file1_label)
        plt.plot(file2['z'], file2['zrms'], 'g-', label = file2_label)
#==============================================================================
#         plt.plot(dataoff['z'], dataoff['xemit'], 'b-', label = 'M260')
#         plt.plot(dataon['z'], dataon['xemit'],  'g-', label='M265')
#==============================================================================
        plottitle = 'BunchLength_'+run+'.pdf'
        

    elif i ==5:
        #Energy Spread
        plt.figure(5)
        #plt.show(block=False)
        #plt.axis((0.0, 20.0, 0, 0.06)) 
        plt.title( r'Energy Spread' , size=18) 
        plt.xlabel(r'z [m]', size=18) 
        plt.ylabel(r'dE/E [mm]', size=18)
        plt.plot(file1['z'], file1['dE']/file1['E'], 'b-', label = file1_label)
        plt.plot(file2['z'], file2['dE']/file2['E'], 'g-', label = file2_label)

        plottitle = 'energySpread_'+run+'.pdf'
        
    elif i ==6: 
	#Bz on axis 
        plt.figure(6)
        #plt.show(block=False)
        #plt.axis((0.0, 15.0, -70,10)) 
        plt.title( r'Magnetic Field' , size=18)
        plt.xlabel(r'z [m]', size=18)
        plt.ylabel(r'Bz [T]', size=18)
        #plt.yticks(np.arange( -70,0, 5.0))
        plt.grid('on')

        plt.plot(file1['z'], file1['Bz'], 'b-', label = file1_label)
        #plt.plot(file2['z'], file2['zrms'], 'g-', label = file2_label)
        plottitle = 'Bz_'+run+'.pdf'

    elif i ==7:
        #By on axis 
        plt.figure(7)
        #plt.show(block=False)
        #plt.axis((0.0, 15.0, -70,10)) 
        plt.title( r'Magnetic Field' , size=18)
        plt.xlabel(r'z [m]', size=18)
        plt.ylabel(r'By [T]', size=18)
        #plt.yticks(np.arange( -70,0, 5.0))
        plt.grid('on')

        plt.plot(file1['z'], file1['By'], 'b-', label = file1_label)
        #plt.plot(file2['z'], file2['zrms'], 'g-', label = file2_label)
        plottitle = 'By_'+run+'.pdf'
    
    elif i ==8:
        #Ez on axis
        plt.figure(8)
        #plt.show(block=False)
        #plt.axis((0.0, 15.0, -70,10)) 
        plt.title( r'Electric Field' , size=18) 
        plt.xlabel(r'z [m]', size=18) 
        plt.ylabel(r'MV/m', size=18)
        plt.yticks(np.arange( -70,0, 5.0))        
        plt.grid('on')
        
        plt.plot(file1['z'], file1['Ez'], 'b-', label = file1_label)
        #plt.plot(file2['z'], file2['zrms'], 'g-', label = file2_label)
        plottitle = 'Ez_'+run+'.pdf'
#==============================================================================
#     for j in np.arange(2, 2, 1): 
#     
#         #s = str(j)
#         #s = s.replace(".", "pt")
#         #myopalfile = opalfilebase + '.stat'
#         #myopalfile = opalfilebase + s + '.stat'
#         #data = mplt.load(myopalfile, 56)
#     
#==============================================================================
    
    plt.legend(loc='best')
    plt.savefig(plottitle, bbox_inches='tight')

#==============================================================================
# plt.plot((0.5, 11.0), (50, 50), 'k--', label='50mm = Linac Radius')
# plt.plot((11.0, 11.0), (25, 50), 'k--')
# plt.plot((11.0, 16.0), (25, 25), 'k--', label='25mm = Drift Radius')
# #plt.plot((16.0, 30.0), (7.5, 7.5), 'k--', label=r'7.5mm = PETS Radius')
# plt.plot((16.0, 16.0), (15.0, 25), 'b--', label='Kicker Entrance')
# plt.plot((16.0, 23.5), (15.0, 15.0), 'k--', label=r'15mm = $\frac{1}{2}$ Kicker Gap')
# plt.plot((23.5, 23.5), (0, 15.0), 'r--', label='7.5m Drift')
# #plt.plot((16.0, 16.6), (13.0, 13.0), 'k--', label=r'60cm = Kicker Length')
# #ax.fill_between(xrms, .4, .10, facecolor='blue', alpha=0.5)
#==============================================================================


#==============================================================================
# Loops and user defined plotting
# #for i in np.arange(1.1, 1.35, 0.05):
# for i in np.arange(1.98, 1.985, 0.01): 
# 
#     #Calculating solenoid strength in current
#     #Mn = 440*(i/1.973966)
#     #Mn = 440*(i/0.625521474)
#     #M = '%.0f' % Mn
#     """
#     #Note, the 1.f gives one decimal place of i
#     num = str(i).replace('.', 'pt')
#     if len(num)==4:   
#         q = num        
#     elif len(num)<6:
#         q = num
#     else: 
#         q = num
#     """
#     data = mplt.load(myfile, 61)
#         
#     mplt.xemit(data,myfile)
#     mplt.yemit(data, myfile)
#     mplt.energy(data, myfile)
#     mplt.xmean(data, myfile)
#     mplt.xrms(data,myfile)
#     mplt.ymean(data, myfile)
#     mplt.by(data,myfile)
#     mplt.bz(data, myfile)
#     mplt.bx(data, myfile)
#==============================================================================







