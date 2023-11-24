# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:42:38 2023

@author: karth
"""

import os

if __name__ == '__main__':
    
    inp_dir = 'C:\\Users\\karth\\OneDrive\\Desktop\\PlantVillage-color\\Dataset-color'
    
    print(len(os.listdir(inp_dir)))
    
    for folder in os.listdir(inp_dir):
        
        folder_path = os.path.join(inp_dir, folder)
        if os.path.isdir(folder_path):
            
            for filename in os.listdir(folder_path):
                if ' ' in filename:
                    new_filename = filename.replace(' ', '_')
                    old_path = os.path.join(folder_path, filename)
                    new_path = os.path.join(folder_path, new_filename)
                    os.replace(old_path, new_path)
                    print(f'Rename: {filename} to {filename.lower()}')
                    
                    
                    
    print('Done with removing the spaces')