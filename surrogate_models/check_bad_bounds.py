import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

db1   = np.load('libE_history_after_gen_900.npy')
loc   = np.where(db1['flag']!=0)
flags = db1['flag'][loc]
xvals = db1['x'][loc]

npts = len(xvals)
data = np.zeros([npts, 7])

for i in range(0,len(xvals)):
    #print(xvals[i][6])
    data[i,0] = xvals[i][0]
    data[i,1] = xvals[i][1]
    data[i,2] = xvals[i][2]
    data[i,3] = xvals[i][3]
    data[i,4] = xvals[i][4]
    data[i,5] = xvals[i][5]
    data[i,6] = xvals[i][6]
    #print(bf)

import sys

sys.path.insert(0, '/home/nicole/Documents/pyOPALTools')
sys.path.insert(0, '/home/nicole/Documents/pyOPALTools/utilities/')

from db import mldb


baseFN   = 'rand_sample'
root     = "."
yNames   = ['emit_x', 'emit_y', 'emit_s', 'rms_x', 'rms_y', 'rms_s', 'energy', 'dE']

#dbw       = mldb.mldb()
#dbw.buildFromSDDS(baseFN, root, yNames)
#dbw.printOverview()

# Now reasd the data back and loop over to train the model
# Note the 0 in the get functions denotes a generation 
dbr       = mldb.mldb()
dbr.load(baseFN+'_910.pk')
#dbr.printOverview()
uqdata = np.zeros([npts+1, 7])

count = 0
for i in range(0, dbr.getSampleSize()):
    #print(dbr.getObjVec(0,i))     # y
    #print(dbr.getDVarVec(0,i)[0])    # x
    test = dbr.getDVarVec(0,i)[0]
    #print(test)
    new = any(abs(float(test)-data[:,0])< 1.0e-3)
    #loc = np.where(new < 1.0e-3)
    if new:
        #print('yes')
        #print(i, new[loc])
        uqdata[count,0] = dbr.getDVarVec(0,i)[0]
        uqdata[count,1] = dbr.getObjVec(0,i)[1]
        uqdata[count,2] = dbr.getObjVec(0,i)[2]
        uqdata[count,3] = dbr.getObjVec(0,i)[3]
        uqdata[count,4] = dbr.getObjVec(0,i)[4]
        uqdata[count,5] = dbr.getObjVec(0,i)[5]
        uqdata[count,6] = dbr.getObjVec(0,i)[6]
        count = count+1

#print(uqdata[:,0][:3], data[:,0][:3])
print(len(uqdata[:,0]))


#print(count)
#data = [
#    go.Parcoords(
#        line = dict(color = 'blue'),
#        dimensions = list([
#            dict(range = [400,550],
#                 #constraintrange = [1,2],
#                 label = 'BF', values = bf),
#
#            dict(range = [150,280],
#                 #tickvals = [1.5,3,4.5],
#                 label = 'M', values = m),
#
#            dict(range = [-20,0],
#                 label = 'P0', values = p0),
#
#            dict(range = [-20, 0],
#                 label = 'P1', values = p1),
#
#            dict(range = [60, 75],
#                 label = 'G0', values = g0),
#
#            dict(range = [15, 25],
#                 label = 'G1', values = g1),
#
#            dict(range = [0.001, 0.004],
#                 label = 'Rc',  values = rc),
#
#        ])
#    )
#]

#plotly.offline.plot(data, filename = 'parcoord-dimensions')


#plt.plot(bf, '.')
#plt.savefig('bf_vals.pdf')

#plt.plot(m, '.')
#plt.savefig('m_vals.pdf')

#plt.plot(p0, 'r.', label = 'gun')
#plt.plot(p1, 'b.', label = 'linac')
#plt.savefig('p_vals.pdf')

#plt.plot(g0, 'r.', label = 'gun') 
#plt.plot(g1, 'b.', label = 'linac')                                 
#plt.savefig('g_vals.pdf')

#plt.plot(rc, '.')
#plt.savefig('rc_vals.pdf')









