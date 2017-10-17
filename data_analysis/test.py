import numpy as np
from imageReader import *
from chargeReader2 import *
from matplotlib.ticker import NullFormatter
import matplotlib.pyplot as plt

#f1 = 'fiducials_1236CTR.npy'
#f1 = 'yag6-2-3_fiducial.npy'
#f2 = 'psi_fiducials.npy'
#f2 = 'yag1_fiducial.npy'

#f1 = np.load(f1).flatten()
#f2 = np.load(f2).flatten()

#f1[0]['yagCTR'] = f2[0]['yagCTR']
#f1[0]['yag1'] = f2[0]['yag1'] 
#print f1[0]
#print f2[0]

#np.save('fiducials_1236CTR.npy', f1)

#https://matplotlib.org/examples/pylab_examples/scatter_hist.html

laserfile = './images/laser_profile_UVcamera_9-22-2017.dat'
(bx, by,b_Nframes, laser_array) = readimage(laserfile)
di_array  = difilter(laser_array)
ave_background = average_images(di_array)
crop= crop_image(ave_background, x_min=70, x_max=530, y_min=0, y_max=480)
fitx, fity = raw_data_curves(ave_background, oneframe=1)

from mpl_toolkits.axes_grid1 import make_axes_locatable

dx, dy = crop.shape

xaxis   = (np.arange(0,dx) - dx/2)
yaxis   = (np.arange(0,dy) - dy/2)

fitx, fity = raw_data_curves(crop, oneframe=1)
fitxnorm = (fitx - np.min(fitx))/(np.max(fitx)-np.min(fitx))#*15 -20  
fitynorm = (fity - np.min(fity))/(np.max(fity)-np.min(fity))#*15 -20 

fig, ax = plt.subplots(figsize=(10.5, 10.5))
ax.set_aspect(1.)
divider = make_axes_locatable(ax)
axHistx = divider.append_axes("top", 1.25, pad=0.1, sharex=ax)
axHisty = divider.append_axes("right", 1.25, pad=0.1, sharey=ax)
# make some labels invisible
axHistx.xaxis.set_tick_params(labelbottom=False)
axHisty.yaxis.set_tick_params(labelleft=False)
axHisty.plot(fitxnorm, -xaxis, linewidth=3)
axHistx.plot(yaxis, fitynorm, linewidth=3)#, orientation='horizontal') 

cmap = plt.cm.viridis
cmap.set_under(color='white')
color = ax.imshow(crop, interpolation='none', cmap=cmap, vmin=1, extent=[np.min(xaxis), np.max(xaxis), np.min(yaxis), np.max(yaxis)])
#ax.plot(xaxis, fitxnorm, '--', linewidth=5, color='firebrick')
#ax.plot(yaxis, fitynorm, '--', linewidth=5, color='firebrick') 
ax.tick_params(labelsize=12)
#axHistx.set_title('YAG 1: Z = 3.1 m', size=20) 
axHistx.set_title('UV laser profile', size=20)
ax.set_xlabel('X pixels', size=18)
ax.set_ylabel('Y pixels', size=18)
plt.colorbar(color,ax=ax, orientation="horizontal", shrink=0.7, pad=0.1)
plt.savefig('laser.pdf', dpi=1000, bbox_inches='tight')






'''
plt.figure(1, figsize=(8, 8))
#ax.set_aspect(1)
#divider = make_axes_locatable(ax)
#axHistx = divider.append_axes("top", 1.25, pad=0.1, sharex=ax)
#axHisty = divider.append_axes("right", 1.25, pad=0.1, sharey=ax)
nullfmt = NullFormatter()         # no labels

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 65
bottom_h = left_h = left + width + 0.02

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.2]
rect_histy = [left_h, bottom, 0.2, height]
#axScatter = plt.axes(rect_scatter)
axScatter = plt.axes(rect_scatter)
axHistx = plt.axes(rect_histx)
axHisty = plt.axes(rect_histy)
axHistx.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)
# make some labels invisible
axHistx.xaxis.set_tick_params(labelbottom=False)
axHisty.yaxis.set_tick_params(labelleft=False)
axHisty.plot(fitx/np.max(fitx), -xaxis, linewidth=3)
axHistx.plot(yaxis, fity/np.max(fity), linewidth=3)#, orientation='horizontal') 

cmap = plt.cm.viridis
cmap.set_under(color='white')
color = axScatter.imshow(crop, interpolation='none', cmap=cmap, vmin=1, extent=[np.min(xaxis), np.max(xaxis), np.min(yaxis), np.max(yaxis)])
#ax.plot(xaxis, fitxnorm, '--', linewidth=5, color='firebrick')
#ax.plot(yaxis, fitynorm, '--', linewidth=5, color='firebrick') 
axScatter.tick_params(labelsize=12)
#axHistx.set_title('YAG 1: Z = 3.1 m', size=20) 
axHistx.set_title('Laser Profile', size=20)
axScatter.set_xlabel('X pixels', size=18)
axScatter.set_ylabel('Y pixels', size=18)
plt.colorbar(color,ax=axScatter, orientation="horizontal", shrink=0.7, pad=0.1)
#plt.savefig('laser.pdf', dpi=1000, bbox_inches='tight')
plt.show()


#add_dist_to_image(ave_crop, fid,basename )

'''


