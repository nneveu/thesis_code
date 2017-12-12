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
fiducial_file   = 'yag1_sol_scan_fiducial_11-02-2017.npy'
data_directory  = './sol_scan_nov-2017/low_charge_Mscan_data/'
ict_file_sdds   = glob(data_directory+'/YAG1_M2*.csv')
yag_backgrounds = glob(data_directory+'/YAG1_M2*background*.dat')
yags            = glob(data_directory+'/YAG1_M2*2017_img.dat')

mask = np.load('mask_dim.npy', encoding = 'latin1').flatten()[0]
#print len(ict_file_sdds)#, ict_file_sdds
#print len(yag_background)#, yag_background
#print len(yag)
count = 0
#ict_file = ict_file_sdds[3]
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
for i in range(200, 204, 5): #,205): #250,5):
   mval = str(i)
   yag       = glob(data_directory+'/YAG1_M'+mval+'*2017_img.dat')[0]
   yag_back  = glob(data_directory+'/YAG1_M'+mval+'*background*.dat')[0]
   ict_file  = glob(data_directory+'/YAG1_M'+mval+'*.csv')[0] 
   
   #SDDS
   volts_array, time = csv_to_volts_array(ict_file)
   #volts_array, cal = sdds_to_volts_array(ict_file)
   charge_array, scaled_volts = ict_charge(volts_array, data_type='csv',time_array=time)
   #plot_ict_curves(scaled_volts, time_array=time)
  
   #Load background images
   (bx, by,b_Nframes, background_array) = readimage(yag_back, header_size=3)
   #Load images, do a charge cut
   (dx, dy, Nframes, image_array) = readimage(yag, header_size=3)
   #Select only images with certain charge
   charge_images = select_on_charge(image_array, charge_array, 0.95, 1.05)

   #Masking everything outside YAG screen
   im_center = [mask['center_x'], mask['center_y']]
   mask_background = mask_images(background_array, bx, by, im_center, mask['radius']) 
   view_each_frame(mask_background)
#   mask = createCircularMask(bx, by, center=[237,297], radius=radius) 
#   masked_img = background_array[:,:,0]
#   masked_img[~mask] = 0
#   view_each_frame(masked_img)

   '''
   #Deinterlace images with median filter
   #Note, doing filter first removes more noise
   #di_background  = difilter(background_array)
   #Average background into one image 
   ave_background = average_images(background_array)
  
   #print "Dx,Dy,NFrames= ",dx,dy,Nframeks
   #print np.shape(charge_images)

   #Apply median filter to all frames
   #Subtract background
   no_background_images = background_subtraction(di_images, background_array)
   di_images = difilter(no_background_images)
  
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
   
   #Starting to find fits
   fiducials = np.load('sol_nov_fiducial.npy', encoding = 'latin1').flatten()
   fid = fiducials[0][key]
   basename = 'plot_hist_'+key
   add_dist_to_image(ave_crop, fid,mval )
   
   #This gives x and y beam sizes 
   beamsizes = fit_data(crop_array, fid, key)
   '''
   count=count+1
