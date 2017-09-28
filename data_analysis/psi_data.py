from imageReader import *
import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
# Main, calling functions    
#==============================================================================
#testfile1  = '/Users/nneveu/Documents/DATA/TBA(1-13-16)/DriveOn_WSPE2_WD1_1p756.dat'
testfile2 = '/home/nicole/Documents/thesis_code/data_analysis/gun_L1-L6_YAG6_FWHM1pt5_M250_R8pt5_GPhase-20_09-20-2017.dat'

yag1 = './gun_L1-L6_YAG1_FWHM1pt5_M185_R-_GPhase-20_09-22-2017.dat'
yag1_background = './gun_L1-L6_YAG1_FWHM1pt5_M185_R-_GPhase-20_background_09-22-2017.dat' 

grasshopper = 'gun_L1-L6_YAG7_FWHM1pt5_M185_R-_GPhase-20_slit_29800_09-22-2017_Grasshopper3 GS3-PGE-23S6M_16376365_img.dat' 

yag2_fiducial = './yag2_fiducial.dat'

#Load background images
#Deinterlace images with median filter
#Average background into one image
(bx, by,b_Nframes, background_array) = readimage(yag1_background)
#Note, doing filter first removes more noise
di_background  = difilter(background_array)
#ave_background = average_images(background_array)#di_background)
ave_background = average_images(di_background)


#Load images
#Apply median filter to all frames
#Subtract background
(dx, dy, Nframes, image_array) = readimage(yag1)
#print "Dx,Dy,NFrames= ",dx,dy,Nframes
#s = similarity_check(image_array)
#print s
di_images = difilter(image_array)
ave_image = average_images(di_images) 
no_background_images = background_subtraction(ave_image, ave_background)

#########ave_no_back = average_images(no_background_images)
#View images
#view_each_frame(ave_no_back)

#Calculating fiducial
#(fx, fy, fNframes, fiducial_array) = readimage(no_background_images)#yag2_fiducial)
#di_background = difilter(fiducial_array)
#ave_fiducial = average_images()
#view_each_frame(fiducial_array)
no_beam = remove_beam(no_background_images, percent_threshold=0.05)
yag2_mm_pixel = fiducial_calc(no_beam)#no_background_images)#ave_fiducial)
print yag2_mm_pixel 

