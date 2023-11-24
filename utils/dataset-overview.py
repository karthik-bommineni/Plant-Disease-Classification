# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 00:45:56 2023

@author: karthik
"""

import os
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    train_path = 'C:\\Users\\karth\\OneDrive\\Desktop\\PlantDoc\\PlantDoc-Dataset\\train'
    
    idxs = os.listdir(train_path)
    # print(idxs)
    
    y = []
    
    for i in range (0, len(idxs)):
        class_path = train_path + '\\' + idxs[i]
        y.append(len(os.listdir(class_path)))   
        
    # print(y)
    # fig, ax = plt.subplots()
    # width = 0.75
    
    #increasing the space between leaf classes
    plt.rcParams["figure.figsize"] = [11.50, 9.50]
    plt.rcParams["figure.autolayout"] = True
    
    plt.barh(idxs, y, color = "green")
    for index, value in enumerate(y):
        plt.text(value, index, str(value))
        
    #setting the x-label and y-label
    plt.xlabel('Leaf classes')
    plt.ylabel('Frequnecy of images')
    
    #setting the title
    plt.title('PLANTDOC DATASET')
    
    plt.savefig('dataset-overview-plantdoc.jpg')
    
    plt.show()