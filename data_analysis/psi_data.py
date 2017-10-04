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

ict_file_sdds  = glob('./charge/gun_L1-L6_YAG*.sdds')
yag_backgrounds = glob('./images/gun_L1-L6_YAG*_FWHM1pt5_M185_R-_GPhase-20_*background*.dat')
yags = glob('./images/gun_L1-L6_YAG*_FWHM1pt5_M185_R-_GPhase-20_09-2*-2017*.dat')

#print len(ict_file_sdds)#, ict_file_sdds
#print len(yag_background)#, yag_background
#print len(yag)
count = 0
ict_file = ict_file_sdds[4]
while count == 0:
#for ict_file in ict_file_sdds: 
   #https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
   if 'YAG1' in ict_file:
       key  = 'yag1'
       find = 'YAG1'
       basename = 'YAG 1: z = 3.1 [m]'
       yag_back =  [s for s in yag_backgrounds if find in s]
       yag      =  [s for s in yags if find in s] 
   
   elif 'YAG2' in ict_file:
       key  = 'yag2'
       find = 'YAG2'
       basename = 'YAG 2: z = 6.4 [m]'
       yag_back =  [s for s in yag_backgrounds if find in s] 
       yag      =  [s for s in yags if find in s] 
   elif 'YAG3' in ict_file:
       key = 'yag3'
       find = 'YAG3'
       basename = 'YAG 3: z = 8.8 [m]'
       yag_back =  [s for s in yag_backgrounds if find in s] 
       yag      =  [s for s in yags if find in s] 
   elif 'YAG6' in ict_file:
       key = 'yag6'
       find = 'YAG6'
       basename = 'YAG 6: z = 15.8 [m]'
       yag_back =  [s for s in yag_backgrounds if find in s] 
       yag      =  [s for s in yags if find in s] 
   elif 'YAG7' in ict_file:
       key = 'yag7'
       find = 'YAG7'
       yag_back =  [s for s in yag_backgrounds if find in s]
       yag      =  [s for s in yags if find in s]  

   elif 'CTR' in ict_file:
       key = 'yagCTR'
       find = 'CTR'
       basename = 'CTR YAG: z = 16.8 [m]'
       yag_back =  [s for s in yag_backgrounds if find in s] 
       yag      =  [s for s in yags if find in s]  
      
   else: 
      print 'bad key'
   
   print yag_back, yag
   
   #SDDS
   volts_array, cal = sdds_to_volts_array(ict_file)
   charge_array, scaled_volts = ict_charge(volts_array, data_type='sdds',cal_array=cal)
   #plot_ict_curves(scaled_volts, cal)
   count = 1


   #Load background images
   (bx, by,b_Nframes, background_array) = readimage(yag_back[0])
   #Deinterlace images with median filter
   #Note, doing filter first removes more noise
   di_background  = difilter(background_array)
   #Average background into one image 
   ave_background = average_images(di_background)
   
   #Load images
   (dx, dy, Nframes, image_array) = readimage(yag[0])
   #print "Dx,Dy,NFrames= ",dx,dy,Nframes
   #Select only images with certain charge
   charge_images, n_images = select_on_charge(image_array, charge_array, 40.0, 33.0)
   #print np.shape(charge_images)
   #Apply median filter to all frames
   di_images = difilter(charge_images)
   #Subtract background
   no_background_images = background_subtraction(di_images, ave_background)
   z = len(no_background_images[0,0,:])
   for i in range(0,z):
      if key=='yag2':
          crop_array = np.zeros((300,300,z))
          crop_array[:,:,i] = crop_image(no_background_images[:,:,0], x_min=200, x_max=500, y_min=50, y_max=350)
      elif key=='yag1':
          crop_array = np.zeros((420,420,z))
          crop_array[:,:,i] = crop_image(no_background_images[:,:,0], x_min=80, x_max=500, y_min=0, y_max=420)
      elif key=='yag3':
          crop_array = np.zeros((300,300,z))
          crop_array[:,:,i] = crop_image(no_background_images[:,:,0], x_min=175, x_max=475, y_min=100, y_max=400)
      elif key=='yag6':
          crop_array = np.zeros((225,225,z))
          crop_array[:,:,i] = crop_image(no_background_images[:,:,0], x_min=175, x_max=400, y_min=125, y_max=350)
      elif key=='yagCTR':
          crop_array = np.zeros((250,250,z))
          crop_array[:,:,i] = crop_image(no_background_images[:,:,0], x_min=135, x_max=385, y_min=65, y_max=315)


   #view_each_frame(no_background_images)
   ave_crop = average_images(crop_array)
   #rivers = np.empty_like(ave_crop)
   #rivers = np.ma.masked_where(ave_crop < 100, rivers)
   #crop = crop_image(ave_no_back, x_min=50,x_max=500, y_min=0, y_max=450)

   #Starting to find fits
   fiducials = np.load('psi_fiducials.npy').flatten()
   fid = fiducials[0][key]
   #basename = 'plot_hist_'+key
   add_dist_to_image(ave_crop, fid,basename )
   #x_axis   = (np.arange(0,dx) - dx/2)*fiducials[0][key]
   #y_axis   = (np.arange(0,dy) - dx/2)*fiducials[0][key]

   #This gives x and y beam sizes 
   beamsizes = fit_data(crop_array, fiducials, key)

#plt.figure(100)
#plt.plot(x_axis, raw_x)
#plt.show()

#print len(raw_x)
#print len(raw_y)

#s = similarity_check(image_array)
#print s

#------------------------
#Calc charge 
#ict_file_csv = './charge/gun_L1-L6_YAG7_FWHM1pt5_M185_R-_GPhase-20_slit_28400_09-22-2017_LC584AL.csv'

#CSV
#volts_array, time_array = csv_to_volts_array(ict_file_csv)
#charge_array, volts_scaled = ict_charge(volts_array, time_array=time_array, data_type='csv')
#plot_ict_curves(volts_scaled, time_array=time_array)

