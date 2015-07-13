# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:20:02 2015

@author: keriambermudez

"""
from skimage import io, measure, exposure, util
import mahotas
from scipy import ndimage
import numpy as np
import os
from  matplotlib import pyplot as plt
path = 'F:\\David_Fenyos\\Image_Analysis\\General_measurements\\Testing_Jacob\\Bleomycyn\\'

for root, dirs, files in os.walk(path):
     for folder in dirs:
        directory = path + folder + '\\'

        #green image

        green_mask = directory + 'srm_image_green_mask.tif'
        green_mask = io.imread(green_mask)
        
        green_tif =  directory+ 'srm_image_green.tif'
        green_tif = io.imread(green_tif)
        
        green_binary = green_mask ==0
        green_tif[green_binary]=0
        io.imsave(directory+'masked_green.tif',green_tif.astype('uint8'))
        #red 
        red_mask = directory + 'srm_image_red_mask.tif'
        red_mask = io.imread(red_mask)
        
        red_tif =  directory+ 'srm_image_red.tif'
        red_tif = io.imread(red_tif)
        
        red_binary = red_mask ==0
        red_tif[red_binary]=0
        io.imsave(directory+'masked_red.tif',red_tif.astype('uint8'))