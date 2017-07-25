# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 18:50:27 2017

@author: nneveu
"""

import matplotlib.pyplot as plt

new = [1,0.805031447,0.528301887,0.880503145,0.58490566,0.465408805,0.51572327,0.823899371]
old = [1,1.053471097,1.221610577,1.036708024,1.211850381,1.27664935,1.231445421,1.04505427]


plt.figure()
#plt.axis((x1, x2, y1, y2))
plt.xlabel(r'Bunch Number', size=18)	
plt.ylabel(r'Bunch Intensity [arb. units]', size=18)
plt.plot(new, '-og', label='new')
plt.plot(old, '-ob', label='old')
plt.legend(loc=2)
