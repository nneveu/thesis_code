import numpy as np
import matplotlib.pyplot as plt

def calc_rho(l_eff, angle_deg):
    radians = np.radians(angle_deg)
    rho = l_eff/(2.0*np.sin(radians/2.0))
    return rho

def counts_to_current(counts):
    #This function returns the current
    #given the counts for the EEX dipole 
    #on the drive line. 
    cal_counts  = np.array([1000.0,5000.0,10000.0,15000.0]) #These were measured
    meas_volts  = np.array([3.7,18.8,37.5,56.3]) #These were measured
    ratio       = 25.0/100.0 #ratio of current/volts 
    cal_current = meas_volts*ratio

    poly = np.polyfit(cal_counts, cal_current, 1)
    #print(poly)
    current = poly[0]*counts + poly[1]
    return current

def current_to_bfield(current):
    #from gao's script to pull info from plot
    #B in Tesla
    bfield = (180.9708*current - 7.2053)*10**-4
    return bfield

def counts_to_energy(rho, counts):
    i = counts_to_current(counts)    
    #B in Tesla
    bfield = current_to_bfield(i)
    #Energy in MeV
    momentum = ((bfield*rho)/3.335641)*10**3
    total_e = np.sqrt(0.511**2+momentum**2)
    print( 'momentum', momentum)
    print( 'total energy', total_e, '\n')
    return total_e

def current_to_energy(rho, current):
    bfield = current_to_bfield(current)
    #Energy in MeV
    momentum = ((bfield*rho)/3.335641)*10**3
    
    total_e = np.sqrt(0.511**2+momentum**2)
    print( 'momentum', momentum)
    print( 'total energy', total_e, '\n')
    return total_e

angle = 20 #degrees
leff = 0.3154

rho = calc_rho(leff, angle)
print("rho", rho, '\n') 

print('Measurements Pre-2018')
mean1       = np.mean([5826,5763]) #,5632 mediean 11/02
mean2       = np.mean([10054,9921,9968,9926])
#mean3      = np.mean([14688]) #bad measurement?
mean3       = np.mean([14072,14083])
mean3_highq = np.mean([13472,13792]) #13808 median 10/17])

gun           = counts_to_energy(rho, 1472.0)#current_to_bfield(counts_to_current(1472.0))
gun_l1l2      = counts_to_energy(rho, mean1)#current_to_bfield(counts_to_current(mean1))
gun_l1l2_l3l5 = counts_to_energy(rho, mean2)#current_to_bfield(counts_to_current(mean2))
gun_l1_to_l6  = counts_to_energy(rho, mean3)#current_to_bfield(counts_to_current(mean3))
high_q_energy = counts_to_energy(rho, mean3_highq)

#e1 = total_energy(gun)
#e2 = total_energy(gun_l1l2)
#e3 = total_energy(gun_l1l2_l3l5)
#e4 = total_energy(gun_l1_to_l6)
#e5 = total_energy(high_q_energy)

#energy spread on 1nc 11-02
#lowenergy  = counts_to_energy(rho, 5376)
#highenergy = counts_to_energy(rho, 5888)
#l = total_energy(lowenergy)
#h = total_energy(highenergy)
#momentum = ((gun*rho)/3.3356)*10**3
#total_e = total_energy(momentum)

#print 'direct energy', counts_to_energy_calc(rho, 1472.0)*10**3
#print('recorded current', current[1])
#plt.plot(counts, current)
#plt.show()

print('Measurements 2018 \n')
#current_to_energy(rho, 0.8)
print('gun, bad measurement')
counts_to_energy(rho, 1408)

print('Gun, L4, L6')
counts_to_energy(rho, 4770)

print('Gun, L4, L6, bad measurement - uncentered')
counts_to_energy(rho, 4736)

print('Gun, L3, L5, bad measurment - uncentered')
counts_to_energy(rho, 5184)


print('Gun, L1, L2, bad measurement - uncentered')
counts_to_energy(rho, 5408)

print('Gun L1-L6, full energy')
print('max energy:')
counts_to_energy(rho, 13503)
print('min energy:')
counts_to_energy(rho, 12768)
