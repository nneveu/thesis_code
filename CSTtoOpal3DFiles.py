# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:50:10 2017

@author: nneveu

ombine 3D linac files from CST
"""
import sys
sys.path.append('/Users/nneveu/Desktop/Scripts/3druns')
import linecache
#==============================================================================
# This function combines E and H CST files
#==============================================================================
def CSTcombo(efilein, hfilein, ehfileout):
    
    num_lines = sum(1 for line in open(efilein))
    #efin = open(efilein, 'r')
    ehout = open(ehfileout, 'w')

    #Starting at line #3 because CST file has 2 lines of header
    for i in xrange(3, num_lines+1): 
        lineE = linecache.getline(efilein, i)
        lineH = linecache.getline(hfilein, i)
        #print lineE.split()[0]
        #print lineH.split()[0]
        
        if lineE.split()[0] == lineH.split()[0]:
            #print 'yes'
            if lineE.split()[1]== lineH.split()[1]:
                #print 'yes'
                if lineE.split()[2]== lineH.split()[2]:
                    #print 'yes' 
                    
                    exreal = float(lineE.split()[3])*10**-6
                    eyreal = float(lineE.split()[4])*10**-6
                    ezreal = float(lineE.split()[5])*10**-6
        
                    hximag = lineH.split()[6]
                    hyimag = lineH.split()[7]
                    hzimag = lineH.split()[8]
        
                    ehout.write('%-20s %-20s %-20s %-20s %-20s %-20s\n' % (str(exreal), str(eyreal), str(ezreal), hximag, hyimag, hzimag))
        
    return num_lines
#==============================================================================
# This function combines E and H CST files, and keeps xyz info
#==============================================================================
def CSTcomboxyz(efilein, hfilein, ehfileout):

    num_lines = sum(1 for line in open(efilein))
    print num_lines
    #efin = open(efilein, 'r')
    ehout = open(ehfileout, 'w')

    for i in xrange(3, num_lines+1): #smaller file 2539203): 
        lineE = linecache.getline(efilein, i)
        lineH = linecache.getline(hfilein, i)
        #print lineE.split()[0]
        #print lineH.split()[0]
        
        if lineE.split()[0] == lineH.split()[0]:
            #print 'yes'
            if lineE.split()[1]== lineH.split()[1]:
                #print 'yes'
                if lineE.split()[2]== lineH.split()[2]:
                    #print 'yes' 
                    
                    x = lineE.split()[0]
                    y = lineE.split()[1]
                    z = lineE.split()[2]
                    
                    exreal = lineE.split()[3]
                    eyreal = lineE.split()[4]
                    ezreal = lineE.split()[5]
                    
                    hximag = lineH.split()[6]
                    hyimag = lineH.split()[7]
                    hzimag = lineH.split()[8]
                    
                    ehout.write('%-10s %-10s %-10s %-20s %-20s %-20s %-20s %-20s %-20s\n' % (x, y, z, exreal, eyreal, ezreal, hximag, hyimag, hzimag))               
    return num_lines


def reorderCST(EHcombofile, reorderedFile, filetype):
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Step 2: 
    #	Write Header info
    #	This info needs to be adjusted by hand
    reorder = open(reorderedFile, 'w')
    reorder.write('3DDynamic XYZ\n')
    if filetype == 'linac':      
        reorder.write('1300.341684\n')
        reorder.write('-4.6 4.6 46\n')
        reorder.write('-4.6 4.6 46\n')
        reorder.write('0.0 120.0 1200\n')
        
        print('linac')
        #Number of grid points in each dimension
        #These need to be adjusted by hand
        nx = 46 +1
        ny = 46 +1
        nz = 1200 +1
    
    elif filetype == 'gun':
        print('gun')
        #Number of grid points in each dimension
        #These need to be adjusted by hand
        reorder.write('1300.151204\n')
        reorder.write('-2.5 2.5 80\n')
        reorder.write('-2.5 2.5 80\n')
        reorder.write('0.0 23.271 376\n')
        
        nx = 80 +1
        ny = 80 +1
        nz = 376 +1
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Step 3: 
    #	Reorder E and H values
    numlines = sum(1 for line in open(EHcombofile))
    
    #Checking file size is correct
    if numlines != nx*ny*nz :
    	print('Not the right number of lines!',numlines, nx*ny*nz  )
    
    # This is the right order to convert from XYZ to ZYX format
    print(nx, ny, nz)
    dx = nx*ny
    dy = ny
    dz = 1
#==============================================================================
#     for k in xrange(0,nx):
#     	dlz = k*dz
#     
#     	for j in xrange(0, ny):
#     		dly = j*dy
#     
#     		for i in xrange(0,nz):
#     			dlx = i*dx
#==============================================================================
    for k in xrange(0,nx):
        dlz = k*dz

        for j in xrange(0, ny):
            dly = j*dy

            for i in xrange(0,nz):
               dlx = i*dx
               zline = dlx + dly + dlz + 1
               reorder.write(linecache.getline(EHcombofile, zline))

    reorder.close()
#==============================================================================
# testing functions
#==============================================================================
#==============================================================================
# num_lines_gun = CSTcombo('field_files/e3D_gun_Zheng.txt', 'field_files/h3D_gun_Zheng.txt', 'hold1.txt')
# #num_lines = CSTcomboxyz('field_files/e3D_gun_Zheng.txt', 'field_files/h3D_gun_Zheng.txt', 'test.txt')
# reorderCST('hold.txt', 'DriveGun_3D.txt', 'gun')
#==============================================================================

num_lines_linac = CSTcombo('field_files/e3d_LinacLargeMeshZheng.txt', 'field_files/h3d_LinacLargeMeshZheng.txt', 'hold2.txt')
#num_lines = CSTcomboxyz('field_files/e3d_LinacLargeMeshZheng.txt', 'field_files/h3d_LinacLargeMeshZheng.txt', 'test.txt')
reorderCST('hold2.txt', 'DriveLinac_3D_2.txt', 'linac')


#num_lines = sum(1 for line in open('DriveLinac3D_CosMinusSin.txt'))


















