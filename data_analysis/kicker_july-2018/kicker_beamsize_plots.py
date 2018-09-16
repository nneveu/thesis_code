import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from glob import glob
#from natsort import natsorted, ns
import sys
sys.path.append('/home/nicole/Documents/thesis_code')
import myplots as mplt
from opal.visualization.plots import *
from opal.opal import load_dataset
import itertools

matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 

files = glob('../../../awa-tba/run_opt_params/experiment_comparison_30nC/3D/*.stat') #'optLinac-40nC_KQ3=3.2_IM=250.stat']
numfiles = len(files)
data_x = np.zeros((numfiles))
data_y = np.zeros((numfiles))
sangle = np.zeros((numfiles))
print(files)
for i, myfile in enumerate(files):
    try:
        dsets = load_dataset('./', fname=myfile)#fname='optLinac-40nC.stat')            
        ds = dsets[0]
    except Exception as e:
        print ( e )

    statangle = myfile.split('=')[1]
    sangle[i] = float(statangle.split('.stat')[0])

    s = ds.getData('s')
    ind = np.where(s>17.8)[0][0]
    print(s[ind])
    xrms = ds.getData('rms_x')
    yrms = ds.getData('rms_y')

    data_x[i] = xrms[ind]
    data_y[i] = yrms[ind]

print(sangle)
#Data
high_charge = np.loadtxt('beamsizes_kickerscan_high_charge_07-2018.txt', skiprows=1)

kval_high_data = high_charge[:,1]
sigx_high_data = high_charge[:,2]
sigy_high_data = high_charge[:,3]
sigx_std_data = high_charge[:,4]
sigy_std_data = high_charge[:,5]

voltage = np.array((0, 18.0, 20.0,22.0, 24.0, 26.0))
#All possible voltages for pulsar
xoffset = np.array((0, 16.08281818, 18.39087455, 21.31531992, 23.58201852, 25.49657292))
deviations = np.array((0, 0.71676416,  0.66506895, 0.74493582, 0.91352114, 0.49975501))
#Calculating angles
data_angles  = np.arcsin(np.abs(xoffset/1000))
data_angles_deg = (180.0/np.pi)*data_angles
angle_deviations = (180.0/np.pi)*(np.arcsin(np.abs(deviations/1000)))
print(np.shape(data_angles_deg))

##Simulations
#major_ticks = np.arange(0, 20, 5)                                              
#minor_ticks = np.arange(0, 101, 5)  

p = sangle.argsort()
sangle = sangle[p]
data_x = data_x[p]
data_y = data_y[p]

print(data_x, data_y, sangle)

plt.figure(1)
plt.title('$30 \pm 0.5$nC Beam Size: $\sigma_{x,y}$', size=20)
plt.xlabel('Kicker Angle [deg]', size=20)
plt.ylabel('$\sigma_{x,y}$ [mm]', size=20)
plt.plot(sangle, data_x*10**3 , 'k--', label = 'Simulation 3D $\sigma_x$', alpha=0.6)
plt.plot(sangle, data_y*10**3, 'b--', label = 'Simulation 3D $\sigma_y$', alpha=0.6) 
#Note y and x are flipped because of camera orientation
plt.errorbar(data_angles_deg, sigy_high_data, sigy_std_data, fmt='ko--', markersize=3, label='Data $\sigma_x$')
plt.errorbar(data_angles_deg, sigx_high_data, sigx_std_data, fmt='bo', markersize=3, label='Data $\sigma_y$')
plt.legend(loc='upper right', prop={'size': 16}, bbox_to_anchor=(1.6, 1))
#plt.axis([190,260, 0, 5])
plt.minorticks_on()
plt.grid(True)#, which='both', color = '0.75', linestyle='--')
plt.savefig('xybeamsizes_high_charge_kicker_scan_angle.pdf', dpi=1000, bbox_inches='tight')

plt.figure(2)
plt.title('$30 \pm 0.5$nC Beam Size: $\sigma_{x,y}$', size=20)
plt.xlabel('Kicker Strength [Amps]', size=20)
plt.ylabel('$\sigma_{x,y}$ [mm]', size=20)
plt.errorbar(kval_high_data, sigy_high_data, sigy_std_data, fmt='ko--', markersize=3, label='Data $\sigma_y$')
plt.errorbar(kval_high_data, sigx_high_data, sigx_std_data, fmt='bo--', markersize=3, label='Data $\sigma_x$')
plt.legend(loc='best', prop={'size': 16})
#plt.axis([190,260, 0, 5])
plt.minorticks_on()
plt.grid(True)#, which='both', color = '0.75', linestyle='--')
plt.savefig('xybeamsizes_high_charge_kicker_scan_voltage.pdf', dpi=1000, bbox_inches='tight')















