

#######################################
# Syntax7.py
# By: Jeremy Corner
# 
# Code that will read in a temperature
# and convert it into Celsius and Kelvin,
# while also looking for a heat or cold 
# warning.
#
#######################################

# prompt for a temperature.

TMPF = input('What is the temperature in Fahrenheit?')

# convert to Celsius and Kelvin.

TMPC = (int(TMPF) - 32) *5/9
print('The temperature in Celsius is '+str(TMPC))

TMPK = TMPC + 273.15
print('The temperature in Kelvin is '+str(TMPK))

# set up logic statements to look for temperature warnings.

if (TMPC >= 35):
    print ('Heat Warning')
elif (TMPC < -5):
    print('Cold Warning')
