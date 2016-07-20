# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:41:19 2016

@author: Timofey
"""
import os
from scipy.misc import imread, imsave, imresize
print "Please make a copy of your dataset if you will need the unresized one in future.This program does not create a new dataset of resized images, it simply edites a given one."
dir = raw_input("Enter a directory of an image dataset: ")
w = int(raw_input("Enter a new width: "))
l = int(raw_input("Enter a new length: "))
print("Scaling the images, please wait...")
for image in os.listdir(dir):
    img = imread(dir+"/"+image)
    img_resized = imresize(img, (l, w))
    imsave(dir+"/"+image, img_resized)
print("Your dataset has been scaled.")
