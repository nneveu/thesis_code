# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 12:10:00 2016

@author: nneveu
"""
#Importing modules ~~~~~~~~~~~~~~~~~~
import scipy.io as spio
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
#import numpy as np
#from matplotlib import rc

#==============================================================================
# rc('font', **{'family': 'serif', 'serif':['Computer Modern']})
# rc('text', usetex=True)
#==============================================================================

#==============================================================================
# load functions do the following:
#     -creates a dictionary with stats information stored
#     -info can be accessed using key words, i.e.: energy = data['E']
#==============================================================================
def loadgpt(myfile):
    
    data = spio.loadmat(myfile, squeeze_me=True, struct_as_record=False)['Data']
    #==============================================================================
    # for i in xrange(0,31): #This loop gives names of data in GPT file
    #     print data[0][i]
    #==============================================================================
#==============================================================================
#     Values in GPT file: 
#     position
#     rmsx
#     rmsxp
#     rmsxxp
#     maxx
#     chirpx
#     nemixrms
#     rmsy
#     rmsyp
#     rmsyp
#     rmsyyp
#     maxy
#     chirpy
#     nemiyrms
#     rmsz
#     rmszp
#     maxz
#     chirpz
#     nemizrms2
#     numpar
#     avgG
#     CSalphax
#     CSbetax
#     CSgammax
#     stdt
#     histx
#     histy
#     histt
#     histbx
#     histby
#     histG    
#==============================================================================
    z       = data[1][0]
    xrms    = data[1][1]
    xprms   = data[1][2]
    xxprms  = data[1][3]
    maxx    = data[1][4]
    chirpx  = data[1][5]
    nemixrms = data[1][6]
    yrms     = data[1][7]
    yprms    = data[1][8]
    yprms    = data[1][9]
    yyprms   = data[1][10]
    maxy     = data[1][11]
    chirpy    = data[1][12]
    nemiyrms  = data[1][13]
    zrms      = data[1][14]
    zprms     = data[1][15]
    maxz      = data[1][16]
    chirpz    = data[1][17]
    nemizrms2 = data[1][18]
    numpar    = data[1][19]
    avgG      = data[1][20]
    
    E = avgG*0.511

    return ({'z':z, 'E':E, 'xrms':xrms, 'yrms':yrms, 'zrms':zrms, 
    'xprms':xprms, 'yprms':yprms, 'zprms':zprms, 'nemixrms':nemixrms, 'nemiyrms':nemiyrms, 'nemizrms':nemizrms2,
    'xxprms':xxprms, 'yyprms':yyprms, 'xmax':maxx, 'ymax':maxy, 'zmax':maxz, 'numpar': numpar})

def load(myfile):

    lookfor = "OPAL"
    
    with open(myfile, "r") as parsefile:
        for num, line in enumerate(parsefile, 1):
            if lookfor in line: 
                skip = num
                break   

    data = np.loadtxt(myfile, skiprows=skip)

    mm = 10**3
    mmr = 10**6

    t  = data[:,0] #Units of s	
    z  = data[:,1] #Units of m
    numpart = data[:,2]
    E  = data[:,4] #Units of MeV

    xrms = mm*data[:,5]#Units of m 
    yrms = mm*data[:,6]
    zrms = mm*data[:,7]

    pxrms = data[:,8] #Units of 1
    pyrms = data[:,9]
    pzrms = data[:,10]
	
    xemit = mmr*data[:,11] #Units of mm-mrad
    yemit = mmr*data[:,12]
    zemit = mmr*data[:,13]
     
    xmean = data[:,14]*mm
    ymean = data[:,15]*mm
    zmean = data[:,16]
    
    xmax = data[:,17]*10**3
    ymax = data[:,18]*10**3
    zmax = data[:,19]
    
    xpx = data[:,20] #Units of 1
    ypy = data[:,21]
    zpz = data[:,22]

    Bx = data[:,35] #Units of T
    By = data[:,36]
    Bz = data[:,37]

    Ex = data[:,38] #Units of MV/m
    Ey = data[:,39]
    Ez = data[:,40] 

    dE = data[:,47] #Units of MeV

    return ({'t':t, 'z':z, 'numpart':numpart, 'E':E, 'dE':dE,'xrms':xrms, 'yrms':yrms, 'zrms':zrms, 
    'pxrms':pxrms, 'pyrms':pyrms, 'pzrms':pzrms, 'xemit':xemit, 'yemit':yemit, 'zemit':zemit,
    'xpx':xpx, 'ypy':ypy, 'zpz':zpz, 'xmean':xmean, 'ymean': ymean, 'zmean':zmean, 
    'xmax':xmax, 'ymax':ymax, 'zmax':zmax,
    'Bx':Bx, 'By':By, 'Bz':Bz, 'Ex':Ex, 'Ey':Ey, 'Ez':Ez})
#==============================================================================
# plotformat function does the following:
#     -create figure
#     -sets axis values
#     -sets x and y labels
#     -sets title
#==============================================================================
def plotformat(ptype='energy', sigma=3, location='', x1=0, x2=0.5, y1=0, y2=8.0):
    #Current defaults plots are for the gun
    #Change x1, x2, y1, and y2, to change the plot area
    plt.figure()
    plt.axis((x1, x2, y1, y2))
    plt.xlabel(r'z [m]', size=18)
    
    if ptype == 'energy':
        plt.ylabel(r'$\gamma mc^2$ [MeV]', size=18)    
        plt.title(r'Mean Energy ' + location, size=18)
        
    elif ptype =='dE':
        #Make sure to change y2 to negative for B and E plots
        plt.ylabel(r'dE [MeV]', size=18)
        plt.title( r'Change in Energy' + location, size=18)          
        
    elif ptype =='Bz':
        #Make sure to change y2 to negative for B and E plots
        plt.ylabel(r'Bz [T]', size=18)
        plt.title( r'Magnetic Field ' + location, size=18)     
        
    elif ptype =='Ez':
        plt.ylabel(r'Ez [T]', size=18)
        plt.title( r'Electric Field' + location, size=18)  
            
    elif ptype =='xemit':
        plt.ylabel(r'$\epsilon_{nx}$ [mm-mrad]', size=18)
        plt.title( r'X Emittance ' + location, size=18) 
        
    elif ptype == 'yemit':
        plt.ylabel(r'$\epsilon_{ny}$ [mm-mrad]', size=18)
        plt.title( r'Y Emittance' + location, size=18) 
        
    elif ptype == 'zemit':
        plt.ylabel(r'$\epsilon_{nz}$ [mm-mrad]', size=18)
        plt.title('Z Emittance '+ location, size=18)
        
    elif ptype == 'xrms':
        plt.title('Beam Size'+ location, size=18)
        if sigma ==3:
            plt.ylabel(r'3 $\sigma_x$ [mm]', size=18) 
        else:
            plt.ylabel(r'$x_{rms}$ [mm]', size=18)
            
    elif ptype == 'yrms':
        plt.title('Beam Size'+ location, size=18)
        if sigma ==3:
            plt.ylabel(r'3 $\sigma_y$ [mm]', size=18) 
        else:
            plt.ylabel(r'$y_{rms}$ [mm]', size=18)
            
    elif ptype == 'xyrms':
        plt.title('Beam Size'+ location, size=18)
        if sigma ==3:
            plt.ylabel(r'3 $\sigma$ [mm]', size=18) 
        else:
            plt.ylabel(r'$xy_{rms}$ [mm]', size=18)
        
    elif ptype == 'zrms':
        plt.title('Bunch Length'+ location, size=18)
        if sigma ==3:
            plt.ylabel(r'3 $\sigma_z$ [mm]', size=18) 
        else:
            plt.ylabel(r'$z_{rms}$ [mm]', size=18)
#==============================================================================
# plotting function does the following:
#     -plot variable Vs. Z
#     -sets legend labels
#     -creates legend
#==============================================================================  
def plotting(data, ptype='energy', legendloc='best', sigma=3, mylabel='none'):
    
    if ptype == 'energy' :   
        plt.plot(data['z'], data['E']+0.511,  '-', label=mylabel, markevery=100)
        
    elif ptype == 'dE':
        plt.plot(data['z'], data['dE'],  '-', label=mylabel, markevery=100)
        
    elif ptype == 'Bz':
        plt.plot(data['z'], data['Bz'],  '-', label=mylabel, markevery=100)
        
    elif ptype == 'By':
        plt.plot(data['z'], data['By'],  '-', label=mylabel, markevery=100)
        
    elif ptype == 'Ez':
        plt.plot(data['z'], data['Ez'],  '-', label=mylabel, markevery=100)
        
    elif ptype == 'Ey':
        plt.plot(data['z'], data['Ey'],  '-', label=mylabel, markevery=100)
        
    elif ptype == 'Ex':
        plt.plot(data['z'], data['Ex'],  '-', label=mylabel, markevery=100)

    elif ptype == 'xemit':
        plt.plot(data['z'], data['xemit'],  '-', label=mylabel, markevery=100)
    
    elif ptype == 'yemit' :   
        plt.plot(data['z'], data['yemit'],  '-', label=mylabel, markevery=100)
        
    elif ptype == 'zemit' :   
        plt.plot(data['z'], data['zemit'],  '-', label=mylabel, markevery=100)
        
    elif ptype == 'xrms':
        #Default is to plot 3 sigma beam size
        #Change option sigma to any number except 3 to plot xrms
        # i.e. sigma = 1, will plot xrms. 
        if sigma ==3:
            plt.plot(data['z'],data['xrms']*3, '-', label=mylabel) 
        else:
            plt.plot(data['z'],data['xrms'], '-', label=mylabel)    

    elif ptype == 'yrms':
        if sigma ==3:
            plt.plot(data['z'],data['yrms']*3, '-', label=mylabel) 
        else:
            plt.plot(data['z'],data['yrms'], '-', label=mylabel)  
            
            
    elif ptype == 'xyrms':
        if sigma ==3:
            plt.plot(data['z'],data['xrms']*3, '-', label=mylabel) 
            plt.plot(data['z'],data['yrms']*3, '-', label=mylabel) 
        else:
            plt.plot(data['z'],data['xrms'], '-', label=mylabel)
            plt.plot(data['z'],data['yrms'], '-', label=mylabel)  

    elif ptype == 'zrms':
        if sigma ==3:
            plt.plot(data['z'],data['zrms']*3, '-', label=mylabel) 
        else:
            plt.plot(data['z'],data['zrms'], '-', label=mylabel)  

    if legendloc == 'lower right':
        plt.legend(loc=4)
    elif legendloc == 'lower left':
        plt.legend(loc=3)
    elif legendloc == 'upper left':
        plt.legend(loc=2)
    elif legendloc == 'upper right':
        plt.legend(loc=1)
    else:
        n=1
        #plt.legend(loc='best') 

   
   
#~~~~~~~~~~~~OLD PLOTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
def emit3in1(xemit, yemit, zemit, z, filename):

	with PdfPages('EmittancePlots.pdf') as pdf:

		plt.plot(z,xemit, 'b-', label='x emittance')
		plt.plot(z,yemit, 'r-', label='y emittance')
		plt.plot(z,zemit, 'k-', label='z emittance')

		plt.legend(loc='best')
		plt.xlabel(r'Z [m]')
		plt.ylabel(r'Emittance [mm-mrad]')
		plt.title(r'Emittance Values Vs. Z')
		pdf.savefig()
		plt.close()

def emitxyandz(xemit, yemit, zemit, z, filename):
	
	with PdfPages(filename+'.pdf') as pdf:
		
		plt.plot(z,xemit, 'b-', label = r'\epsilon_{nx}')
		plt.plot(z,yemit, 'r-', label = r'\epsilon_{ny}')
		
		plt.legend(loc='best')
                plt.xlabel(r'Z [m]')
                plt.ylabel(r'Emittance [mm-mrad]')
                plt.title(r'X and Y Emittance Vs. Z')
                pdf.savefig()
                plt.close()

		plt.plot(z,zemit, 'r-', label = r'\epsilon_{ny}')

                plt.legend(loc='best')
                plt.xlabel(r'Z [m]')
                plt.ylabel(r'Emittance [mm-mrad]')
                plt.title(r' Z Emittance Vs. Z')
                pdf.savefig()
                plt.close()


def beplots(Bx, By, Bz, Ex, Ey, Ez, z, filename):

	with PdfPages('BandEplots.pdf') as pdf:

		#Plotting Magnetic fields
		plt.plot(z, Bx,'r-', label = 'Bx')
		plt.plot(z, By,'k-', label = 'By')
		plt.plot(z, Bz,'b-', label = 'Bx')
	
        	plt.legend(loc='best')
        	plt.xlabel(r'Z [m]', size=20)
                plt.ylabel(r'Magnetic Fields [T]', size=20)
		plt.title(r'Magnetic Fields vs. Z', size=24)
        	pdf.savefig()
        	plt.close()

		#Plotting Electric Fields
		plt.plot(z, Ex,'r-', label = 'Ex')
		plt.plot(z, Ey,'k-', label = 'Ey')
		plt.plot(z, Ez,'b-', label = 'Ez')
	
		plt.legend(loc='best')
		plt.xlabel(r'Z [m]', size=20)
		plt.ylabel(r'Electric Fields [Mv/m]', size=20)
		plt.title(r'Electric Fields vs. Z', size=24)
		pdf.savefig()
		plt.close()



def edeplots(E, dE, z, filename):
	
	with PdfPages(filename) as pdf:
		spread = dE/E

		fig, ax1=plt.subplots()
	
		ax1.plot(z, E, 'b-', label='Energy')

		ax2 = ax1.twinx()	
		ax2.plot(z, spread, 'r-', label='dE')
	
		ln1, lab1 = ax1.get_legend_handles_labels()
		ln2, lab2 = ax2.get_legend_handles_labels()
		ax2.legend(ln1+ln2, lab1+lab2, loc='upper left')

		plt.title(r'Energy and Energy Spread Vs. Z')
		ax1.set_xlabel(r'Z [m]')
		ax1.set_ylabel(r'Energy [MeV]')
		ax2.set_ylabel(r'dE/E')

		for t1 in ax1.get_yticklabels():
			t1.set_color('b')
		for t1 in ax2.get_yticklabels():
 			t1.set_color('r')

		pdf.savefig()
		plt.close()

def rmsplots(xrms, yrms, zrms, z, filename):

   with PdfPages('RMSplots.pdf') as pdf:
	plt.plot(z,xrms, 'bo', label='xrms')
	plt.plot(z,yrms, 'r-', label='yrms')
	plt.plot(z,zrms, 'k-', label='zrms')

	plt.legend(loc='best')
	plt.xlabel(r'Z [m]', size = 20)
	plt.ylabel(r'RMS Values [mm]', size = 20)
	plt.title(r'RMS Values Vs. Z')
	pdf.savefig()
	plt.close()

