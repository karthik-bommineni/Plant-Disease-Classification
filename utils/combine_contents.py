# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 01:01:43 2023

@author: karth
"""

import os
import shutil

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == '__main__':
    
    train_path = 'C:\\Users\\karth\\OneDrive\\Desktop\\PlantDoc\\PlantDoc-Dataset\\train'
    test_path = 'C:\\Users\\karth\\OneDrive\\Desktop\\PlantDoc\\PlantDoc-Dataset\\test'
    
    train_dirs = os.listdir(train_path)
    test_dirs = os.listdir(test_path)
    
    print(train_dirs)
    print(test_dirs)