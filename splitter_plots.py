# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 18:50:27 2017

@author: nneveu
"""
import numpy as np
import matplotlib.pyplot as plt


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

new = [1,0.805031447,0.528301887,0.880503145,0.58490566,0.465408805,0.51572327,0.823899371]
old = [1,1.053471097,1.221610577,1.036708024,1.211850381,1.27664935,1.231445421,1.04505427]
x = [1,2,3,4,5,6,7,8]

std_old = np.std(old)
std_new = np.std(new)
mean_old = sum(old)/8
mean_new = sum(new)/8


plt.figure()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.axis((0, 9, 0.2, 1.35))
plt.xlabel(r'Laser Pulse Number', size=16)	
plt.ylabel(r'Pulse Intensity [arb. unit]', size=16)
plt.plot(x, new, '-og', label='$\pm5\%$')
plt.plot(x, old, '-ob', label='$\pm3\%$' )

#plt.plot([0, 8], [mean_new, mean_new], '-og', label='Mean New Splitters')
#plt.plot([0, 8], [mean_old, mean_old], '-ob', label='Mean Old Splitters' )
plt.legend(loc=3, numpoints=1)
plt.grid('on')
plt.savefig('../thesis/tex/images/splitter_improvement.jpg',bbox_inches='tight',dpi=900)
