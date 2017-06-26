
# Interpolation
# =============
# 
# In this exercise, we will use some of the SciPy interpolation functions, to clean up some bad data. We will read a datafile, which has some invalid entries, which we will then fill with plausible interpolated results. We will then make a plot of the cleaned data, and as a bonus, will highlight the interpolated regions on the plot.

# Question 1
# ----------
# 
# Read the data in `ud667.csv`. Note that some of the values are -999.25, which is a special value for "Missing data".


from numpy import genfromtxt, empty, NaN



logs = genfromtxt('ud667.csv', names=True)


# Question 2
# ----------
# 
# Use the function `interp1d` in the `scipy.interpolate` module to fill in the "bad" regions (where the data is -999.25) of the VP data with data from the "good" areas in the logs.


from scipy.interpolate import interp1d



vp = logs['VP']

depth = logs['DEPTH']



good_mask = vp != -999.25



good_depth = depth[good_mask]

good_vp = vp[good_mask]



# Now find the depths where we want to interpolate.

interp_depth = depth[~good_mask]



# Create an "interpolator" object that interpolates from the 

# good values for depth and vp 

interpolator = interp1d(good_depth, good_vp, kind=3, bounds_error=False)



# Now, interpolate the new vp values in the areas we had -999.25.

interp_vp = interpolator(interp_depth)



# Combine the good original and the new interpolated values into

# one log.

cleaned_vp = vp.copy()

cleaned_vp[~good_mask] = interp_vp


# Question 3
# ----------
# 
# Create a plot of VP vs. DEPTH using the interpolated data.


plot(depth, cleaned_vp)

xlabel('depth')

ylabel('vp')

title('Interpolated Log')


# Question 4
# ----------
# 
# Bonus: Create another plot of VP vs DEPTH, but change the color
#  of the interpolated part of the data.


# Build another plot that shows the original and interpolated

# sections separately.



plot(depth, cleaned_vp, 'b')



# plot() skips NaN values without connecting the lines

cleaned_vp[good_mask] = NaN

plot(depth, cleaned_vp, 'r', lw=2, alpha=.8)


# Copyright 2008-2016, Enthought, Inc.  
# Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.  
# http://www.enthought.com
