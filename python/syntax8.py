
#################################################
# Syntax8.py
# By: Jeremy Corner
#
# Code that will read an SOI file. Then find the 
# max and min values for each year, and print out
# the values.
#
#################################################

# Import files to allow for certain processes to happen.
import warnings
warnings.filterwarnings('ignore', 'numpy.dtype size changed')
import numpy as np
import pandas as pd

# Read in the text file we want to look at.
df_soi = pd.read_csv('/archive/data_kevin/met330/soi.txt', skiprows = 3, delim_whitespace=True)


# Find all the years in the file.
years = df_soi.YEAR.values
years = df_soi.values[:,0].astype('int')

# Find the max for each year in the soi data.
data = df_soi.values[:,1::].astype('float')
SOI_max = np.max(data, axis=1)

# Find the min for each year in the soi data.
data = df_soi.values[:,1::].astype('float')
SOI_min = np.min(data, axis=1)

# Print out the all the needed information.
max_and_min = (np.vstack((years ,SOI_max ,SOI_min)))
for i in range(max_and_min.shape[1]):
    print('Year:'+str(int(max_and_min[0,i])) +'  Max:'+str(max_and_min[1,i]) + '  Min:'+ str(max_and_min[2,i]))


