# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:04:15 2023

@author: mumta
"""

#3. Yeso 
#(Lat. -33.80, Lon. -70.21)


##########################################################glaceir_profile.csv

#Glacier Name: Rio Olivares

#column: Elevation, Area, WE, EleZone

#from the gl_tif(reclassify or contour, zonal geometry as table)

#Elevation: elevation of jun from min to max with 10m step 
#from gl_th_tif file (reclassify or contour, zonal geometry as table)
#Area: area per elevation band (elevation band area/catchment area)
#WE: thickness of ice at the elevation band


#EleZone: 100m elevation step


    
#glacier_profile_GIS.csv file is created manually
    
    
#reading excel file

import pandas as pd
import numpy as np


from pathlib import Path; home = str(Path.home())

#C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/5. matilda-maipo-final/1. Rio Olivares_GIS/8/Export_Output.txt
df = pd.read_csv(home + "/Desktop/Thesis/Modelling/Matlida/5. matilda-maipo-final/5. Upper Maipo 5701002/MAT/glacier_profile.csv")






elezone_interval = 100
def round_elezones(x, base=100):
    return base * round(x/base)

df["EleZone"] = round_elezones(df["Elevation"], base=elezone_interval)




#saving csv file to the dir
df.to_csv(r'C:\Users\mumta\Desktop\Thesis\Modelling\Matlida\5. matilda-maipo-final\5. Upper Maipo 5701002\MAT\glacier_profile.csv',index=False,  header=True)













Glacier_profile = df[['AREA', 'MEAN']]
Glacier_profile = Glacier_profile.rename(columns={'AREA': 'Area', 'MEAN': 'WE'})



Elevation_band = 10
def round_Elevation_band(x, base=10):
    return base * round(x/base)



Glacier_profile.insert(loc=0,column='Elevation', value = 3810)
Glacier_profile["Elevation"] = pd.Series(np.arange(3810,5732,10))






catchment_area = 21.4507
#converting area unit from m2 to km2 and fraction of glacier area
Glacier_profile["Area"] = Glacier_profile["Area"]/(catchment_area*1000000)

Glacier_profile["WE"] = Glacier_profile["WE"]*0.908*1000












































#C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/Rio Olivares/glacier_profile.csv
#C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/5. matilda-maipo-final/1. Rio Olivares_GIS/8/Export_Output.txt

# calculate the mean ice thickness per elevation band and write table
gis_thickness = "/Desktop/Thesis/Modelling/Matlida/Rio Olivares mHM2/glacier_profile_GIS.csv"

glacier_profile = pd.read_csv(home + gis_thickness)


catchment_area = 280
#catchment_area = 241.5



#converting area unit from m2 to km2
glacier_profile["Area"] = glacier_profile["Area"]/(catchment_area*1000000)

glacier_profile["WE"] = glacier_profile["WE"]*0.908*1000





#Saving file as csv
#glacier_profile.to_csv(r'C:\Users\mumta\Desktop\Thesis\Modelling\Matlida\matilda-master\Example Maipo\4. netcdf_ real_gl_pro\glacier_profile.csv',index=False,  header=True)
#glacier_profile.to_csv(output_path + "ice_thickness_profile_final.csv", index=False)

glacier_profile.to_csv(r'C:\Users\mumta\Desktop\Thesis\Modelling\Matlida\Rio Olivares mHM2\glacier_profile.csv',index=False,  header=True)





























mydir = 'C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/Gis Routine/Juncal/Txt/'



C1 = pd.read_excel(mydir + 'Jun_colP_1.xls', index_col=0) 


C1 = pd.read_csv(mydir+"glacier_profile.csv" )











min_elev = 3773
mean_elev = 4415
max_elev = 5648





df = pd.DataFrame(columns = ['Elevation', 'Area', 'WE', 'EleZone'])





