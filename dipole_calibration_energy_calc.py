import numpy as np
import matplotlib.pyplot as plt


angle = 20 #degrees
radians = (angle)

'''
This function returns the current
given the counts for the EEX dipole
on the drive line.
'''
def counts_to_current(counts):
    cal_counts  = np.array([1000.0,5000.0,10000.0,15000.0]) #These were measured
    mv      = np.array([3.7,18.8,37.5,56.3]) #These were measured
    ratio   = 25.0/100.0
    cal_current = mv*ratio

    poly = np.polyfit(cal_counts, cal_current, 1)
    #print(poly)
    current = poly[0]*counts + poly[1]

    return current


leff = 0.3154
test = counts_to_current(5000.0)
print('test current',test)
#print('recorded current', current[1])

#bfield = 180.9708*current - 7.2053

#plt.plot(counts, current)
#plt.show()





