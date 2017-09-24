import imageReader as ir
import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
# Main, calling functions    
#==============================================================================
#testfile1  = '/Users/nneveu/Documents/DATA/TBA(1-13-16)/DriveOn_WSPE2_WD1_1p756.dat'
testfile2 = '/home/nicole/Documents/thesis_code/data_analysis/gun_L1-L6_YAG6_FWHM1pt5_M250_R8pt5_GPhase-20_09-20-2017.dat'

yag1 = './gun_L1-L6_YAG1_FWHM1pt5_M185_R-_GPhase-20_09-22-2017.dat'
grasshopper = 'gun_L1-L6_YAG7_FWHM1pt5_M185_R-_GPhase-20_slit_29800_09-22-2017_Grasshopper3 GS3-PGE-23S6M_16376365_img.dat' 


#Load images
(dx, dy, Nframes, image_array) = ir.readimage(yag1)
print "Dx,Dy,NFrames= ",dx,dy,Nframes

#View images
#ir.view_each_frame(image_array)

ir.average_images(image_array, dx, dy)




