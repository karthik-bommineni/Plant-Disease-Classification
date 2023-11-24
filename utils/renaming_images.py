# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:04:10 2023

@author: karth
"""

import os


if __name__ == '__main__':
    
    inp_dir = 'C:\\Users\\karth\\OneDrive\\Desktop\\PlantVillage-color\\Dataset-color'
    
    print(len(os.listdir(inp_dir)))
    
    for folder in os.listdir(inp_dir):
        
        folder_path = os.path.join(inp_dir, folder)
        if os.path.isdir(folder_path):
            print(f'Renaming images in the folder: {folder}')
            
            for filename in os.listdir(folder_path):
                if filename.endswith(('.JPG')):
                    old_path = os.path.join(folder_path, filename)
                    new_path = os.path.join(folder_path, filename.lower())
                    os.replace(old_path, new_path)
                    print(f'Rename: {filename} to {filename.lower()}')
                    
                    
                    
    print('Done with renaming')