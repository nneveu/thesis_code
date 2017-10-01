from imageReader import *
from chargeReader2 import *
import numpy as np
import matplotlib.pyplot as plt
from glob import glob	
#==============================================================================
# Main, calling functions    
#==============================================================================

#The following code was used to find fiducial
"""
fiducial_files = glob('./images/fiducials/yag*fiducial.dat')
print fiducial_files
fiducial = {}

for f in fiducial_files:
    key = (f.split('_')[0]).split('/')[-1]
    print key
    (dx, dy,Nframes, im_fid) = readimage(f)
    di_fid  = difilter(im_fid) 
    ave_fid = average_images(di_fid)
    
    #Deal with dark current yag1, forgot to take fiducial
    if  key == 'yag1':
        #(bx, by, bn, background_array) = readimage('./images/gun_L1-L6_YAG1_FWHM1pt5_M185_R-_GPhase-20_background_09-22-2017.dat') 
        #di_background  = difilter(background_array) 
        #ave_background = average_images(di_background)

        #no_background = background_subtraction(ave_fid, ave_background)        
        #no_beam = remove_beam(no_background, percent_threshold=0.05) 
        #fiducial[key] = fiducial_calc(no_beam)
        fiducial[key] = (np.load('yag1_fiducial.npy').flatten())[0]['yag1']
        #np.save('psi_fiducials.npy',fiducial)

    elif key == 'yag7': 
        fiducial[key] = fiducial_calc(ave_fid, min_r=0.18, max_r=0.2)

    elif key =='yagCTR':
        fiducial[key] = fiducial_calc(ave_fid, YAG_D=50.038) 
    else:
        fiducial[key] = fiducial_calc(ave_fid)

    np.save('psi_fiducials.npy', fiducial)
"""
#The following code  is used to do charge cut off
# and analyize images
ict_file_sdds = './charge/gun_L1-L6_YAG1_FWHM1pt5_M185_R-_GPhase-20_09-22-2017LC584AL.sdds'
yag_background = './images/gun_L1-L6_YAG1_FWHM1pt5_M185_R-_GPhase-20_background_09-22-2017.dat'
yag = './images/gun_L1-L6_YAG1_FWHM1pt5_M185_R-_GPhase-20_09-22-2017.dat'
 
#SDDS
volts_array, cal = sdds_to_volts_array(ict_file_sdds)
charge_array, scaled_volts = ict_charge(volts_array, data_type='sdds',cal_array=cal)
#plot_ict_curves(scaled_volts, cal)

#Load background images
(bx, by,b_Nframes, background_array) = readimage(yag_background)
#Deinterlace images with median filter
#Note, doing filter first removes more noise
di_background  = difilter(background_array)
#Average background into one image 
ave_background = average_images(di_background)

#Load images
(dx, dy, Nframes, image_array) = readimage(yag)
#print "Dx,Dy,NFrames= ",dx,dy,Nframes
#Select only images with certain charge
charge_images, n_images = select_on_charge(image_array, charge_array, 31.0, 29.0)
#print np.shape(charge_images)
#Apply median filter to all frames
di_images = difilter(charge_images)
#Subtract background
no_background_images = background_subtraction(di_images, ave_background)
#view_each_frame(no_background_images)
#ave_no_back = average_images(no_background_images)

#Starting to find fits
fiducials    = np.load('psi_fiducials.npy').flatten()
sigmax   = np.zeros((n_images))
sigmay   = np.zeros((n_images))

for n in range(0,n_images):
    raw_x, raw_y = raw_data_curves(no_background_images[:,:,n], dx, dy)
    x_axis, sigmax[n] = fit_data(raw_y, fiducials[0]['yag1'])
    x_axis, sigmay[n] = fit_data(raw_y, fiducials[0]['yag1'])
print sigmax, sigmay

#print x_axis

#plt.figure(100)
#plt.plot(x_axis, raw_x)
#plt.show()

#print len(raw_x)
#print len(raw_y)

#s = similarity_check(image_array)
#print s

#------------------------
#Calc charge 
#ict_file_sdds = './charge/gun_L1-L6_YAG6_FWHM1pt5_M250_R8pt5_GPhase-20_09-20-2017LC584AL.sdds'
#ict_file_csv = './charge/gun_L1-L6_YAG7_FWHM1pt5_M185_R-_GPhase-20_slit_28400_09-22-2017_LC584AL.csv'

#CSV
#volts_array, time_array = csv_to_volts_array(ict_file_csv)
#charge_array, volts_scaled = ict_charge(volts_array, time_array=time_array, data_type='csv')
#plot_ict_curves(volts_scaled, time_array=time_array)





