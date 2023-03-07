# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:23:01 2023

@author: mumta
"""
import pandas as pd
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt



#C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/6. Thesis/1. Olivares/Camel/2010_2018/2011_2018_2023-02-26_07-37-44

mydir = 'C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/6. Thesis/1. Olivares/Camel/2008_2018/2009_2018_2023-02-26_09-04-17/'

#reading saved file from Prepro
df = pd.read_csv(mydir+"model_output_2009-2018.csv" , parse_dates=[0],header=0,index_col=0 ,)

df1 = df['Melt_total']/24

df1 = df1.resample('H').ffill()



#Saving file as csv
df1.to_csv(r'C:\Users\mumta\Desktop\Ubuntu Share\mhm_with_mat\1. Olivares\2009-18\glacier_melt_in.txt',index=False,  header=False)


#Add last daily values 23 more times


fig = plt.figure(figsize=(10,3))
ax1 = fig.add_subplot(111)
ax1.plot(df1['Melt_total'], 'k', label='Melt', )
ax1.legend()
ax1.set_title('Olivares Total Melt ' )
#ax1.set_xlabel('Time')
ax1.set_ylabel('Total melt [mm]')
plt.tight_layout()
