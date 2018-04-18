import numpy as np
import matplotlib
import matplotlib.pyplot as plt

header = 18
z0 = 50
vin = 0.2

singlep1 = 'Ch1_sing_P1.txt'
singlep2 = 'Ch1_sing_P2.txt'
singlep3 = 'Ch1_sing_P3.txt'
singlep4 = 'Ch1_sing_P4.txt'

singles = [singlep1, singlep2, singlep3, singlep4]
style   = ['k-', 'b-', 'o-', 'g--']

plt.xlabel('Time [ns]', size=14) 
plt.ylabel('Z [$\Omega$]', size=14)  
plt.title('Single Port TDR Measurements', size=16)  
#plt.axis([0.9, 2.0, 0, 300]) 


for i, s in enumerate(singles):
    slabel = (s.split('_')[2]).split('.')[0]
    data = np.loadtxt(s, skiprows=header, delimiter=',')
    rho  = data[:,1]/vin
    print(rho)
    zout = z0*( (1+rho)/(1-rho) )
    print(zout) 
    plt.plot(data[:,0]*10**9, zout, alpha=0.7, label=slabel) 

plt.legend(loc='upper left')
plt.savefig('singles.pdf',bbox_inches='tight',dpi=900)




#comm1 = 'R1_Comm_Ch1P1_Ch2P3.txt'
#comm2 = 'R1_Comm_Ch1P2_Ch2P4.txt'
#
#
#fig = plt.figure(2)
#data1 = np.loadtxt(comm1, skiprows=header, delimiter=',')
#data2 = np.loadtxt(comm2, skiprows=header, delimiter=',')
#plt.title('Common Mode TDR Measurements', size=16)
#plt.xlabel('Time [ns]', size=14)
#plt.ylabel('Voltage [V]', size=14) 
#plt.plot(data1[:,0]*10**9, data1[:,1], alpha=0.7, label='P1-P3')
#plt.plot(data2[:,0]*10**9, data2[:,1], '--',alpha=0.7, label='P2-P4')
#plt.legend(loc='upper left')
#plt.savefig('comm.pdf',bbox_inches='tight',dpi=900)


#fig2 = plt.figure(3)
#diff1 = 'R1_Diff_Ch1P1_Ch2P3.txt'
#diff2 = 'R1_Diff_Ch1P2_Ch2P4.txt'
#
#datad1 = np.loadtxt(diff1, skiprows=header, delimiter=',')
#datad2 = np.loadtxt(diff2, skiprows=header, delimiter=',')
#plt.title('Differential Mode TDR Measurements', size=16)
#plt.xlabel('Time [ns]', size=14)
#plt.ylabel('Voltage [V]', size=14)
#plt.plot(datad1[:,0]*10**9, datad1[:,1], alpha=0.7, label='P1-P3')
#plt.plot(datad2[:,0]*10**9, datad2[:,1], '--',alpha=0.7, label='P2-P4')
#plt.legend(loc='upper left')
#plt.savefig('diff.pdf',bbox_inches='tight',dpi=900)















