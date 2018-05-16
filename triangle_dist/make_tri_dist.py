import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

def showplot(x,y):
    plt.plot(x,y, '.', markersize=1) 
    plt.show()
    plt.close()


dist = np.loadtxt('tri_DIST.dat')
x    = dist[:,0]
px   = dist[:,1]
y    = dist[:,2]
py   = dist[:,3]
t    = dist[:,4]
pz   = dist[:,5]

tmax = max(t)
tmin = min(t)

xmax = max(x)
xmin = min(x)

#plt.showplot(x,y, '.', markersize=1)
n =1E4

def make_tri(n, xmin, xmax, x):

    half = int(n/2)
    yr  = np.zeros(half*2)
    #step 1
    nr = int(n)
    xr = np.random.rand(nr)

    for j in range(0,nr):
        #step 3
        if j < half:
            yr[j] = (1- np.sqrt(1-xr[j]))*(xmax-xmin)  
        elif j >= half:
        #step 4 
            yr[j] = (-1 + np.sqrt(1-xr[j]))*(xmax-xmin) 

    #showplot(xr, yr)
    for k in range(0,len(x)):
        #print(y[k])
        if (-yr[k]/8 <= x[k] <= yr[k]/8):
            pass
            #x[k]=0
        else:
            #print(x[k])
            x[k]=0
            #pass

    #showplot(xr,x)
    return x, xr

xnew, xr = make_tri(n, -0.0075/2, 0.0075/2, x)
ynew, yr2 = make_tri(n, -0.0075/2, 0.0075/2, y)
  
tscale = xr*(tmax-tmin)
#showplot(tyscale,ynew )

ind = np.where(xnew==0)
tscale[ind] = 0
#print(ind)
print(len(ind))
zs = int(1e4)
print(zs)
xnozero = np.zeros(zs)
tnozero = np.zeros(zs)
pxnoz = np.zeros(zs) 
pynoz = np.zeros(zs) 
pznoz = np.zeros(zs) 

for i,xval in enumerate(xnew):
    xnozero[i] = xval
    tnozero[i] = tscale[i]
    pynoz[i] = py[i]
    pxnoz[i] = px[i]
    pznoz[i] = pz[i]

ynozero = xnozero

#xnozero = xnew[~np.all(xnew == 0).any()]
#tnozero = tscale[~np.all(tscale == 0).any()]

#showplot(-tnozero, xnozero)
#xnew = np.ma.masked_equal(x,0)
#tnew = np.ma.masked_equal(t,0)
#plt.plot(xnew, '.', markersize=1)
#plt.show()
z = 3*10**8*-tnozero
#showplot(z, xnozero)
tosave = np.column_stack((xnozero, pxnoz, ynozero, pynoz, z, pznoz))

np.savetxt('tridist.txt', tosave, delimiter = ' ', header ='1E4')

#nullfmt = NullFormatter()         # no labels
#
## definitions for the axes
#left, width = 0.1, 0.65
#bottom, height = 0.1, 0.65
#bottom_h = left_h = left + width + 0.02
#
#rect_scatter = [left, bottom, width, height]
#rect_histx = [left, bottom_h, width, 0.2]
#rect_histy = [left_h, bottom, 0.2, height]
#
## start with a rectangular Figure
#plt.figure(1, figsize=(8, 8))
#
#axScatter = plt.axes(rect_scatter)
#axHistx = plt.axes(rect_histx)
#axHisty = plt.axes(rect_histy)
#
## no labels
#axHistx.xaxis.set_major_formatter(nullfmt)
#axHisty.yaxis.set_major_formatter(nullfmt)
#
## the scatter plot:
#axScatter.scatter(t,x)
#
## now determine nice limits by hand:
#binwidth = 0.25
#xymax = np.max([np.max(np.fabs(tnew)), np.max(np.fabs(xnew))])
#lim = (int(xymax/binwidth) + 1) * binwidth
#
#axScatter.set_xlim((-lim, lim))
#axScatter.set_ylim((-lim, lim))
#
#bins = np.arange(-lim, lim + binwidth, binwidth)
#axHistx.hist(x, bins=bins)
#axHisty.hist(y, bins=bins, orientation='horizontal')
#
#axHistx.set_xlim(axScatter.get_xlim())
#axHisty.set_ylim(axScatter.get_ylim())
#
##plt.show()


