# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:50:10 2017

@author: nneveu

Re-order and combine 3D linac files from CST
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
    ehout.write('3DDynamic XYZ\n')
    ehout.write('1300.00\n')
    ehout.write('-4.6 4.6 46\n')
    ehout.write('-4.6 4.6 46\n')
    ehout.write('0.0 120.0 1200\n')
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
#==============================================================================
# testing functions
#==============================================================================
num_lines = CSTcombo('field_files/e3d_LinacLargeMeshZheng.txt', 'field_files/h3d_LinacLargMeshZheng.txt', 'DriveLinac_3D.txt')
#num_lines = CSTcomboxyz('field_files/e3D_gun_Zheng.txt', 'field_files/h3D_gun_Zheng.txt', 'test.txt')

#num_lines = sum(1 for line in open('DriveLinac3D_CosMinusSin.txt'))


















