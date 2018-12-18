# -*- coding: utf-8 -*-
"""
Concrete Temperature Analysis Code
By: Thomas Robbins

This is code designed to analyze a csv file containing temperature data 
of curing concrete. Process to analysis this file is outlined in the 
comments throughout the code. (green text) 
"""
"""
These import important python libraries to perform the work in the code.
"""
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
"""
This section imports the csv file. Ensure that you are in the directory that 
contains the file, and input the file name listed below as "file_name" 
NOTE: The code is designed to skip the first 9 rows of the csv file. If the 
header size changes, change the length of skipped rows. 
"""
data = pd.read_csv('B582127B.csv', skiprows=range(1,9))
data[0:4]

