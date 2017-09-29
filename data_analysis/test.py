import numpy as np

f1 = 'yag6-2-3_fiducial.npy'
f2 = 'yag1_fiducial.npy'

f1 = np.load(f1).flatten()
#f2 = np.load(f2).flatten()

#f1[0]['yag1'] = f2[0]['yag1']

print f1[0]
#print f2[0]

#np.save('fiducials_1236.npy', f1)
