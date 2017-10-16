import numpy as np
import matplotlib.pyplot as plt

#_________________plot distribution_______________
dist_file = 'distribution.data'
dist = np.loadtxt(dist_file, skiprows=1)
plt.plot(dist[:,0], dist[:,1])
plt.savefig('dist_plot.pdf')

