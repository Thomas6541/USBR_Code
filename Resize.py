# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import PIL
import os
import os.path
from PIL import Image



f = r'C:\Users\tomro\OneDrive\Pictures\Tes_Two'

ratio = 0.3

for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    width, height = img.size
    resized = (int(width * ratio), int(height * ratio))
    img = img.resize(resized, Image.ANTIALIAS)
    img.save(f_img)
        
        

