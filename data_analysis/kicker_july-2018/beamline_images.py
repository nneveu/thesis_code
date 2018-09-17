from imageReader import *
from chargeReader import *
import numpy as np
import matplotlib.pyplot as plt
from glob import glob	

def make_incrementor(n):
 #https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string   
 return lambda x: x + n

#The following code  is used to do charge cut off
# and analyize images
#fiducial_file   = '/home/nicole/Documents/thesis_code/data_analysis/kicker_july-2018/kicker_07-19-2018/Yag6_fiducial.dat'
fid_dir         = '/home/nicole/Documents/thesis_code/data_analysis/kicker_july-2018/kicker_07-19-2018/'
data_directory  = './kicker_07-19-2018/high_charge/'
ict_files_sdds  = glob(data_directory+'/YAG*_0kV*.sdds')
yag_backgrounds = glob(data_directory+'/YAG*0kV*background*.dat')
yags            = glob(data_directory+'/YAG*0kV_07*2018.dat')


#-------------------------------------------------------------------------
all_beamsizesx = np.zeros((10))
all_beamsizesy = np.zeros((10))
summary = 'beamsizes_beamline_high_charge_07-2018.txt'
#f = open(summary,'w')
#f.write('Npoints' + "\t"+ 'YAG' + "\t" + 'sigmax_ave' + "\t" + 'sigmay_ave' + "\t" \
#        + 'stdx' + "\t" + 'stdy' + "\t" + 'rx_ave' + "\t"+ 'ry_ave'+"\n")
#4,5,6,8,9



###FIDUCIAL CALCULATIONS
yagnumbers = np.array((2,3,4,6,8,9))#,6,8,9))
#yag 5, 0.4, 0.45
rmin = np.array((0.27, 0.3, 0.25, 0.15, 0.25, 0.24))
rmax = np.array((0.33, 0.33, 0.35, 0.2, 0.33, 0.25))

#Calculating fiducials
f = open('fiducials.txt', 'w')
f.write('YAG' + '\t' + 'fiducial\n')
for i,yag in enumerate(yagnumbers):

   print('\n\n YAG', str(yag))
   nyag = str(yag)
   print(fid_dir+'YAG'+nyag+'_fiducial.dat') 
   #-------------------------------------------------------------------------
   #Load fiducial image, adjust YAG mask size
   fiducial_file = glob(fid_dir+'YAG'+nyag+'_fiducial.dat')[0]
   (fx, fy, fz, fid_image) = readimage(fiducial_file, header_size=6)
   
   if yag==5:
       #Crop images 
       x, y, z = fid_image.shape
       print(x,y,z)
       #usage = np.zeros((dy, dx, dz))
       crop_array = np.zeros((480,480,z)) 
       for j in range(0,z):
           crop_array[:,:,j] = crop_image(fid_image[:,:,j], x_min=0, x_max=580, y_min=120, y_max=600)
       fid_image = crop_array

   circle_dim = circle_finder(fid_image, min_r=rmin[i], max_r=rmax[i], showcircle=True)
   #circle_dim = circle_finder(test, min_r=0.37, max_r=0.4)
   fiducial   = fiducial_calc(circle_dim['radius'])
  
   f.write(str(nyag) + '\t' + str(fiducial) +'\n')
   #Make a smaller radius for mask (july data)
   #print('radius before', circle_dim['radius'])
   #circle_dim['radius'] = int(circle_dim['radius']*0.8) 
   #print('radius after', circle_dim['radius'])
f.close

#   yag       = glob(data_directory+'high_charge_YAG'+nyag+'_0kV_07*2018.dat')[0]#_img.dat')[0]
#   ict_file  = glob(data_directory+'high_charge_YAG'+nyag+'*.sdds')[0] #csv')[0] 
#   #yag_back  = glob(data_directory+'high_charge_YAG'+nyag+'*background*.dat')[0]
#
#   #-------------------------------------------------------------------------
#   #Get charges 
#   charge_array, scaled_volts = ict_charge(ict_file, data_type='sdds')#'csv')
#   
#   #Load images, do a charge cut
#   (dx, dy, Nframes, image_array) = readimage(yag, header_size=6)
#
#   #Select only images with certain charge
#   #usage = select_on_charge(images, charge, min_charge, max_charge)
#   charge_images = select_on_charge(image_array, charge_array, 29.5, 30.5)#0.95, 1.05)
#
#   #Load background images
#   #(bx, by,b_Nframes, background_array) = readimage(yag_back, header_size=6)
#
#   #Masking everything outside YAG screen
#   #masked_background    = mask_images(background_array, circle_dim)
#   circle_dim['radius'] = 0.8*circle_dim['radius']
#   masked_charge_images = mask_images(charge_images, circle_dim)
#   #im_center, mask['radius']) 
#   #view_each_frame(mask_cut_images)
#
#   #Clean up noise with median filter
#   #background  = do_filter(masked_background)
#   #Average background into one image 
#   #ave_background = average_images(masked_background)
#  
#   #Subtract background
#   #no_background = background_subtraction(masked_charge_images, ave_background)
#   #view_each_frame(no_background)
#   
#   #Apply median filter to all frames
#   di_images = do_filter(masked_charge_images, n=3)
#
#   #Crop images 
#   x, y, z = di_images.shape
#   #usage = np.zeros((dy, dx, dz))
#   crop_array = np.zeros((300,300,z)) 
#   for j in range(0,z):
#      crop_array[:,:,j] = crop_image(di_images[:,:,j], x_min=100, x_max=400, y_min=100, y_max=400)
#
#   #view_each_frame(crop_array)
#   ave_crop = average_images(crop_array)
#   #view_each_frame(ave_crop)    
#      
#   #Starting to find fits
#   key = 'yag' +str(nyag)
#   #Showing x and y projections on averaged image
#   add_dist_to_image(ave_crop, fiducial, './output_high_charge/'+key+'_0kV',title="YAG "+nyag, background=20)
#   
#   #This gives array with x and y beam sizes 
#   #Every beam size is recorded, not the average only
#   #The arrays will be the same size as the amount of shots analyzed
#   #beamsizes = fit_gaussian(crop_array, fiducial, './output/beamsizes_'+key+'_M'+mval, clip_tail=80)
#   #This array has all values of sigmax and sigmay 
#   beamsizes, rx2, ry2, centroids = combo_model(crop_array, fiducial, './output_high_charge/beamsizes_YAG'+nyag+'_0kV.pdf')
#   
#   f.write(str(len(rx2))+ "\t" + str(i) + "\t"\
#                        + str(np.average(beamsizes['sigmax'])) + "\t"\
#                        + str(np.average(beamsizes['sigmay'])) + "\t"\
#             + str(np.std(beamsizes['sigmax'])) + "\t"\
#             + str(np.std(beamsizes['sigmay'])) + "\t" 
#             + str(np.average(rx2)) + "\t"+ str(np.average(ry2))+"\n")
#
#   #all_beamsizesx[n] = np.average(beamsizes['sigmax'])
#   #all_beamsizesy[n] = np.average(beamsizes['sigmay'])
#
##print(all_beamsizesx, np.max(all_beamsizesx), np.min(all_beamsizesx))
##print(all_beamsizesy, np.max(all_beamsizesy), np.min(all_beamsizesy))
#
##np.save('xbeamsizes_1nC.npy', all_beamsizesx )
##np.save('ybeamsizes_1nC.npy', all_beamsizesy)
#
#f.close()
