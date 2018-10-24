
###########################################################
#
# A script to make plots for various elements from a 
# station plot.
#
# By: Jeremy Corner
#
# I have neither given or recieved, nor have I tolerated
# others' use of unathourized aid.
#
###########################################################

# Import in numpy, panda, and matlib.
import warnings
warnings.filterwarnings('ignore', 'numpy.dtype size changed')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read in the data.
kvpz_data = pd.read_csv('/archive/data_kevin/met330/kvpz_20161006_surface.dat')

# Create plot for temp and dew point.
kvpz_temp = kvpz_data.TemperatureF.values
kvpz_time = kvpz_data.TimeCDT.values
kvpz_dew = kvpz_data.DewPointF.values

# Make the plot
plt.figure(1)
plt.plot((kvpz_time/100), kvpz_temp, color='red')
plt.plot((kvpz_time/100), kvpz_dew, color='green')
plt.xlabel('Time -UTC')
plt.ylabel('Temperature Degrees F')

# Adjust x label to look better
plt.xticks(range(0, 27, 3))

# Save figure 1
plt.savefig('kvpz_temps.png',dpi=150)

# Information for 2nd plot. MUST BE A BAR GRAPH!
kvpz_precip = kvpz_data.PrecipitationIn.values

# Making the bar graph
plt.figure(2)
plt.bar((kvpz_time/100), kvpz_precip)
plt.xlabel('Time -UTC')
plt.ylabel('Precipitation in Inches')
plt.xticks(range(0, 27, 3))


# Save figure 2
plt.savefig('kvpz_precip.png',dpi=150)

# Information for the 3rd plot. Back to the good ol' plot.
kvpz_wind = kvpz_data.WindSpeedMPH.values

# Making the 3rd plot
plt.figure(3)
plt.plot((kvpz_time/100), (kvpz_wind*0.868976))
plt.xlabel('Time -UTC')
plt.ylabel('Wind in Knots')
plt.xticks(range(0, 27, 3))

# Save figure 3
plt.savefig('kvpz_wind.png',dpi=150)


