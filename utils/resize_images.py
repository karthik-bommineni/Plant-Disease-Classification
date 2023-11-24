# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 23:21:05 2023

@author: karth
"""

import os
import matplotlib.image as mpimg
import cv2

if __name__ == '__main__':
    inp_dir = 'C:\\Users\\karth\\OneDrive\\Desktop\\PlantVillage-color\\Dataset-color'
    
    target_size = (224, 224)
    
    print(os.listdir(inp_dir))
    
    for folder in os.listdir(inp_dir):
        
        folder_path = os.path.join(inp_dir, folder)
        if os.path.isdir(folder_path):
            print(f'Processing images in the folder: {folder}')
            for filename in os.listdir(folder_path):
                if filename.endswith(('.jpg', '.jpeg', '.png', '.JPG')):
                    
                    #load the img
                    img_path = os.path.join(folder_path, filename)
                    img = mpimg.imread(img_path)
                    
                    #resizing
                    resized_img = cv2.resize(img, target_size)
                    
                    #overwriting the input images with the resized images
                    mpimg.imsave(img_path, resized_img)
                
                
    print('Done with Resizing')
    