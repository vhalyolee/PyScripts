
# Interpolation
# =============
# 
# In this exercise, we will use some of the SciPy interpolation functions, to clean up some bad data. We will read a datafile, which has some invalid entries, which we will then fill with plausible interpolated results. We will then make a plot of the cleaned data, and as a bonus, will highlight the interpolated regions on the plot.

# Question 1
# ----------
# 
# Read the data in `ud667.csv`. Note that some of the values are -999.25, which is a special value for "Missing data".


from numpy import genfromtxt, empty, NaN



# your code goes here


# Question 2
# ----------
# 
# Use the function `interp1d` in the `scipy.interpolate` module to fill in the "bad" regions (where the data is -999.25) of the VP data with data from the "good" areas in the logs.


from scipy.interpolate import interp1d



# your code goes here


# Question 3
# ----------
# 
# Create a plot of VP vs. DEPTH using the interpolated data.


# your code goes here


# Question 4
# ----------
# 
# Bonus: Create another plot of VP vs DEPTH, but change the color
#  of the interpolated part of the data.


# your code goes here


# Copyright 2008-2016, Enthought, Inc.  
# Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.  
# http://www.enthought.com
