# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:22:45 2022

@author: tomro
"""

import PIL
import os
import os.path
from PIL import Image




f = r'C:\Users\tomro\OneDrive\Pictures\Python_Code_Pics'

ratio = 0.5

for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    width, height = img.size
    resized = (int(width * ratio), int(height * ratio))
    img = img.resize(resized, Image.ANTIALIAS)
    img.save(f_img)
        