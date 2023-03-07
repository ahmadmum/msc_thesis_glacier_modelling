# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 00:16:20 2023

@author: mumta
"""

#hypsometry plot

# importing the required module
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path; home = str(Path.home())



df = "/Desktop/Thesis/Modelling/Matlida/1. Catchment/Plotting/Hyp/glacier_profile_GIS_Ice.csv"
df = pd.read_csv(home + df)


df["Area"] = df["Area"]/(1000000)
df["Area1"] = df["Area1"]/(1000000)
df["Area2"] = df["Area2"]/(1000000)
df["Area3"] = df["Area3"]/(1000000)
df["Area4"] = df["Area4"]/(1000000)
df["Area5"] = df["Area5"]/(1000000)


#Maipo Basin
# x axis values
x = df['Area']
# corresponding y axis values
y = df['Elevation']
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('Area km2')
# naming the y axis
plt.ylabel('Elevation')
  
# giving a title to my graph
plt.title('(f) Hypsometry Maipo Basin')
  
# function to show the plot
plt.show()



#Olivares
# x axis values
x = df['Area1']
# corresponding y axis values
y = df['Elevation1']
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('Area km2')
# naming the y axis
plt.ylabel('Elevation')
  
# giving a title to my graph
plt.title('(a) Hypsometry Olivares ')
  
# function to show the plot
plt.show()


#Colorado
# x axis values
x = df['Area2']
# corresponding y axis values
y = df['Elevation2']
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('Area km2')
# naming the y axis
plt.ylabel('Elevation')
  
# giving a title to my graph
plt.title('(b) Hypsometry Colorado ')
  
# function to show the plot
plt.show()



#Yeso
# x axis values
x = df['Area3']
# corresponding y axis values
y = df['Elevation3']
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('Area km2')
# naming the y axis
plt.ylabel('Elevation')
  
# giving a title to my graph
plt.title('(c) Hypsometry Yeso ')
  
# function to show the plot
plt.show()


#Volcan
# x axis values
x = df['Area4']
# corresponding y axis values
y = df['Elevation4']
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('Area km2')
# naming the y axis
plt.ylabel('Elevation')
  
# giving a title to my graph
plt.title('(d) Hypsometry Volcan ')
  
# function to show the plot
plt.show()





#Upper Maipo
# x axis values
x = df['Area5']
# corresponding y axis values
y = df['Elevation5']
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('Area km2')
# naming the y axis
plt.ylabel('Elevation')
  
# giving a title to my graph
plt.title('(e) Hypsometry Upper Maipo ')
  
# function to show the plot
plt.show()








fig = plt.figure(figsize=(10,18))
ax1 = fig.add_subplot(621)
ax2 = fig.add_subplot(622)
ax3 = fig.add_subplot(623)
ax4 = fig.add_subplot(624)
ax4 = fig.add_subplot(625)
ax4 = fig.add_subplot(626)

ay1 = fig.add_subplot(621)
ay2 = fig.add_subplot(622)
ay3 = fig.add_subplot(623)
ax4 = fig.add_subplot(624)
ax4 = fig.add_subplot(625)
ax4 = fig.add_subplot(626)



ax1.plot(df['Area'], df['Elevation4'] 'g', label='Forest', linestyle = 'solid', linewidth = 2)
ax1.plot(df3H_gb.index,df3H_gb['TA_P']['mean'], 'r', label='Pasture', linestyle = 'solid', linewidth = 2)

ax2.plot(df3H_gb.index,df3H_gb['RH_F']['mean'], 'r', label='Forest', linestyle = 'solid', linewidth = 2)
ax2.plot(df3H_gb.index,df3H_gb['RH_P']['mean'], 'b', label='Pasture', linestyle = 'solid', linewidth = 2)

ax3.plot(df3H_gb.index,df3H_gb['TS_F']['mean'], 'b', label='Forest', linestyle = 'solid', linewidth = 2)
ax3.plot(df3H_gb.index,df3H_gb['TS_P']['mean'], 'g', label='Pasture', linestyle = 'solid', linewidth = 2)

ax4.plot(df3H_gb.index,df3H_gb['SWC_F']['mean'], 'b', label='Forest', linestyle = 'solid', linewidth = 2)
ax4.plot(df3H_gb.index,df3H_gb['SWC_P']['mean'], 'g', label='Pasture', linestyle = 'solid', linewidth = 2)

ax3.plot(df3H_gb.index,df3H_gb['TS_F']['mean'], 'b', label='Forest', linestyle = 'solid', linewidth = 2)
ax3.plot(df3H_gb.index,df3H_gb['TS_P']['mean'], 'g', label='Pasture', linestyle = 'solid', linewidth = 2)

ax4.plot(df3H_gb.index,df3H_gb['SWC_F']['mean'], 'b', label='Forest', linestyle = 'solid', linewidth = 2)
ax4.plot(df3H_gb.index,df3H_gb['SWC_P']['mean'], 'g', label='Pasture', linestyle = 'solid', linewidth = 2)

ax1.legend()
ax1.set_title(' Air Temperature ', fontsize=15)
ax1.set_xlabel('Time')
ax1.set_ylabel('TA (degC)')

ax2.legend()
ax2.set_title('Relative Humidity', fontsize=15)
ax2.set_xlabel('Time')
ax2.set_ylabel('RH (%)')

ax3.legend()
ax3.set_title(' Soil Temperature', fontsize=15)
ax3.set_xlabel('Time')
ax3.set_ylabel('TS (degC)')

ax4.legend()
ax4.set_title(' Soil Water Content', fontsize=15)
ax4.set_xlabel('Time')
ax4.set_ylabel('SWC (%)')

ax3.legend()
ax3.set_title(' Soil Temperature', fontsize=15)
ax3.set_xlabel('Time')
ax3.set_ylabel('TS (degC)')

ax4.legend()
ax4.set_title(' Soil Water Content', fontsize=15)
ax4.set_xlabel('Time')
ax4.set_ylabel('SWC (%)')

plt.tight_layout()




























#all in one

# x axis values
x1 = df['Area1']
x2 = df['Area2']
x3 = df['Area3']
x4 = df['Area4']
x5 = df['Area5']

# corresponding y axis values

y1 = df['Elevation1']
y2 = df['Elevation2']
y3 = df['Elevation3']
y4 = df['Elevation4']
y5 = df['Elevation5']

# plotting the points
plt.plot(x1, y1, label = "line 1")
plt.plot(x2, y2, label = "line 1")
plt.plot(x3, y3, label = "line 1")
plt.plot(x4, y4, label = "line 1")
plt.plot(x5, y5, label = "line 1")

# naming the x axis
plt.x1label('Area')

# naming the y axis
plt.y2label('Elevation')


# giving a title to my graph
plt.title('Hypsometry')

# function to show the plot
plt.show()



















