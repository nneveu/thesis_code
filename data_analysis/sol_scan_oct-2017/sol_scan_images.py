from imageReader import *
from chargeReader2 import *
import numpy as np
import matplotlib.pyplot as plt
from glob import glob	
#==============================================================================
# Main, calling functions    
#==============================================================================
'''
#The following code was used to find fiducial
fiducial_files = glob('./images/YAG1_M210_10-17-2017.dat')
print(fiducial_files)
fiducial = {}

for f in fiducial_files:
    key = (f.split('_')[0]).split('/')[-1]
    print(key)
    (dx, dy,Nframes, im_fid) = readimage(f)
    #view_each_frame(im_fid)
    di_fid  = difilter(im_fid) 
    #ave_fid = average_images(di_fid)
    image   = di_fid[:,:,1]
    image[0:130, :] = 0
    #view_each_frame(image)
    
    #Deal with dark current yag1, forgot to take fiducial
    if  key == 'YAG1':
        #(bx, by, bn, background_array) = readimage('./images/YAG1_M230_10-17-2017.dat') 
        #di_background  = difilter(background_array) 
        #ave_background = average_images(di_background)

        #no_background = background_subtraction(image, ave_fid)        
        no_beam = remove_beam(image, percent_threshold=0.059) 
        fiducial['yag1'] = fiducial_calc(no_beam, min_r=0.35, max_r=0.4)
        print(fiducial['yag1'])
        #fiducial[key] = (np.load('yag1_fiducial.npy').flatten())[0]['yag1']
        np.save('sol_fiducial.npy',fiducial)

    elif key == 'yag7': 
        fiducial[key] = fiducial_calc(ave_fid, min_r=0.18, max_r=0.2)

    elif key =='yagCTR':
        fiducial[key] = fiducial_calc(ave_fid, YAG_D=50.038) 
    else:
        fiducial[key] = fiducial_calc(ave_fid)

    #np.save('sol_fiducials.npy', fiducial)

#The following code  is used to do charge cut off
# and analyize images
'''
ict_file_sdds  = glob('./charge/YAG*.sdds')
#yag_backgrounds = glob('./images/YAG*.dat')
yags = glob('./images/YAG*.dat')

#print len(ict_file_sdds)#, ict_file_sdds
#print len(yag_background)#, yag_background
#print len(yag)
count = 0
#ict_file = ict_file_sdds[3]
#while count == 0:
for ict_file in ict_file_sdds: 
   #https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
   if 'YAG1' in ict_file:
       key  = 'yag1'
       mval = ict_file.split('_')[1]
       print(mval)
       #yag_back =  [s for s in yag_backgrounds if find in s]
       yag      =  [s for s in yags if mval in s] 
   
   else: 
      print('bad key')
   
   print(yag)
   
   #SDDS
   volts_array, cal = sdds_to_volts_array(ict_file)
   charge_array, scaled_volts = ict_charge(volts_array, data_type='sdds',cal_array=cal)
   #plot_ict_curves(scaled_volts, cal)
   count = 1


   #Load background images
   #(bx, by,b_Nframes, background_array) = readimage(yag_back[0])
   #Deinterlace images with median filter
   #Note, doing filter first removes more noise
   #di_background  = difilter(background_array)
   #Average background into one image 
   #ave_background = average_images(di_background)
   
   #Load images
   (dx, dy, Nframes, image_array) = readimage(yag[0])
   #print "Dx,Dy,NFrames= ",dx,dy,Nframes
   #Select only images with certain charge
   charge_images, n_images = select_on_charge(image_array, charge_array, 51.0, 49.0)
   #print np.shape(charge_images)

   #Apply median filter to all frames
   di_images = difilter(charge_images)
   #Subtract background
   #no_background_images = background_subtraction(di_images, ave_background)
   z = len(di_images[0,0,:])
   for i in range(0,z):
      if key=='yag1':
          crop_array = np.zeros((500,480,z)) #640 = rows = Y
          crop_array[:,:,i] = crop_image(di_images[:,:,0], x_min=0, x_max=480, y_min=100, y_max=600)


   #view_each_frame(no_background_images)
   ave_crop = average_images(crop_array)
   #rivers = np.empty_like(ave_crop)
   #rivers = np.ma.masked_where(ave_crop < 100, rivers)
   #crop = crop_image(ave_no_back, x_min=50,x_max=500, y_min=0, y_max=450)

   #Starting to find fits
   fiducials = np.load('sol_fiducial.npy', encoding = 'latin1').flatten()
   fid = fiducials[0][key]
   #basename = 'plot_hist_'+key
   #add_dist_to_image(ave_crop, fid,mval )
   
   #This gives x and y beam sizes 
   #beamsizes = fit_data(crop_array, fid, key)



