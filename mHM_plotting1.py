# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 13:55:23 2023

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



mydir = 'C:/Users/mumta/Desktop/Ubuntu_shared/output_b1_daily/'

df = pd.read_csv(mydir+"daily_discharge.out.csv" ,parse_dates=[0],header=0,index_col=0, )  #with missing data obs

#calibration whole time period
# Daily: KGE-  0.80, NSE- 0.70 (from mHM)

df['Qobs'].fillna(0, inplace=True)
print(r2_score(df['Qobs'], df['Qsim'], force_finite = False))     #R2 score of baseline model is 0.

Details_df = df.describe().transpose()


#################################monthly resampling

dfm = df.resample('M').mean()

#dfm['Qobs'].fillna(0, inplace=True)


print(r2_score(dfm['Qobs'], dfm['Qsim'], force_finite = False))     #R2 score of baseline model is 0.
print(he.evaluator(he.nse, dfm['Qobs'], dfm['Qsim'])) #NSE  -infinity to 1.0 (best is 1)
print(he.evaluator(he.kge, dfm['Qobs'], dfm['Qsim'])) #KGE  -infinity to 1.0 (best is 1)
#print(he.evaluator(he.rmse, df4['Qobs'], df4['Qsim'])) #RMSE






################################################################2011-2014
################################################################2015-2018

import pandas as pd
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score   
import hydroeval as he
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error



mydir1 = 'C:/Users/mumta/Desktop/Ubuntu Share/mHM Final/'

df1 = pd.read_csv(mydir1+"2011-14.csv" ,parse_dates=[0],header=0,index_col=0, )  #with missing data obs
Details_df1 = df1.describe().transpose()

df2 = pd.read_csv(mydir1+"2015-18.csv" ,parse_dates=[0],header=0,index_col=0, )  #with missing data obs
Details_df2 = df2.describe().transpose()



#calibration 2011-2014
# Daily: KGE-  0.70, NSE- 0.40 (from mHM)
df1['Qobs'].fillna(0, inplace=True)
print(r2_score(df1['Qobs'], df1['Qsim'], force_finite = False))     #R2 score of baseline model is 0.



#calibration 2011-2014
# Daily: KGE-  0.53, NSE- 0.15 (from mHM)
df2['Qobs'].fillna(0, inplace=True)
print(r2_score(df2['Qobs'], df2['Qsim'], force_finite = False))     #R2 score of baseline model is 0.


#plot in one 2011-2014 and 2016-18


df4 = df1['2012-01-01 23:00:00':'2014-12-31 23:00:00']
df8 = df2['2016-01-01 23:00:00':'2018-12-31 23:00:00']



#plot in one 2011-2014

fig = plt.figure(figsize=(10,3.5))
ax1 = fig.add_subplot(111)
ax1.plot(df4['Qobs'], 'r', label='Qobs')
ax1.plot(df4['Qsim'], 'b', label='Qsim')
ax1.legend()
ax1.set_title('Daily mHM Simulation for the period 2012-14 and 2016-18 ' )
#ax1.set_xlabel('Time')
ax1.set_ylabel('Discharge m3/s')
plt.tight_layout()


#plot in one 2015-2018

fig = plt.figure(figsize=(10,3.5))
ax1 = fig.add_subplot(111)
ax1.plot(df8['Qobs'], 'r', label='Qobs')
ax1.plot(df8['Qsim'], 'b', label='Qsim')
ax1.legend()
#ax1.set_title('Discharge ' )
ax1.set_xlabel('Time')
ax1.set_ylabel('Discharge m3/s')
plt.tight_layout()




########## merging both time


frames = [df4, df8]
df8y = pd.concat(frames)

########################         correlation seasonal

def select_season(inDF, season, year=None):
    fake_idx = inDF.index + pd.DateOffset(months=1)   # --> python starts counting with 0 !!!
    seasons = {'DJF':1,'MAM':2,'JJA':3,'SON':4}
    if year is None:
        resultDF = inDF.groupby([fake_idx.quarter]).get_group((seasons[season]))
    else:
        resultDF = inDF.groupby([fake_idx.year,fake_idx.quarter]).get_group((year,seasons[season]))
    return resultDF

#Maipo season: DJF Summer ,JJA Winter  , MAM Autumn ,SON  Spring 


#2011-18
summ = select_season(df8y,'DJF')
aut = select_season(df8y,'MAM')
win = select_season(df8y,'JJA')
spr = select_season(df8y,'SON')


#meta data
Details_summ = summ.describe().transpose()
Details_win = aut.describe().transpose()
Details_aut = win.describe().transpose()
Details_spr = spr.describe().transpose()

#corr
summ['Qobs'].corr(summ['Qsim']) 
win['Qobs'].corr(win['Qsim']) 
aut['Qobs'].corr(aut['Qsim']) 
spr['Qobs'].corr(spr['Qsim']) 







