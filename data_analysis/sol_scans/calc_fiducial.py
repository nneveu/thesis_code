from imageReader import * 
from chargeReader2 import *
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
#==============================================================================
# Main, calling functions    
#==============================================================================
#The following code was used to find fiducial
fiducial_dict  = 'yag1_sol_scan_fiducial.npy'
fiducial_files = glob('sol_scan_nov-2017/fiducials/YAG1*.dat')
print(fiducial_files)
fiducial = {}
radius   = {}
#image   = di_fid[:,:,1]
#image[0:130, :] = 0
#view_each_frame(image)

for f in fiducial_files:
    key = (f.split('/')[2]).split('_')[0]
    print(key)
    (dx, dy,Nframes, im_fid) = readimage(f, header_size=3)
    #averaging fiducial images    
    di_fid  = difilter(im_fid)
    ave_fid = average_images(di_fid) 
    #view_each_frame(ave_fid)

    if  key == 'YAG1':
        #(bx, by, bn, background_array) = readimage('./images/YAG1_M230_10-17-2017.dat') 
        #di_background  = difilter(background_array) 
        #ave_background = average_images(di_background)

        #no_background = background_subtraction(image, ave_fid)        
        #no_beam = remove_beam(image, percent_threshold=0.059) 
        #fiducial['yag1'] = fiducial_calc(no_beam, min_r=0.35, max_r=0.4)

        fiducial['yag1'] = fiducial_calc(ave_fid, min_r=0.367, max_r=0.38, mask_info='mask_dim.npy')
        print('fiducial', fiducial['yag1'])
        mask = np.load('mask_dim.npy').flatten()[0]
        print(mask['center_x'], mask['center_y'])
        #np.save(fiducial_dict,fiducial)

    elif key == 'yag7':
        fiducial[key], radius = fiducial_calc(ave_fid, min_r=0.18, max_r=0.2)

    elif key =='yagCTR':
        fiducial[key], radius = fiducial_calc(ave_fid, YAG_D=50.038)
    else:
        fiducial[key] = fiducial_calc(ave_fid)

    #np.save('radius.npy', radius)
