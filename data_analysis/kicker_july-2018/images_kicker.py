from imageReader import *
from chargeReader import *
import numpy as np
import matplotlib.pyplot as plt
from glob import glob	
from scipy import ndimage, stats

def make_incrementor(n):
 #https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string   
 return lambda x: x + n

#The following code  is used to do charge cut off
# and analyize images
fiducial_file   = '/home/nicole/Documents/thesis_code/data_analysis/kicker_july-2018/kicker_07-19-2018/Yag6_fiducial.dat' 
data_directory  = './kicker_07-19-2018/high_charge/' 
ict_files_sdds  = glob(data_directory+'/high_charge_YAG6_*kV*.sdds')
#print(ict_files_sdds)
#yag_backgrounds = glob(data_directory+'/high_charge_YAG6_*background*.dat')
yags            = glob(data_directory+'/high_charge_YAG6_*kV*2018.dat')

#-------------------------------------------------------------------------
#Load fiducial image, adjust YAG mask size (july data)
(fx, fy, fz, fid_image) = readimage(fiducial_file, header_size=6)
circle_dim = circle_finder(fid_image, min_r=0.15, max_r=0.2, showcircle=False)
#circle_dim = circle_finder(test, min_r=0.37, max_r=0.4)
fiducial   = fiducial_calc(circle_dim['radius'])

#-------------------------------------------------------------------------
all_beamsizesx = np.zeros((10))
all_beamsizesy = np.zeros((10))
deflection = np.zeros((6))
deviations = np.zeros((6))
summary = 'beamsizes_kickerscan_high_charge_07-2018.txt'
f = open(summary,'w')
f.write('Npoints' + "\t"+ 'Kicker Voltage' + "\t" + 'sigmax_ave' + "\t" + 'sigmay_ave' + "\t" \
        + 'stdx' + "\t" + 'stdy' + "\t" + 'rx_ave' + "\t"+ 'ry_ave'+"\n")

kicker_voltages = np.array((0,18,20,22, 24, 26))
for n, i in enumerate(kicker_voltages):    #range(0, 1, 2)): 
   print('\n\n')
   print('The voltage is', i, 'kV')
   kval = str(i)
   yag       = glob(data_directory+'/high_charge_YAG6_'+kval+'*2018.dat')[0]#_img.dat')[0]
   ict_file  = glob(data_directory+'/high_charge_YAG6_'+kval+'*.sdds')[0] #csv')[0] 
   #yag_back  = glob(data_directory+'/YAG6_'+mval+'*background*.dat')[0]

   #yag       = glob(data_directory+'/YAG1_M'+mval+'*2017_img.dat')[0]
   #ict_file  = glob(data_directory+'/YAG1_M'+mval+'*.csv')[0] 
   #yag_back  = glob(data_directory+'/YAG1_M'+mval+'*background*.dat')[0]
   #-------------------------------------------------------------------------
   #Get charges 
   charge_array, scaled_volts = ict_charge(ict_file, data_type='sdds')
   
   #Load images, do a charge cut
   (dx, dy, Nframes, image_array) = readimage(yag, header_size=6)

   #Select only images with certain charge
   #usage = select_on_charge(images, charge, min_charge, max_charge)
   charge_images = select_on_charge(image_array, charge_array, 29.5, 30.5)#0.95, 1.05)

   #Load background images
   #(bx, by,b_Nframes, background_array) = readimage(yag_back, header_size=3)

   #Masking everything outside YAG screen
   #masked_background    = mask_images(background_array, circle_dim)
   circle_dim['radius']=circle_dim['radius']*1.25
   circle_dim['center_y']=circle_dim['center_y']*0.8
   masked_charge_images = mask_images(charge_images, circle_dim)
   #view_each_frame(masked_charge_images)

   #Apply median filter to all frames
   di_images = do_filter(charge_images, n=3)

   #Crop images 
   x, y, z = di_images.shape
   #Crop sizes
   cropy = 200
   cropx = 230
   #usage = np.zeros((dy, dx, dz))
   crop_array = np.zeros((cropx,cropy,z)) 
   for j in range(0,z):
      crop_array[:,:,j] = crop_image(di_images[:,:,j], x_min=50, x_max=250, y_min=120, y_max=350)

   #view_each_frame(crop_array)
   #Swap axis for kicker
   rotated_image = np.zeros((cropy,cropx,z))
   for j in range(0,z):
       rotated_image[:,:,j] = np.rot90(crop_array[:,:,j],axes=(-2,-1)) #ndimage.rotate(crop_array[:,:,j], 90)
       #plt.imshow(turn[:,:,j])
       #plt.show()
   #ave_crop = average_images(crop_array)
   ave_crop = average_images(rotated_image)
   #view_each_frame(ave_crop)    
      
   #Starting to find fits
   key = 'yag6'
   #Showing x and y projections on averaged image
   add_dist_to_image(ave_crop, fiducial, './output3/'+key+'_kicker_voltage'+kval,title="V="+kval, background=200)
   
   #This gives array with x and y beam sizes 
   #Every beam size is recorded, not the average only
   #The arrays will be the same size as the amount of shots analyzed
   #beamsizes = fit_gaussian(crop_array, fiducial, './output/beamsizes_'+key+'_M'+mval, clip_tail=80)
   #This array has all values of sigmax and sigmay 
   beamsizes, rx2, ry2, centroids= combo_model(crop_array, fiducial, './output3/beamsizes_'+key+'_K'+kval+'.pdf')
   deflection[n] = np.average(centroids['y'])
   deviations[n] = np.std(centroids['y'])

   #Saving summary data to text file
   f.write(str(len(rx2))+ "\t" + str(i) + "\t"\
                       + str(np.average(beamsizes['sigmax'])) + "\t"\
                       + str(np.average(beamsizes['sigmay'])) + "\t"\
            + str(np.std(beamsizes['sigmax'])) + "\t"\
            + str(np.std(beamsizes['sigmay'])) + "\t" 
            + str(np.average(rx2)) + "\t"+ str(np.average(ry2))+"\n")

  #all_beamsizesx[n] = np.average(beamsizes['sigmax'])
  #all_beamsizesy[n] = np.average(beamsizes['sigmay'])

#print(all_beamsizesx, np.max(all_beamsizesx), np.min(all_beamsizesx))
#print(all_beamsizesy, np.max(all_beamsizesy), np.min(all_beamsizesy))

np.save('xbeamsizes_30nC.npy', all_beamsizesx )
np.save('ybeamsizes_30nC.npy', all_beamsizesy)

f.close()

#fit_fn = np.poly1d(deflection) 
# Generated linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(kicker_voltages,deflection)
line = slope*kicker_voltages+intercept
print('r_value', r_value, 'std_err', std_err)

xoffset    = deflection[1:] - deflection[0] 
print(np.abs(xoffset))
angles     = np.arcsin(np.abs(xoffset/1000))
angles_deg = (180.0/np.pi)*angles
print('angle estimate',  angles_deg)
print('deviations for plot', deviations)

plt.title('Kicker Deflection, $30 \pm 0.5$ nC Beam', size=20)
plt.xlabel('Kicker Voltage [kV]', size=18)
plt.ylabel('Beam Centroid \non YAG Screen [mm]', size=18)
plt.errorbar(kicker_voltages, deflection, deviations, fmt='bo', markersize=3, label='Data')
plt.plot(kicker_voltages, line, 'k--', label='Linear Fit')
plt.legend(loc='upper right')
plt.grid('on')
plt.savefig('kicker_linearity.pdf', dpi=1000, bbox_inches='tight')
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
