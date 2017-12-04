from imageReader import *
from chargeReader2 import *
import numpy as np
import matplotlib.pyplot as plt
from glob import glob	
#https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
#==============================================================================
# Main, calling functions    
#==============================================================================

#The following code  is used to do charge cut off
# and analyize images
fiducial_file   = 'yag1_sol_scan_fiducial.npy'
ict_file_sdds   = glob('./sol_scan_nov-2017/charge/YAG*.csv')
yag_backgrounds = glob('./sol_scan_nov-2017/images/*background*.dat')
yags = glob('./sol_scan_nov-2017/images/*2017_img.dat')

#print len(ict_file_sdds)#, ict_file_sdds
#print len(yag_background)#, yag_background
#print len(yag)
count = 0
#ict_file = ict_file_sdds[3]
#while count == 0:
for ict_file in ict_file_sdds:
   print('\n\nCharge file:\n', ict_file) 
   if 'YAG1' in ict_file:
       key  = 'yag1'
       mval = ict_file.split('M')[1].split('_')[0]
       #print(mval)
       yag_back =  [s for s in yag_backgrounds if mval in s]
       yag  =  [s for s in yags if mval in s] 
   
   else: 
      print('bad key')
   
   print("YAG files:\n",yag,'\n', yag_back, '\n')
 
   #SDDS
   volts_array, time = csv_to_volts_array(ict_file)
   #volts_array, cal = sdds_to_volts_array(ict_file)
   charge_array, scaled_volts = ict_charge(volts_array, data_type='csv',time_array=time)
   #plot_ict_curves(scaled_volts, time_array=time)
   count = 1
  
   #Load background images
   (bx, by,b_Nframes, background_array) = readimage(yag_back[0], header_size=3)
   #Deinterlace images with median filter
   #Note, doing filter first removes more noise
   di_background  = difilter(background_array)
   #Average background into one image 
   ave_background = average_images(di_background)
  
   #Load images
   (dx, dy, Nframes, image_array) = readimage(yag[0], header_size=3)
   #print "Dx,Dy,NFrames= ",dx,dy,Nframes
   #Select only images with certain charge
   charge_images, n_images = select_on_charge(image_array, charge_array, 1.1, 1.0)
   #print np.shape(charge_images)

   #Apply median filter to all frames
   di_images = difilter(charge_images)
   #Subtract background
   no_background_images = background_subtraction(di_images, ave_background)

   z = len(no_background_images[0,0,:])
   for i in range(0,z):
      if key=='yag1':
          crop_array = np.zeros((500,480,z)) #640 = rows = Y
          crop_array[:,:,i] = crop_image(no_background_images[:,:,0], x_min=0, x_max=480, y_min=100, y_max=600)


   #view_each_frame(no_background_images)
   ave_crop = average_images(crop_array)
   #rivers = np.empty_like(ave_crop)
   #rivers = np.ma.masked_where(ave_crop < 100, rivers)
   #crop = crop_image(ave_no_back, x_min=50,x_max=500, y_min=0, y_max=450)
'''
   #Starting to find fits
   fiducials = np.load('sol_nov_fiducial.npy', encoding = 'latin1').flatten()
   fid = fiducials[0][key]
   basename = 'plot_hist_'+key
   add_dist_to_image(ave_crop, fid,mval )
   
   #This gives x and y beam sizes 
   beamsizes = fit_data(crop_array, fid, key)
'''


