# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pathlib import Path; home = str(Path.home())
import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pysheds.grid import Grid
import fiona
import geopandas as gpd
import subprocess
import warnings
warnings.filterwarnings('ignore')


working_directory = home + "/Desktop/Thesis/Modelling/Matlida/Gis Routine/"

#C:/Users/mumta/Desktop/Thesis/Input Data/Meteo/5710001/morph/dem.asc

input_DEM = home + "/Desktop/Thesis/Modelling/Matlida/Gis Routine/pyr_tiff/pyr_ext1.tif"
#RGI_files = home + "/Desktop/Thesis/Modelling/Matlida/Gis Routine/Mount_glac_shp/glims_polygons.shp"
ice_thickness_files = home + "/Desktop/Thesis/Modelling/Matlida/Gis Routine/"










x, y = -70.50, -34.50 # pouring point  -33.5641325,-69.8914745

ele_bands, ele_zones = 20, 100


output_path = home + "/Desktop/Thesis/Modelling/Matlida/Gis Routine/Output/"


#Define a function to plot the digital elevation model
#def plotFigure(data, label, cmap='Blues'):
    #plt.figure(figsize=(12,10))
    #plt.imshow(data, extent=grid.extent)
    #plt.colorbar(label=label)
    #plt.grid()


## Catchment delineation with pysheds
# https://github.com/mdbartos/pysheds


# Plot the DEM
grid = Grid.from_raster(input_DEM, data_name='dem')
dem = grid.read_raster(input_DEM)
grid.view('input_DEM')  ########################################## got error
print(grid.crs)




# Condition DEM
# ----------------------
# Fill pits in DEM
pit_filled_dem = grid.fill_pits(dem)
# Fill depressions in DEM
flooded_dem = grid.fill_depressions(pit_filled_dem)
# Resolve flats in DEM
inflated_dem = grid.resolve_flats(flooded_dem)



# Specify directional mapping
dirmap = (64, 128, 1, 2, 4, 8, 16, 32)

# Compute flow directions
fdir = grid.flowdir(inflated_dem, dirmap=dirmap)



# Calculate flow accumulation
# --------------------------
acc = grid.accumulation(fdir, dirmap=dirmap)

# Delineate the catchment based on the pouring point  (delinate catchment by shape file)
x_snap, y_snap = grid.snap_to_mask(acc > 1000, (x, y))

# Delineate the catchment
catch = grid.catchment(x=x_snap, y=y_snap, fdir=fdir, dirmap=dirmap, 
                       xytype='coordinate')



###########################################catchment_dem
# Crop and plot the catchment
# ---------------------------
# Clip the bounding box to the catchment
grid.clip_to(catch)
clipped_catch = grid.view(catch)

# Plot the catchment
fig, ax = plt.subplots(figsize=(8,6))
fig.patch.set_alpha(0)

plt.grid('on', zorder=0)
im = ax.imshow(np.where(clipped_catch, clipped_catch, np.nan), extent=grid.extent,
               zorder=1, cmap='Greys_r')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Delineated Catchment', size=14)


# save as clipped TIF
grid.to_raster(clipped_catch, output_path + "catchment_DEM.tif")



#########################################catchment_shp
# Create shapefile and save it
shapes = grid.polygonize()

schema = {
    'geometry': 'Polygon',
    'properties': {'LABEL': 'float:16'}
}

with fiona.open(output_path + "catchment_shapefile.shp", 'w',
                driver='ESRI Shapefile',
                crs=grid.crs.srs,
                schema=schema) as c:
    i = 0
    for shape, value in shapes:
        rec = {}
        rec['geometry'] = shape
        rec['properties'] = {'LABEL' : str(value)}
        rec['id'] = str(i)
        c.write(rec)
        i += 1
c.close()

print("Mean catchment elevation is " + str(np.nanmean(clipped_catch)) + " m")

##############################################Glacier_dem
## Cutting all glaciers within the catchment from the RGI shapefile
rgi_shapefile = gpd.GeoDataFrame.from_file(RGI_files)
catchment_shapefile = gpd.GeoDataFrame.from_file(output_path + "catchment_shapefile.shp")

glaciers_catchment = gpd.overlay(rgi_shapefile, catchment_shapefile, how='intersection')
fig, ax = plt.subplots(1, 1)
base = catchment_shapefile.plot(color='white', edgecolor='black')
glaciers_catchment.plot(ax=base, column="RGIId", legend=True)
plt.show()


###################102




## Copy/get ice thickness files for each glacier


























