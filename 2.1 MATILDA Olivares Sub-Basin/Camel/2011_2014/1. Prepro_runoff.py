# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:01:40 2023

@author: mumta
"""

#1. Olivares 5706001
#(Lat. -33.49, Lon. -70.14)

#area covering:-33.49 to -33.06 and -70.25to -70.05
#-33.09375 -33.15625 -33.21875 -33.28125 -33.34375 -33.40625, -33.46875 
#-70.21875 -70.15625 -70.09375






#preprocessing netcdf file

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#############################################Creating runoff_data.csv file 

#Column: Date, Qobs

#Extracting Qobs Discharge from mrm_flux

data = Dataset(r'C:/Users/mumta/Desktop/Ubuntu_shared/output_b1_daily/mRM_Fluxes_States.nc')

#print(data)


print(data.variables.keys())

Dis_routed = data.variables['Qrouted']
print(Dis_routed)

time = data.variables['time']
print(time)
time_data = data.variables['time'][:]
print(time_data)


lat = data.variables['lat']
print(lat)
lat_data = data.variables['lat'][:]
print(lat_data)


lon = data.variables['lon']
print(lon)
lon_data = data.variables['lon'][:]
print(lon_data)





#lat, lon for the olivares basin outlet

lat_j = -33.49   
lon_j = -70.14     

#Selecting close one lat and lon of the selected point 

#Squared diff of lat and lon
sq_diff_lat = (lat_data - lat_j )**2
sq_diff_lon = (lon_data - lon_j )**2

#Identifiying the index of the min value for the lan and lon

min_index_lat = sq_diff_lat.argmin()
print(min_index_lat)


min_index_lon = sq_diff_lon.argmin()
print(min_index_lon)


#Creating an empty dataframe   

starting_date = data.variables['time'].units[11:23] #or '1950-01-01'
ending_date = '2020-12-31'


date_range = pd.date_range(start = starting_date, end = ending_date )
df = pd.DataFrame(0, columns = ['Qobs'], index = date_range)
df.index = df.index.date


dt = np.arange(0,data.variables['time'].size )


for time_index in dt:
    df.iloc[time_index] = Dis_routed[time_index, min_index_lat, min_index_lon ]



#plotting Qobs


fig = plt.figure(figsize=(8,3.5))
ax = fig.add_subplot(111)
ax.plot(df['Qobs'], 'r', label='Dischrage', linestyle = 'solid', linewidth = 2)
ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('Value (m3/s)')




# Extracting 5 year data 2015-2028


startdate0 = pd.to_datetime("2015-01-01").date()
enddate0 = pd.to_datetime("2018-12-31").date()
Qobs_5y = df.loc[startdate0:enddate0]

#plotting 2015-2020
fig = plt.figure(figsize=(8,3.5))
ax = fig.add_subplot(111)
ax.plot(Qobs_5y['Qobs'], 'r', label='Dischrage', linestyle = 'solid', linewidth = 2)
ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('Value (m3/s)')


Qobs_5y.index.name = 'Date'


#Saving file as csv
Qobs_5y.to_csv(r'C:\Users\mumta\Desktop\Thesis\Modelling\Matlida\6. Thesis\1. Olivares\runoff_data.csv',index=True,  header=True)








#changing unit of discharge from m3/s to mm/day

#catchment_area = 79.994
#Qobs_5y["Qobs"] = Qobs_5y["Qobs"]*86400*1000/(catchment_area*1000000)






