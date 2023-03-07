# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:15:13 2023

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



########################################################2012-14

mydir = 'C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/6. Thesis/6. Maipo/camels/2. 2011_2014/2012_2014_2023-02-25_20-07-59/'

df = pd.read_csv(mydir+"model_output_2012-2014.csv" ,parse_dates=[0],header=0,index_col=0, )  #with missing data obs
Detailsdf = df.describe().transpose()


#yearly mean 
dfYm = df.resample('Y').mean()
DetailsdfYm = dfYm.describe().transpose()

#########################################################2016-18

mydir1 = 'C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/6. Thesis/6. Maipo/camels/3. 2015_2018/2016_2018_2023-02-25_20-08-50/'

df1 = pd.read_csv(mydir1+"model_output_2016-2018.csv" ,parse_dates=[0],header=0,index_col=0, ) 
Detailsdf1 = df1.describe().transpose()




#max available also in mat folder meta details


##################################################2011-18 HBV output

mydir2 = 'C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/6. Thesis/6. Maipo/camels/4. 2011_2018/2011_2018_2023-02-25_21-01-11/'

df2 = pd.read_csv(mydir2+"model_output_2011-2018.csv" ,parse_dates=[0],header=0,index_col=0, )  #with missing data obs
Detailsdf2 = df2.describe().transpose()





######################################sesonal analysis from 2012-14 and 2016-18



frames = [df, df1]
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
Details_win = win.describe().transpose()
Details_aut = aut.describe().transpose()
Details_spr = spr.describe().transpose()
