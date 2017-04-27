# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:16:13 2016

@author: nneveu
"""
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append('/Users/nneveu/Documents/PythonScripts')
import myplots as mplt

run = 'check2mAfterKicker'

#myfile1 = 'dipoleKickerM260.stat'
#myfile2 = 'dipoleKickerM255.stat'
#myfile = 'kickerScanQstrength1pt8.stat'
#myfile2 = 'kickerScanQ1Q2-1pt98.stat'
#statdata = mplt.load(myfile2,59)

#opalfilebase = 'dipoleKickerBaselineK0-0pt012'

angledata = mplt.load('dipoleKicker20m.stat')
#k0data  = mplt.load('dipoleKickerBaselineK0-0pt012.stat', 56)
#k08psdata = mplt.load('dipoleKicker-10%E.stat', 56)


for i in np.arange(2, 3, 1): 
    
    if i ==1: 
        #Energy Plot
        plt.figure(1)
        plt.show(block=False) 
        plt.axis((0, 20, 0, 70))
        plt.title( r'Energy Vs. Z' , size=18)
        plt.xlabel(r'z [m]', size=18)
        plt.ylabel(r'$\gamma mc^2$ [MeV]', size=18)
        plt.plot(angledata['z'], angledata['E'], 'b-', label = 'Baseline')
        #plt.plot(k08psdata['z'], k08psdata['E'],  'g-', label='-10\% Energy')#,markersize=4, markevery=50)        
        #plt.plot(k08psdata['z'], k08psdata['E'],  'g-', label='8ps: K0 = -0.12196 [T]',markersize=4, markevery=50)
        plottitle = 'Energy' +run +'.pdf'
        
    
    elif i ==2:
        #XRMS Plot
        plt.figure(2)
        plt.show(block=False) 
        plt.axis((0, 20, 0, 35))
        plt.title( r'Beam Size Vs. Z' , size=18)
        plt.xlabel(r'z [m]', size=18)
        plt.ylabel(r'$3\sigma$ [mm]', size=18)
        plt.plot(angledata['z'], 3*angledata['xrms'], 'b-', label = '3$\sigma_{x/y}$ Baseline')
        #plt.plot(k08psdata['z'], 3*k08psdata['xrms'],  'g-', label='3$\sigma_{x/y}$ -10\%E',markersize=4, markevery=50)
        plt.plot(angledata['z'], 3*angledata['yrms'], 'b--')#, label = '3$\sigma_y$')
        #plt.plot(k08psdata['z'], 3*k08psdata['yrms'],  'g--')#, label='3$\sigma_y$',markersize=4, markevery=50)
#==============================================================================
#         plt.plot(dataoff['z'], dataoff['xrms'], 'b-', label = 'M260')
#         plt.plot(dataon['z'], dataon['xrms'],  'g-', label='M265')
#==============================================================================
        plottitle = 'XRMS3sigma' +run +'.pdf'
    
    elif i ==3:
        #XEMIT Plot
        plt.figure(3)
        plt.show(block=False)
        plt.axis((0.0, 20.0, 50.0, 350)) 
        plt.title( r'Emittance Vs. Z' , size=18) 
        plt.xlabel(r'z [m]', size=18) 
        plt.ylabel(r'$\epsilon_{nx}$ [mm-mrad]', size=18)
        plt.plot(angledata['z'], angledata['xemit'], 'b-', label = '2.0ps: 2deg Angle')
        #plt.plot(k08psdata['z'], k08psdata['xemit'],  'g-', label='8.09ps: K0 = -0.12196 [T]',markersize=4, markevery=50)
#==============================================================================
#         plt.plot(dataoff['z'], dataoff['xemit'], 'b-', label = 'M260')
#         plt.plot(dataon['z'], dataon['xemit'],  'g-', label='M265')
#==============================================================================
        plottitle = 'Emittance'+run+'.pdf'
        
    elif i ==4:
        #XEMIT Plot
        plt.figure(3)
        plt.show(block=False)
        plt.axis((0.0, 20.0, 0, 3)) 
        plt.title( r'Bunch Length' , size=18) 
        plt.xlabel(r'z [m]', size=18) 
        plt.ylabel(r'$\sigma_{z}$ [mm]', size=18)
        plt.plot(angledata['z'], angledata['zrms'], 'b-', label = '2.0ps: 2deg Angle')
        #plt.plot(k08psdata['z'], k08psdata['zrms'],  'g-', label='8.09ps: K0 = -0.12196 [T]',markersize=4, markevery=50)
#==============================================================================
#         plt.plot(dataoff['z'], dataoff['xemit'], 'b-', label = 'M260')
#         plt.plot(dataon['z'], dataon['xemit'],  'g-', label='M265')
#==============================================================================
        plottitle = 'BunchLength'+run+'.pdf'
#==============================================================================
#     for j in np.arange(2, 2, 1): 
#     
#         #s = str(j)
#         #s = s.replace(".", "pt")
#         #myopalfile = opalfilebase + '.stat'
#         #myopalfile = opalfilebase + s + '.stat'
#         #data = mplt.load(myopalfile, 56)
#     
#         if i ==1: 
#             #Energy Plots
#             plt.plot(data['z'], data['E'],  '-')#, label=s,markersize=4, markevery=50)
#             plt.legend(loc=4)  
#             
#         elif i ==2:   
#             #XRMS Plots
#             plt.plot(data['z'], 3*data['xrms'], label= '$\sigma_x$') 
#             plt.plot(data['z'], 3*data['yrms'], label= '$\sigma_y$')#, Q2 = '+str(j)) 
#             #plt.plot((11.0, 16.0), (25, 25), 'k--', label='25mm = Drift Radius')
#             plt.plot((15.3, 15.3), (0.0, 15.0), 'k-')
#             plt.plot((16.0, 16.0), (0.0, 15.0), 'k-')
#             plt.plot((15.3, 16.0), (15.0, 15.0), 'k-', label=r'Kicker')
#             plt.legend(loc='best')
#             
#         elif i ==3: 
#             #XEMIT Plots
#             plt.plot(data['z'],data['xemit'])#, label=s)
#             plt.legend(loc='best') 
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







