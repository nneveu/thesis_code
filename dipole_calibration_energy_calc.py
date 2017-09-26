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
    mv      = np.array([3.7,18.8,37.5,56.3]) #These were measured
    ratio   = 25.0/100.0
    cal_current = mv*ratio

    poly = np.polyfit(cal_counts, cal_current, 1)
    #print(poly)
    current = poly[0]*counts + poly[1]
    return current


def current_to_bfield(current):
    bfield = (180.9708*current - 7.2053)*10**-4
    return bfield

def counts_to_energy(rho, counts):
    i = counts_to_current(counts)    
    bfield = current_to_bfield(i)
    energy = ((bfield*rho)/3.3356)*10**3
    return energy    

def total_energy(momentum):
    total_e = np.sqrt(0.511**2+momentum**2)
    print 'momentum', momentum
    print 'total energy', total_e
    return total_e

angle = 20 #degrees
leff = 0.3154

rho = calc_rho(leff, angle)
print "rho", rho 

mean1       = np.mean([5826,5763])
mean2       = np.mean([10054,9921,9968,9926])
mean3       = np.mean([14072,14083])
mean3_highq = np.mean([13472,13792])

gun           = counts_to_energy(rho, 1472.0)#current_to_bfield(counts_to_current(1472.0))
gun_l1l2      = counts_to_energy(rho, mean1)#current_to_bfield(counts_to_current(mean1))
gun_l1l2_l3l5 = counts_to_energy(rho, mean2)#current_to_bfield(counts_to_current(mean2))
gun_l1_to_l6  = counts_to_energy(rho, mean3)#current_to_bfield(counts_to_current(mean3))
high_q_energy = counts_to_energy(rho, mean3_highq)


e1 = total_energy(gun)
e2 = total_energy(gun_l1l2)
e3 = total_energy(gun_l1l2_l3l5)
e4 = total_energy(gun_l1_to_l6)
e5 = total_energy(high_q_energy)



#momentum = ((gun*rho)/3.3356)*10**3
#print 'gun b', gun
#print 'momentum', momentum
#total_e = total_energy(momentum)


#print 'direct energy', counts_to_energy_calc(rho, 1472.0)*10**3
#print('recorded current', current[1])
#plt.plot(counts, current)
#plt.show()





