import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)      
plt.rc('font', family='serif') 


import sys
sys.path.append('/Users/nneveu/Documents/PythonScripts')
import myplots as mplt 

times   = np.loadtxt('timings.txt', skiprows=1)
tstep   = times[:,0]
seconds = times[:,1]

plt.title('Timing results')
plt.xlabel('time step [s]')
plt.ylabel('simulation time [s]')
plt.plot(tstep, seconds, '*--')
plt.savefig('./time_vs_timestep.pdf', format='pdf', dpi=1000, bbox_inches='tight')

#data1 = mplt.load('5e-10.stat')
#data2 = mplt.load('1e-10.stat')
data3 = mplt.load('5e-11.stat')
#data4 = mplt.load('1e-11.stat')
#data5 = mplt.load('5e-12.stat')
#data6 = mplt.load('1e-12.stat')

datah = mplt.load('1e5_np.stat')
datan = mplt.load('optLinac_40nC.stat')

#data = [data1, data2, data3, data4, data5, data6, datan]
#v = [str(5e-10), str(1e-10), str(5e-11), str(1e-11), str(5e-12), str(1e-12), 'multi-steps  np=1e5']

data = [data3, datan, datah]
v = ['low fidelity', 'low fidelity adjusted dT', 'mid fidelity']

markers = ['b--', 'k-', 'y--', 'r-', 'k--', 'm-', '--']

f, axarr = plt.subplots(2, 2) #, figsize=(15,8))
#f.subplots_adjust(hspace=.6)
#f.subplots_adjust(wspace=.4)

axarr[0, 0].set_title('Transverse Beam Size',fontsize=14)
axarr[0, 0].set_xlabel('z [m]',fontsize=14)
axarr[0, 0].set_ylabel(r'rms$_x$ (mm)',fontsize=14)
axarr[0, 0].set_xticks(np.arange(0.0, 20.0, 2.0) )
axarr[0, 0].axis([0.0,19.0,0,10.0])

axarr[1, 0].set_title('Bunch Length',fontsize=14)
axarr[1, 0].set_xlabel('s (m)',fontsize=14)
axarr[1, 0].set_ylabel('rms$_s$ (mm)',fontsize=14)
axarr[1, 0].set_xticks(np.arange(0.0, 20.0, 2.0) )
axarr[1, 0].axis([0,19.0,0.5,1.75])

axarr[0, 1].set_title('Normalized Emittance',fontsize=14)
axarr[0, 1].set_xlabel('s (m)',fontsize=14)
axarr[0, 1].set_ylabel('$\epsilon_{x}$ (mm mrad)',fontsize=14)
axarr[0, 1].set_xticks(np.arange(0.0, 20.0, 2.0) )
axarr[0, 1].set_yticks(np.arange(0.0, 400, 50.0) )
axarr[0, 1].axis([0.0,19.0,50,300])

axarr[1, 1].set_title('Energy ',fontsize=14)
axarr[1, 1].set_xlabel('s (m)',fontsize=14)
axarr[1, 1].set_ylabel('$\gamma mc^2$ (MeV)',fontsize=14)
axarr[1, 1].set_xticks(np.arange(0.0, 20.0, 2.0) )
axarr[1, 1].axis([0.0,19.0,0,70.0])

for i in range(0,len(v)):
    data_n = data[i]
    axarr[0, 0].plot(data_n['z'], data_n['xrms'], markers[i], label = 'dT='+v[i], markevery=200, markersize=4, markerfacecolor='None')
    axarr[1, 0].plot(data_n['z'], data_n['zrms'], markers[i], label = 'dT='+v[i], markevery=200, markersize=4, markerfacecolor='None')
    axarr[0, 1].plot(data_n['z'], data_n['xemit'], markers[i], label = 'dT='+v[i], markevery=200, markersize=4, markerfacecolor='None')
    axarr[1, 1].plot(data_n['z'], data_n['E']+0.511, markers[i], label = 'dT='+v[i], markevery=200, markersize=4, markerfacecolor='None')

#axarr[0, 0].legend(bbox_to_anchor=(1.04,1)) #loc='best')
#axarr[1, 0].legend(bbox_to_anchor=(1.04,1))
axarr[0, 1].legend(bbox_to_anchor=(0.35,-1.75))#loc='upper left')
#axarr[1, 1].legend(bbox_to_anchor=(1.04,1))#loc='best')

f.tight_layout()
plt.savefig('./timestep_comparison_paper.pdf', format='pdf', dpi=1000, bbox_inches='tight')
