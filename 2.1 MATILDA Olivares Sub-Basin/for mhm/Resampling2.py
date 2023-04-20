# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:02:30 2023

@author: mumta
"""

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt



mydir = 'C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/6. Thesis/1. Olivares/Camel/2015_2018/2016_2018_2023-02-25_22-34-38/'

#reading saved file from Prepro
df = pd.read_csv(mydir+"model_output_2016-2018.csv" , parse_dates=[0],header=0,index_col=0 ,)


df1 = df['Melt_total']/24

df2 = df1.resample('H').ffill()



#Saving file as csv
df2.to_csv(r'C:\Users\mumta\Desktop\Ubuntu Share\mhm_with_mat\1. olivares\mat melt\glacier_melt_in.txt',index=False,  header=False)



