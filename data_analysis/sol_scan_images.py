from imageReader import *
from chargeReader2 import *
import numpy as np
import matplotlib.pyplot as plt
from glob import glob	
#https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string

#The following code  is used to do charge cut off
# and analyize images
fiducial_file   = 'sol_scan_nov-2017/fiducials/YAG1_fiducial_11-02-2017_img.dat'
data_directory  = './sol_scan_nov-2017/low_charge_Mscan_data/'
ict_files_sdds  = glob(data_directory+'/YAG1_M2*.csv')
yag_backgrounds = glob(data_directory+'/YAG1_M2*background*.dat')
yags            = glob(data_directory+'/YAG1_M2*2017_img.dat')

#Load fiducial image
(fx, fy, fz, fid_image) = readimage(fiducial_file, header_size=3)
#Finding dimensions of YAG screen and fiducial
circle_dim = circle_finder(fid_image, min_r=0.367, max_r=0.38)
fiducial   = fiducial_calc(circle_dim['radius'])
print('fiducial:', fiducial)

#Error from choosing diff radius values
# delta_fiducial ~= 0.0005 mm/pixel, less than 1%
#fiducials = np.load('yag1_sol_scan_fiducial_11-02-2017.npy', encoding = 'latin1').flatten()
#old = fiducials[0]['yag1']
#print('old:', old, 'new:', fiducial)

#Make a smaller radius for mask 
print('radius before', circle_dim['radius'])
circle_dim['radius'] = int(circle_dim['radius']*0.8) 
print('radius after', circle_dim['radius'])

#while count == 0:
#for ict_file in ict_file_sdds:
#   print('\n\nCharge file:\n', ict_file) 
#   if 'YAG1' in ict_file:
#       key  = 'yag1'
#       mval = ict_file.split('M')[1].split('_')[0]
#       #print(mval)
#       yag_back =  [s for s in yag_backgrounds if mval in s]
#       yag  =  [s for s in yags if mval in s] 
#   
#   else: 
#      print('bad key')
#   
#   #print("YAG files:\n",yag,'\n', yag_back, '\n')
#
for i in range(205, 210, 5): #,205): #250,5):
   mval = str(i)
   yag       = glob(data_directory+'/YAG1_M'+mval+'*2017_img.dat')[0]
   ict_file  = glob(data_directory+'/YAG1_M'+mval+'*.csv')[0] 
   yag_back  = glob(data_directory+'/YAG1_M'+mval+'*background*.dat')[0]
  
   #SDDS
   volts_array, time = csv_to_volts_array(ict_file)
   #volts_array, cal = sdds_to_volts_array(ict_file)
   charge_array, scaled_volts = ict_charge(volts_array, data_type='csv',time_array=time)
   #plot_ict_curves(scaled_volts, time_array=time)
   
   #Load images, do a charge cut
   (dx, dy, Nframes, image_array) = readimage(yag, header_size=3)
   #view_each_frame(image_array)

   #Select only images with certain charge
   #usage = select_on_charge(images, charge, min_charge, max_charge)
   charge_images = select_on_charge(image_array, charge_array, 0.95, 1.05)

   #Load background images
   (bx, by,b_Nframes, background_array) = readimage(yag_back, header_size=3)

   #Masking everything outside YAG screen
   masked_background    = mask_images(background_array, circle_dim)
   masked_charge_images = mask_images(charge_images, circle_dim)
   #im_center, mask['radius']) 
   #view_each_frame(mask_cut_images)

   #Clean up noise with median filter
   di_background  = difilter(masked_background)
   #Average background into one image 
   ave_background = average_images(di_background)
  
   #Subtract background
   no_background = background_subtraction(masked_charge_images, ave_background)
   #view_each_frame(no_background)
   
   #Apply median filter to all frames
   di_images = difilter(no_background)

   #Crop images 
   x, y, z = di_images.shape
   #usage = np.zeros((dy, dx, dz))
   crop_array = np.zeros((350,350,z)) 
   for i in range(0,z):
      crop_array[:,:,i] = crop_image(di_images[:,:,i], x_min=80, x_max=430, y_min=80, y_max=430)

   #view_each_frame(crop_array)
   ave_crop = average_images(crop_array)
   #view_each_frame(ave_crop)    
      
   #Starting to find fits
   key = 'yag1'
   #Showing x and y projections on averaged image
   add_dist_to_image(ave_crop, fiducial, './output/'+key+'_M'+mval,title="M="+mval, background=20)
   
   #This gives array with x and y beam sizes 
   #Every beam size is recorded, not the average only
   #The arrays will be the same size as the amount of shots analyzed
   #subtract base level?
   test = crop_array - 10
   #beamsizes = fit_data(crop_array, fiducial, './output/beamsizes_'+key+'_M'+mval)
   #beamsizes = fit_data(test, fiducial, './output/beamsizes_'+key+'_M'+mval)
  
