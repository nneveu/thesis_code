from imageReader import *
from chargeReader2 import *
import numpy as np
import matplotlib.pyplot as plt
from glob import glob	
#==============================================================================
# Main, calling functions    
#==============================================================================
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




#Load background images
#Deinterlace images with median filter
#Average background into one image
###########(bx, by,b_Nframes, background_array) = readimage(yag1_background)
#Note, doing filter first removes more noise
###########di_background  = difilter(background_array)
#ave_background = average_images(background_array)#di_background)
###########ave_background = average_images(di_background)


#Load images
#Apply median filter to all frames
#Subtract background
###########3(dx, dy, Nframes, image_array) = readimage(yag1)
#print "Dx,Dy,NFrames= ",dx,dy,Nframes
#s = similarity_check(image_array)
#print s
##############di_images = difilter(image_array)
##############ave_image = average_images(di_images) 
##############no_background_images = background_subtraction(ave_image, ave_background)

#########ave_no_back = average_images(no_background_images)
#View images
#view_each_frame(ave_no_back)

#Calculating fiducial
#(fx, fy, fNframes, fiducial_array) = readimage(no_background_images)#yag2_fiducial)
#di_background = difilter(fiducial_array)
#ave_fiducial = average_images()
#view_each_frame(fiducial_array)
############no_beam = remove_beam(no_background_images, percent_threshold=0.05)
############yag2_mm_pixel = fiducial_calc(no_beam)#no_background_images)#ave_fiducial)

############print yag2_mm_pixel 


#------------------------
#Calc charge 
#ict_file = './charge/gun_L1-L6_YAG6_FWHM1pt5_M250_R8pt5_GPhase-20_09-20-2017LC584AL.sdds'

#volts_array, cal = sdd_to_volts_array(ict_file)
#scaled_volts, charge_array = ict_charge(volts_array, cal)
#plot_ict_curves(scaled_volts, cal)

#desired_charge = 40
#loc = np.where(charge_array[0,:] < -38.0)
#print len(loc[0]) 













