# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 18:04:21 2023

@author: mumta
"""


import pandas as pd
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score   
import hydroeval as he
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

mydir1 = 'C:/Users/mumta/Desktop/Ubuntu Share/mHM Final/2011/'
mydir2 = 'C:/Users/mumta/Desktop/Ubuntu Share/mHM Final/2015/'

df1 = pd.read_csv(mydir1+"2011_mhm_meangis.csv" ,parse_dates=[0],header=0,index_col=0, )  #with missing data obs
df2 = pd.read_csv(mydir2+"2015_mhm_meangis.csv" ,parse_dates=[0],header=0,index_col=0, )  #with missing data obs


#merged
frames = [df1, df2]
df8 = pd.concat(frames)

Details = df8.describe().transpose()





fig = plt.figure(figsize=(10,6))
fig.suptitle(" Daily output from the mHM model in the period 2012-2018")
ax1 = fig.add_subplot(511)
ax2 = fig.add_subplot(512)
ax3 = fig.add_subplot(513)
ax4 = fig.add_subplot(514)
ax5 = fig.add_subplot(515)

ax1.plot(df8['aET'], 'black')
ax2.plot(df8['SM_Lall'], 'black')
ax3.plot(df8['snowpack'], 'black')
ax4.plot(df8['Qsm'], 'black')
ax5.plot(df8['unsatSTW'], 'black')


ax1.legend()
ax1.set_title(' Actual evapotranspiration ', fontsize=9)
#ax1.set_xlabel()
ax1.set_ylabel('[mm d-1]')

ax2.legend()
ax2.set_title('Soil moisture', fontsize=9)
#ax2.set_xlabel()
ax2.set_ylabel('[mm mm-1]')

ax3.legend()
ax3.set_title(' Depth of snowpack', fontsize=9)
#ax3.set_xlabel()
ax3.set_ylabel('[mm]')

ax4.legend()
ax4.set_title(' Snow melt', fontsize=9)
#ax4.set_xlabel()
ax4.set_ylabel('[mm d-1]')

ax5.legend()
ax5.set_title(' Unsaturated storage', fontsize=9)
#ax4.set_xlabel('Time')
ax5.set_ylabel('[mm]')

plt.tight_layout()



#########optional if u want individually for both time

df4 = df1['2012-01-01 23:00:00':'2014-12-31 23:00:00']


fig = plt.figure(figsize=(10,6))
fig.suptitle(" Daily output from the mHM model in the period 2012-2014")
ax1 = fig.add_subplot(511)
ax2 = fig.add_subplot(512)
ax3 = fig.add_subplot(513)
ax4 = fig.add_subplot(514)
ax5 = fig.add_subplot(515)

ax1.plot(df4['aET'], 'black')
ax2.plot(df4['SM_Lall'], 'black')
ax3.plot(df4['snowpack'], 'black')
ax4.plot(df4['Qsm'], 'black')
ax5.plot(df4['unsatSTW'], 'black')


ax1.legend()
ax1.set_title(' Actual evapotranspiration ', fontsize=9)
#ax1.set_xlabel()
ax1.set_ylabel('[mm d-1]')

ax2.legend()
ax2.set_title('Soil moisture', fontsize=9)
#ax2.set_xlabel()
ax2.set_ylabel('[mm mm-1]')

ax3.legend()
ax3.set_title(' Depth of snowpack', fontsize=9)
#ax3.set_xlabel()
ax3.set_ylabel('[mm]')

ax4.legend()
ax4.set_title(' Snow melt', fontsize=9)
#ax4.set_xlabel()
ax4.set_ylabel('[mm d-1]')

ax5.legend()
ax5.set_title(' Unsaturated storage', fontsize=9)
#ax4.set_xlabel('Time')
ax5.set_ylabel('[mm]')

plt.tight_layout()




##### 2015-18

df8 = df2['2016-01-01 23:00:00':'2018-12-31 23:00:00']



fig = plt.figure(figsize=(10,6))
fig.suptitle(" Daily output from the mHM model in the period 2015-2018")
ax1 = fig.add_subplot(511)
ax2 = fig.add_subplot(512)
ax3 = fig.add_subplot(513)
ax4 = fig.add_subplot(514)
ax5 = fig.add_subplot(515)

ax1.plot(df8['aET'], 'black')
ax2.plot(df8['SM_Lall'], 'black')
ax3.plot(df8['snowpack'], 'black')
ax4.plot(df8['Qsm'], 'black')
ax5.plot(df8['unsatSTW'], 'black')


ax1.legend()
ax1.set_title(' Actual evapotranspiration ', fontsize=9)
#ax1.set_xlabel()
ax1.set_ylabel('[mm d-1]')

ax2.legend()
ax2.set_title('Soil moisture', fontsize=9)
#ax2.set_xlabel()
ax2.set_ylabel('[mm mm-1]')

ax3.legend()
ax3.set_title(' Depth of snowpack', fontsize=9)
#ax3.set_xlabel()
ax3.set_ylabel('[mm]')

ax4.legend()
ax4.set_title(' Snow melt', fontsize=9)
#ax4.set_xlabel()
ax4.set_ylabel('[mm d-1]')

ax5.legend()
ax5.set_title(' Unsaturated storage', fontsize=9)
#ax4.set_xlabel('Time')
ax5.set_ylabel('[mm]')

plt.tight_layout()












