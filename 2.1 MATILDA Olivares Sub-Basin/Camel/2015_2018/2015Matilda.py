"""MATILDA Package - Example Script:
    Demonstrates the MATILDA workflow using a 3y example dataset. Per default the script reads the input files from
    the directory the script is located in.
    When executed, the model runs twice:
    - The first part features the comprehensive matilda_simulation function.
    - The second part runs the individual steps in separate functions and shows optional arguments.
    The output is saved in the working directory in separate subdirectories for both runs.
"""

import os
import sys
import pandas as pd
from matilda.core import matilda_simulation, matilda_parameter, matilda_preproc, matilda_submodules, matilda_plots, matilda_save_output


#C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/5. matilda-maipo-final/1. Olivares 5706001/MAT1

mydir = "C:/Users/mumta/Desktop/Thesis/Modelling/Matlida/6. Thesis/1. Olivares/Camel/2015_2018/"


df = pd.read_csv(mydir+'forcing_data.csv' )
obs = pd.read_csv(mydir+'runoff_data.csv')
glacier_profile = pd.read_csv(mydir+'glacier_profile.csv')


Catchment_area = 541.55

#obs["Qobs"] = obs["Qobs"]*86400*1000/(Catchment_area*1000000)                 #changing unit of discharge from m3/s to mm/day

glacier_profile["Area"] = glacier_profile["Area"]/(Catchment_area*1000000)     #converting area unit from m2 to km2 and fraction of glacier area
glacier_profile["WE"] = glacier_profile["WE"]*0.908*1000                       #changing ice thicness into WE in mm

# lat = -33.49, area_cat = Catchment_area , area_glac = Glacier_area, 
# ele_dat = 3585, ele_glac = 4685.5, ele_cat = 3748,

## Quick model run:
output_matilda = matilda_simulation(df, obs=obs, output=mydir,
                                    set_up_start='2015-01-01', set_up_end='2015-12-31',  # Min. 1y recommended
                                    sim_start='2016-01-01', sim_end='2018-12-31',
                                    freq="D",  # Temporal resolution ("D", "M" or "Y")
                                    lat = -33.49, area_cat = Catchment_area , area_glac = 79.99, 
                                    ele_dat = 3043.5, ele_glac = 4673.5, ele_cat = 3748,
  
                                    # Optional:

                                   # 1. specify model parameters, e.g.
                                    CET=0,PCORR= 0.5, CFMAX_ice = 3,
                                   
                                    # For a list of model parameters and default values check the Parameters file

                                    # 2. Add glacier profile (see Readme) to account for glacier change:
                                    glacier_profile= glacier_profile,
                                    elev_rescaling=True,

                                    # 3. Include interactive plots:
                                    plot_type='all'	# If you receive errors relating to plotly either try a different plotly version or change plot_type to "print"
                                    )





