import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from glob import glob
from natsort import natsorted, ns
import sys
sys.path.append('/home/nicole/Documents/thesis_code')
import myplots as mplt

matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 

opal1 = mplt.load('optLinac_M185_GPhase-20_R8.5mm_FWHM1.5e-12_L1-L6_0_3D.stat') #_3D.stat')
opal2 = mplt.load('optLinac_M250_GPhase-20_R8.5mm_FWHM1.5e-12_L1-L6_0_3D.stat') #_3D.stat') 

beamfiles = glob('./output/1nC/*beamsizes_1nC.npy')
n_points  = len(beamfiles)
#https://stackoverflow.com/questions/4836710/does-python-have-a-built-in-function-for-string-natural-sort
natsorted(beamfiles, key=lambda y: y.lower())
#natsorted(beamfiles, alg=ns.IGNORECASE)

ave_sigx  = {} #np.zeros((n_points))
ave_sigy  = {} #np.zeros((n_points))

max_barx  = {} #np.zeros((n_points)) 
max_bary  = {} #np.zeros((n_points)) 

error_barsx  = {} #np.zeros((n_points)) 
error_barsy  = {} #np.zeros((n_points)) 

std_sigx = {} 
std_sigy = {}

#YAGS: 1, 2, 3, 6, CTR, 7
x_axis = np.array([3.1, 6.377, 8.76, 15.808, 16.753])

for n, bfile in enumerate(beamfiles, 0):
    #print(n, bfile)
    #key = (bfile[0].split('_')).split('.')[0]
    key = (bfile.split('_')[1]).split('.')[0]
    beamsizes = np.load(bfile).flatten()[0]
    sigmax    = beamsizes['sigmax']
    sigmay    = beamsizes['sigmay']

    ave_sigx[key] = np.mean(sigmax)
    ave_sigy[key] = np.mean(sigmay)

    std_sigx[key] = np.std(sigmax)
    std_sigy[key] = np.std(sigmay)    
    
    #print ave_sigx[key] 
    #print std_sigx[key] 
    #print ave_sigx[key]
    #print ave_sigx[key]-std_sigx[key]

    error_barsx[key] = [3*std_sigx[key], 3*std_sigx[key]]
    error_barsy[key] = [3*std_sigy[key], 3*std_sigy[key]]
    #error_barsx[key] = [ave_sigx[key] -np.min(sigmax), np.max(sigmax)-ave_sigx[key] ] 
    #error_barsy[key] = [ave_sigy[key] -np.min(sigmay), np.max(sigmay)-ave_sigy[key] ] 
    print(error_barsx[key])

sigmax = np.array([ave_sigx['yag1'], ave_sigx['yag2'], ave_sigx['yag3'], ave_sigx['yag6'], ave_sigx['yagCTR']])
sigmay = np.array([ave_sigy['yag1'], ave_sigy['yag2'], ave_sigy['yag3'], ave_sigy['yag6'], ave_sigy['yagCTR']])


errorx = np.append([error_barsx['yag1'], error_barsx['yag2']], [error_barsx['yag3'], error_barsx['yag6'], error_barsx['yagCTR']], axis=0) 
errory = np.append([error_barsy['yag1'], error_barsy['yag2']], [error_barsy['yag3'], error_barsy['yag6'], error_barsy['yagCTR']], axis=0)
#print error_barsx

print(sigmax)
print(sigmay)

lowerx = errorx[:,0]
upperx = errorx[:,1]

lowery = errory[:,0]
uppery = errory[:,1]

#print lower_bound
#print upper_bound

major_ticks = np.arange(0, 20, 5)                                              
#minor_ticks = np.arange(0, 101, 5)  

plt.figure(1)
plt.title('Beam Size: $\sigma_x$', size=20)
plt.xlabel('Z Location [m]', size=20)
plt.ylabel('$\sigma_x$ [mm]', size=20)
plt.plot(opal1['z'], opal1['xrms'], 'g-', label = 'OPAL Weak Solenoid')
plt.plot(opal2['z'], opal2['xrms'], 'b-', label = 'OPAL Strong Solenoid') 
plt.errorbar(x_axis, sigmax, yerr=[lowerx, upperx], fmt='ko-', markersize=5, label='Data Weak Solenoid')
plt.legend(loc='best', prop={'size': 16})
plt.axis([0,20, 0, 17])
plt.minorticks_on()
plt.grid(True)#, which='both', color = '0.75', linestyle='--')
plt.savefig('beamsizes_x.pdf', dpi=1000, bbox_inches='tight')

plt.figure(2)
plt.title('Beam Size: $\sigma_y$', size=20)
plt.xlabel('Z Location [m]', size=20)
plt.ylabel('$\sigma_y$ [mm]', size=20)
plt.plot(opal1['z'], opal1['yrms'], 'g-', label = 'OPAL Weak Solenoid')
plt.plot(opal2['z'], opal2['yrms'], 'b-', label = 'OPAL Strong Solenoid')
plt.errorbar(x_axis, sigmay, yerr=[lowery, uppery],fmt='ko-', markersize=5, label='Data Weak Solenoid' )
plt.legend(loc='best', prop={'size': 16})
plt.axis([0,20, 0, 17])
plt.minorticks_on()
plt.grid(True)#, which='both', color='0.75', linestyle='--')
plt.savefig('beamsizes_y.pdf', dpi=1000, bbox_inches='tight')

