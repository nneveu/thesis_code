# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 17:08:59 2016

@author: nneveu
"""
import scipy.io as spio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font',family='Times New Roman')
matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 

import sys
sys.path.append('/Users/nneveu/Documents/PythonScripts')
import myplots as mplt


dataopal = mplt.load('46grid1mill.stat')
#dataopal2 = mplt.load('RFphotoinjector.stat', 57)
dataopal2 = mplt.load('optgun_273_0_0.00075.stat')
datagpt  = mplt.loadgpt('OUTAnlysGun2.mat')

#==============================================================================
# astrax = np.loadtxt('awa_gunSCon.Xemit.001', skiprows=0)
# astray = np.loadtxt('awa_gunSCon.Yemit.001', skiprows=0)
# astraz = np.loadtxt('awa_gunSCon.Zemit.001', skiprows=0)
# 
# 
# 
# # Four axes, returned as a 2-d array
# f, axarr = plt.subplots(2, 2, figsize=(7.5,6))
# f.subplots_adjust(hspace=.6)
# f.subplots_adjust(wspace=.4)
# 
# axarr[0, 0].plot(astrax[:,0], astrax[:,3], 'g-', label = 'ASTRA', markevery=5) #xrms
# axarr[0, 0].plot(datagpt['z'], datagpt['xrms']*10.0**3.0, 'k-o', label = 'GPT', markevery = 5, markersize =3)
# axarr[0, 0].plot(dataopal2['z'], dataopal2['xrms'], 'r-', label = 'OPAL 32^3 grid')
# axarr[0, 0].plot(dataopal['z'], dataopal['xrms'], '--', label = 'OPAL 46^3 grid')
# axarr[0, 0].set_title('Transverse Beam Size',fontsize=18)
# axarr[0, 0].set_xlabel('z [m]',fontsize=18)
# axarr[0, 0].set_ylabel(r'$x_{rms}$ [mm]',fontsize=20)
# axarr[0, 0].set_xticks(np.arange(0.05, 0.30, 0.1) )
# axarr[0, 0].axis([0.0,0.3,0,2.5])
# axarr[0, 0].legend(loc='best')
# 
# 
# axarr[1, 0].plot(astraz[:,0], astraz[:,3], 'g-', label = 'ASTRA', markevery=5) #zrms
# axarr[1, 0].plot(datagpt['z'], datagpt['zrms']*10.0**3.0, 'k-o', label = 'GPT', markevery = 5, markersize =3)
# axarr[1, 0].plot(dataopal2['z'], dataopal2['zrms'], 'r-', label = 'OPAL 32^3 grid')
# axarr[1, 0].plot(dataopal['z'], dataopal['zrms'], '--', label = 'OPAL 46^3 grid')
# axarr[1, 0].set_title('Bunch Length',fontsize=18)
# axarr[1, 0].set_xlabel('z [m]',fontsize=18)
# axarr[1, 0].set_ylabel('$z_{rms}$ [mm]',fontsize=20)
# axarr[1, 0].set_xticks(np.arange(0.05, 0.30, 0.1) )
# axarr[1, 0].axis([0.0,0.3,0,2.5])
# axarr[1, 0].legend(loc='lower right')
# 
# axarr[0, 1].plot(astrax[:,0], astrax[:,5], 'g-', label = 'ASTRA') #emittance
# axarr[0, 1].plot(datagpt['z'], datagpt['nemixrms']*10.0**6.0, 'k-o', label = 'GPT', markevery = 2, markersize =3)
# axarr[0, 1].plot(dataopal2['z'], dataopal2['xemit'], 'r-', label = 'OPAL 32^3 grid')
# axarr[0, 1].plot(dataopal['z'], dataopal['xemit'], '--', label = 'OPAL 46^3 grid')
# axarr[0, 1].set_title('Normalized Emittance',fontsize=18)
# axarr[0, 1].set_xlabel('z [m]',fontsize=18)
# axarr[0, 1].set_ylabel('$\epsilon_{nx}$ [$\mu$m]',fontsize=20)
# axarr[0, 1].set_xticks(np.arange(0.05, 0.30, 0.1) )
# axarr[0, 1].axis([0.0,0.3,0,120])
# axarr[0, 1].legend(loc='lower right')
# 
# axarr[1, 1].plot(astraz[:,0], astraz[:,2]+0.511, 'g-', label = 'ASTRA') #energy
# axarr[1, 1].plot(datagpt['z'], datagpt['E'], 'k-o', label = 'GPT', markevery = 5, markersize =3)
# axarr[1, 1].plot(dataopal2['z'], dataopal2['E']+0.511, 'r-', label = 'OPAL 32^3 grid')
# axarr[1, 1].plot(dataopal['z'], dataopal['E']+0.511, '--', label = 'OPAL 46^3 grid')
# axarr[1, 1].set_title('Energy ',fontsize=18)
# axarr[1, 1].set_xlabel('z [m]',fontsize=18)
# axarr[1, 1].set_ylabel('$\gamma mc^2$ [MeV]',fontsize=20)
# axarr[1, 1].set_xticks(np.arange(0.05, 0.30, 0.1) )
# axarr[1, 1].axis([0.0,0.3,0,8.0])
# axarr[1, 1].legend(loc='best')
# 
# plt.savefig('wikitestNoMinStep.pdf', format='pdf', dpi=1000, bbox_inches='tight')
# 
# #==============================================================================
# # 
# #==============================================================================
# 
# f, axarr = plt.subplots(2, 2, figsize=(7.5,6))
# f.subplots_adjust(hspace=.6)
# f.subplots_adjust(wspace=.4)
# 
# axarr[0, 0].plot(astrax[:,0], astrax[:,3], 'g-', label = 'ASTRA', markevery=5) #xrms
# axarr[0, 0].plot(datagpt['z'], datagpt['xrms']*10.0**3.0, 'k-o', label = 'GPT', markevery = 5, markersize =3)
# axarr[0, 0].plot(dataopal2['z'], dataopal2['xrms'], 'r-', label = 'OPAL 32^3 grid')
# axarr[0, 0].plot(dataopal['z'], dataopal['xrms'], '--', label = 'OPAL 46^3 grid')
# axarr[0, 0].set_title('Transverse Beam Size',fontsize=18)
# axarr[0, 0].set_xlabel('z [m]',fontsize=18)
# axarr[0, 0].set_ylabel(r'$x_{rms}$ [mm]',fontsize=20)
# axarr[0, 0].set_xticks(np.arange(0.0, 5.0, 1.0) )
# axarr[0, 0].axis([0.0,4.0,0,3.0])
# axarr[0, 0].legend(loc='best')
# 
# axarr[1, 0].plot(astraz[:,0], astraz[:,3], 'g-', label = 'ASTRA', markevery=5) #zrms
# axarr[1, 0].plot(datagpt['z'], datagpt['zrms']*10.0**3.0, 'k-o', label = 'GPT', markevery=10, markersize=3)
# axarr[1, 0].plot(dataopal2['z'], dataopal2['zrms'], 'r-', label = 'OPAL 32^3 grid')
# axarr[1, 0].plot(dataopal['z'], dataopal['zrms'], '--', label = 'OPAL 46^3 grid')
# axarr[1, 0].set_title('Bunch Length',fontsize=18)
# axarr[1, 0].set_xlabel('z [m]',fontsize=18)
# axarr[1, 0].set_ylabel('$z_{rms}$ [mm]',fontsize=20)
# axarr[1, 0].set_xticks(np.arange(0.0, 5.0, 1.0) )
# axarr[1, 0].axis([0.0,4.0,0,2.5])
# axarr[1, 0].legend(loc='best')
# 
# axarr[0, 1].plot(astrax[:,0], astrax[:,5], 'g-', label = 'ASTRA') #emittance
# axarr[0, 1].plot(datagpt['z'], datagpt['nemixrms']*10.0**6.0, 'k-o', label = 'GPT', markevery=5, markersize=3)
# axarr[0, 1].plot(dataopal2['z'], dataopal2['xemit'], 'r-', label = 'OPAL 32^3 grid')
# axarr[0, 1].plot(dataopal['z'], dataopal['xemit'], '--', label = 'OPAL 46^3 grid')
# axarr[0, 1].set_title('Normalized Emittance',fontsize=18)
# axarr[0, 1].set_xlabel('z [m]',fontsize=18)
# axarr[0, 1].set_ylabel('$\epsilon_{nx}$ [$\mu$m]',fontsize=20)
# axarr[0, 1].set_xticks(np.arange(0.0, 5.0, 1.0) )
# axarr[0, 1].set_yticks(np.arange(0.0, 14, 2.0) )
# axarr[0, 1].axis([0.0,4.0,0,14])
# axarr[0, 1].legend(loc='upper right')
# 
# axarr[1, 1].plot(astraz[:,0], astraz[:,2]+0.511, 'g-', label = 'ASTRA') #energy
# axarr[1, 1].plot(datagpt['z'], datagpt['E'], 'k-o', label = 'GPT', markevery=10, markersize=3)
# axarr[1, 1].plot(dataopal2['z'], dataopal2['E']+0.511, 'r-', label = 'OPAL 32^3 grid')
# axarr[1, 1].plot(dataopal['z'], dataopal['E']+0.511, '--', label = 'OPAL 46^3 grid')
# axarr[1, 1].set_title('Energy ',fontsize=18)
# axarr[1, 1].set_xlabel('z [m]',fontsize=18)
# axarr[1, 1].set_ylabel('$\gamma mc^2$ [MeV]',fontsize=20)
# axarr[1, 1].set_xticks(np.arange(0.0, 5.0, 1.0) )
# axarr[1, 1].axis([0.0,4.0,0,8.0])
# axarr[1, 1].legend(loc='lower right')
# 
# plt.savefig('wikitest5mNoMinStep.pdf', format='pdf', dpi=1000, bbox_inches='tight')
# 
# # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
# #plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
# #plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
# 
#==============================================================================
