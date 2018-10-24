########################################################################
# Temperature Conversion Program: Program to convert temperatures.
#
# By: Jeremy Corner
# 
# I have neither given or recieved, nor have I tolerated others' use of
# unathourized aid.
#
########################################################################

# Definitions of temperature conversions
def tmpf2tmpc(temp):
    temp = (float(temp) - 32.0)*(5/9)
    return float(temp)
    '''Write a conversion program to go from temperature in Fahrenheit to Celsius'''


def tmpc2tmpf(temp):
    temp = float(temp) * (9/5) + 32
    return float(temp)

    '''Write a conversion program to go from temperature in Celsius to Fahrenheit'''


def tmpc2tmpk(temp):
    temp = float(temp) + 273
    return float(temp)

    '''Write a conversion program to go from temperature in Celsius to Kelvin'''


def tmpk2tmpc(temp):
    temp = float(temp) - 273
    return float(temp)

    '''Write a conversion program to go from temperature in Kelvin to Celsius'''


# Start of main program

# Get input from standard input, the temperature and unit must be separated by a space
temp, temp_unit = input("Enter a temperature with unit (e.g., 45 F): ").split()
out_unit = input("Enter the desired temperature unit (C, F, or K): ")

if (temp_unit == out_unit):
    out_unit = temp_unit
    print("Warning: No conversion needed due to no change in units")
elif (temp_unit != out_unit):
    if ((out_unit == 'C') & (temp_unit == 'F')):
           t = tmpf2tmpc(temp)
    elif ((out_unit == 'F') & (temp_unit == 'C')):
            t = tmpc2tmpf(temp)
    elif ((out_unit == 'K') & (temp_unit == 'C')):
            t = tmpc2tmpk(temp)
    elif ((out_unit == 'C') & (temp_unit == 'K')):
            t = tmpk2tmpc(temp)

# Output the values read in from standard input to standard output
print(temp, temp_unit)
print()
print(t ,out_unit)
