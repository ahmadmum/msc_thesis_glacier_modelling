

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:40:53 2023

@author: mumta
"""

#plotting

import pandas as pd
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

from sklearn.metrics import r2_score   
import hydroeval as he
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

#C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/1. Catchment/Plotting/mhm mat plotting

mydir = 'C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/1. Catchment/Plotting/mhm mat plotting/'

df = pd.read_csv(mydir+"obs_mhm_mhmmat 2009-18 - Copy.csv" ,parse_dates=[0],header=0,index_col=0, )  #with missing data obs
#df = pd.read_csv(mydir+"Discharge_copy1.csv" ,parse_dates=[0],header=0,index_col=0, )





df4 = df['2011-01-01 23:00:00':'2015-12-31 23:00:00']
df8 = df['2015-01-01 23:00:00':'2018-12-31 23:00:00']

Details_4 = df4.describe().transpose()
Details_8 = df8.describe().transpose()



#plot in one 2011-2014

fig = plt.figure(figsize=(10,3))
ax1 = fig.add_subplot(111)
ax1.plot(df4['Melt_total'], 'k', label='Melt', )
ax1.legend()
ax1.set_title('Olivares Total Melt ' )
#ax1.set_xlabel('Time')
ax1.set_ylabel('Total melt [mm]')
plt.tight_layout()



#plot in one 2015-2018

fig = plt.figure(figsize=(10,3))
ax1 = fig.add_subplot(111)
ax1.plot(df8['Melt_total'], 'k', label='Melt', )
ax1.legend()
#ax1.set_title(' ' )
ax1.set_xlabel('Time')
ax1.set_ylabel('Total melt [mm]')
plt.tight_layout()




###########################################################




#with Nan values
print(ma.corrcoef(ma.masked_invalid(df4['Qobs']), ma.masked_invalid(df4['Qmhm'])))
print(ma.corrcoef(ma.masked_invalid(df4['Qobs']), ma.masked_invalid(df4['Qmhm_mat'])))

print(ma.corrcoef(ma.masked_invalid(df8['Qobs']), ma.masked_invalid(df8['Qmhm'])))
print(ma.corrcoef(ma.masked_invalid(df8['Qobs']), ma.masked_invalid(df8['Qmhm_mat'])))


#Converting NAN values to 0
df4['Qobs'].fillna(0, inplace=True)
df8['Qobs'].fillna(0, inplace=True)


#2011-14
print(r2_score(df4['Qobs'], df4['Qmhm'], force_finite = False))     #R2 score of baseline model is 0.
print(he.evaluator(he.nse, df4['Qobs'], df4['Qmhm'])) #NSE  -infinity to 1.0 (best is 1)
print(he.evaluator(he.kge, df4['Qobs'], df4['Qmhm'])) #KGE  -infinity to 1.0 (best is 1)
#print(he.evaluator(he.rmse, df4['Qobs'], df4['Qsim'])) #RMSE

print(r2_score(df4['Qobs'], df4['Qmhm_mat'], force_finite = False))     #R2 score of baseline model is 0.
print(he.evaluator(he.nse, df4['Qobs'], df4['Qmhm_mat'])) #NSE  -infinity to 1.0 (best is 1)
print(he.evaluator(he.kge, df4['Qobs'], df4['Qmhm_mat'])) #KGE  -infinity to 1.0 (best is 1)
#print(he.evaluator(he.rmse, df4['Qobs'], df4['Qsim'])) #RMSE



#2015-18
print(r2_score(df8['Qobs'], df8['Qmhm'], force_finite = False))     #R2 score of baseline model is 0.
print(he.evaluator(he.nse, df8['Qobs'], df8['Qmhm'])) #NSE  -infinity to 1.0 (best is 1)
print(he.evaluator(he.kge, df8['Qobs'], df8['Qmhm'])) #KGE  -infinity to 1.0 (best is 1)
#print(he.evaluator(he.rmse, df4['Qobs'], df4['Qsim'])) #RMSE

print(r2_score(df8['Qobs'], df8['Qmhm_mat'], force_finite = False))     #R2 score of baseline model is 0.
print(he.evaluator(he.nse, df8['Qobs'], df8['Qmhm_mat'])) #NSE  -infinity to 1.0 (best is 1)
print(he.evaluator(he.kge, df8['Qobs'], df8['Qmhm_mat'])) #KGE  -infinity to 1.0 (best is 1)
#print(he.evaluator(he.rmse, df4['Qobs'], df4['Qsim'])) #RMSE


#################################monthly resampling

df4m = df4.resample('M').mean()
df8m = df8.resample('M').mean()

#monthly

#2011-14
print(r2_score(df4m['Qobs'], df4m['Qmhm'], force_finite = False))     #R2 score of baseline model is 0.
print(he.evaluator(he.nse, df4m['Qobs'], df4m['Qmhm'])) #NSE  -infinity to 1.0 (best is 1)
print(he.evaluator(he.kge, df4m['Qobs'], df4m['Qmhm'])) #KGE  -infinity to 1.0 (best is 1)
#print(he.evaluator(he.rmse, df4['Qobs'], df4['Qsim'])) #RMSE

print(r2_score(df4m['Qobs'], df4m['Qmhm_mat'], force_finite = False))     #R2 score of baseline model is 0.
print(he.evaluator(he.nse, df4m['Qobs'], df4m['Qmhm_mat'])) #NSE  -infinity to 1.0 (best is 1)
print(he.evaluator(he.kge, df4m['Qobs'], df4m['Qmhm_mat'])) #KGE  -infinity to 1.0 (best is 1)
#print(he.evaluator(he.rmse, df4['Qobs'], df4['Qsim'])) #RMSE



#2015-18
print(r2_score(df8m['Qobs'], df8m['Qmhm'], force_finite = False))     #R2 score of baseline model is 0.
print(he.evaluator(he.nse, df8m['Qobs'], df8m['Qmhm'])) #NSE  -infinity to 1.0 (best is 1)
print(he.evaluator(he.kge, df8m['Qobs'], df8m['Qmhm'])) #KGE  -infinity to 1.0 (best is 1)
#print(he.evaluator(he.rmse, df4['Qobs'], df4['Qsim'])) #RMSE

print(r2_score(df8m['Qobs'], df8m['Qmhm_mat'], force_finite = False))     #R2 score of baseline model is 0.
print(he.evaluator(he.nse, df8m['Qobs'], df8m['Qmhm_mat'])) #NSE  -infinity to 1.0 (best is 1)
print(he.evaluator(he.kge, df8m['Qobs'], df8m['Qmhm_mat'])) #KGE  -infinity to 1.0 (best is 1)
#print(he.evaluator(he.rmse, df4['Qobs'], df4['Qsim'])) #RMSE




############################# correlation seasonal

df8y = df['2011-01-01 23:00:00':'2018-12-31 23:00:00']



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
Details_summ = df8y.describe().transpose()
Details_win = df8y.describe().transpose()
Details_aut = df8y.describe().transpose()
Details_spr = df8y.describe().transpose()

#corr
summ['Qobs'].corr(summ['Qmhm']) 
summ['Qobs'].corr(summ['Qmhm_mat']) 
win['Qobs'].corr(win['Qmhm']) 
win['Qobs'].corr(win['Qmhm_mat']) 
aut['Qobs'].corr(aut['Qmhm']) 
aut['Qobs'].corr(aut['Qmhm_mat']) 
spr['Qobs'].corr(spr['Qmhm']) 
spr['Qobs'].corr(spr['Qmhm_mat']) 






