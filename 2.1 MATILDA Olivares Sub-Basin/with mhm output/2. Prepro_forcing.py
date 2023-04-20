# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 09:58:30 2023

@author: mumta
"""

#1. Olivares 5706001
#(Lat. -33.49, Lon. -70.14)



##########################################################forcing_data.csv

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#column: TIMESTAMP, T2, RR


#######################################extracting temp(T2) from tavg.nc

data1 = Dataset(r'C:/Users/mumta/Desktop/Thesis/Input Data/Meteo/5710001/meteo_era5/meteo_1950_2020_day/tavg.nc')
print(data1.variables.keys())





Temp_avg = data1.variables['tavg']
print(Temp_avg)

time1 = data1.variables['time']
print(time1)
time_data1 = data1.variables['time'][:]
print(time_data1)

lat1 = data1.variables['lat']
print(lat1)
lat_data1 = data1.variables['lat'][:]
print(lat_data1)


lon1 = data1.variables['lon']
print(lon1)

lon_data1 = data1.variables['lon'][:]
print(lon_data1)


#lat, lon for the lower point of the glacier (choosen one if manual:  -33.375, -70.125)


lat_j1 = -33.49 
lon_j1 = -70.14

#Squared diff of lat and lon
sq_diff_lat1 = (lat_data1 - lat_j1 )**2
sq_diff_lon1 = (lon_data1 - lon_j1 )**2

#Identifiying the index of the min value for the lan and lon

min_index_lat1 = sq_diff_lat1.argmin()
print(min_index_lat1)

min_index_lon1 = sq_diff_lon1.argmin()
print(min_index_lon1)


#Creating an empty dataframe   

starting_date1 = '1950-01-01'   #data1.variables['time'].units[11:23] #or '1950-01-01'
ending_date1 = '2020-12-31'


date_range1 = pd.date_range(start = starting_date1, end = ending_date1 )
df1 = pd.DataFrame(0, columns = ['T2'], index = date_range1)
df1.index = df1.index.date


dt1 = np.arange(0,data1.variables['time'].size )


for time_index in dt1:
    df1.iloc[time_index] = Temp_avg[time_index, min_index_lat1, min_index_lon1 ]


Details_1 = df1.describe().transpose()

#plotting Tavg

fig = plt.figure(figsize=(8,3.5))
ax = fig.add_subplot(111)
ax.plot(df1['T2'], 'r', label='Temp', linestyle = 'solid', linewidth = 2)
ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('C')



# Extracting 5 year data 2015-2020

startdate1 = pd.to_datetime("2015-01-01").date()
enddate1 = pd.to_datetime("2018-12-31").date()
Tavg_5y = df1.loc[startdate1:enddate1]



#plotting 2015-2020
fig = plt.figure(figsize=(8,3.5))
ax = fig.add_subplot(111)
ax.plot(Tavg_5y['T2'], 'r', label='Temp', linestyle = 'solid', linewidth = 2)
ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('C')


Tavg_5y.index.name = 'TIMESTAMP'





#####################################################extracting pre from pre.nc
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data2 = Dataset(r'C:/Users/mumta/Desktop/Thesis/Input Data/Meteo/5710001/meteo_era5/meteo_1950_2020_day/pre.nc')


print(data2.variables.keys())


Preci = data2.variables['pre']
print(Preci)

time2 = data2.variables['time']
print(time2)
time_data2 = data2.variables['time'][:]
print(time_data2)


lat2 = data2.variables['lat']
print(lat2)
lat_data2 = data2.variables['lat'][:]
print(lat_data2)


lon2 = data2.variables['lon']
print(lon2)
lon_data2 = data2.variables['lon'][:]
print(lon_data2)


#lat, lon for the lower point of the glacier (choosen one if manual:  -33.375, -70.125)

lat_j2 = -33.49 
lon_j2 = -70.14

#Squared diff of lat and lon
sq_diff_lat2 = (lat_data2 - lat_j2 )**2
sq_diff_lon2 = (lon_data2 - lon_j2 )**2

#Identifiying the index of the min value for the lan and lon

min_index_lat2 = sq_diff_lat2.argmin()
print(min_index_lat2)

min_index_lon2 = sq_diff_lon2.argmin()
print(min_index_lon2)
#Creating an empty dataframe   

starting_date2 = '1950-01-01'  #data2.variables['time'].units[11:23] #or 
ending_date2 = '2020-12-31'


date_range2 = pd.date_range(start = starting_date2, end = ending_date2 )
df2 = pd.DataFrame(0, columns = ['RRR'], index = date_range2)
df2.index = df2.index.date


dt2 = np.arange(0,data2.variables['time'].size )


for time_index in dt2:
    df2.iloc[time_index] = Preci[time_index, min_index_lat2, min_index_lon2 ]



#plotting Tavg

fig = plt.figure(figsize=(8,3.5))
ax = fig.add_subplot(111)
ax.plot(df2['RRR'], 'r', label='Preci', linestyle = 'solid', linewidth = 2)
ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('mm')



Details_d = df2.describe().transpose()

# Extracting 5 year data 2015-2020

startdate2 = pd.to_datetime("2015-01-01").date()
enddate2 = pd.to_datetime("2018-12-31").date()
RRR_5y = df2.loc[startdate2:enddate2]

RRR_5y.index.name = 'TIMESTAMP'

#plotting 2015-2020
fig = plt.figure(figsize=(8,3.5))
ax = fig.add_subplot(111)
ax.plot(RRR_5y['RRR'], 'r', label='Preci', linestyle = 'solid', linewidth = 2)
ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('mm')




####################################################extracting pet from pet.nc
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data3 = Dataset(r'C:/Users/mumta/Desktop/Thesis/Input Data/Meteo/5710001/meteo_era5/meteo_1950_2020_day/pet.nc')

print(data3.variables.keys())


Evapo = data3.variables['pet']
print(Evapo)

time3 = data3.variables['time']
print(time3)
time_data3 = data3.variables['time'][:]
print(time_data3)


lat3 = data3.variables['lat']
print(lat3)
lat_data3 = data3.variables['lat'][:]
print(lat_data3)


lon3 = data3.variables['lon']
print(lon3)
lon_data3 = data3.variables['lon'][:]
print(lon_data3)


#lat, lon for the lower point of the glacier (choosen one if manual:  -33.375, -70.125)

lat_j3 = -33.49 
lon_j3 = -70.14


#Squared diff of lat and lon
sq_diff_lat3 = (lat_data3 - lat_j3 )**2
sq_diff_lon3 = (lon_data3 - lon_j3 )**2

#Identifiying the index of the min value for the lan and lon

min_index_lat3 = sq_diff_lat3.argmin()
print(min_index_lat3)

min_index_lon3 = sq_diff_lon3.argmin()
print(min_index_lon3)
#Creating an empty dataframe   

starting_date3 = '1950-01-01'  #data2.variables['time'].units[11:23] #or 
ending_date3 = '2020-12-31'


date_range3 = pd.date_range(start = starting_date3, end = ending_date3 )
df3 = pd.DataFrame(0, columns = ['PE'], index = date_range3)
df3.index = df3.index.date


dt3 = np.arange(0,data3.variables['time'].size )


for time_index in dt3:
    df3.iloc[time_index] = Evapo[time_index, min_index_lat3, min_index_lon3 ]



#plotting Tavg

fig = plt.figure(figsize=(8,3.5))
ax = fig.add_subplot(111)
ax.plot(df3['PE'], 'r', label='Evapo', linestyle = 'solid', linewidth = 2)
ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('mm')



# Extracting 5 year data 2015-2020

startdate3 = pd.to_datetime("2015-01-01").date()
enddate3 = pd.to_datetime("2018-12-31").date()
PE_5y = df3.loc[startdate3:enddate3]



PE_5y.index.name = 'TIMESTAMP'

#plotting 2015-2020
fig = plt.figure(figsize=(8,3.5))
ax = fig.add_subplot(111)
ax.plot(PE_5y['PE'], 'r', label='Evapo', linestyle = 'solid', linewidth = 2)
ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('mm')




#Combining temp, precipitation and evapo in one file

df_all = pd.concat([Tavg_5y,RRR_5y,PE_5y], axis=1)

#Saving file as csv
df_all.to_csv(r'C:\Users\mumta\Desktop\Thesis\Modelling\Matlida\6. Thesis\1. Olivares\forcing_data.csv',index=True,  header=True)















