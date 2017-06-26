
# Stats with SciPy
# ================
# 
# In this exercise, we will try out some of the statistics functions in SciPy.

# Question 1
# ----------
# 
# Import `stats` from `scipy`, and look at its docstring to see what is available in the stats module.


from scipy import stats



# your code goes here


# Question 2
# ----------
# 
# Look at the docstring for the normal distribution:
# You'll notice it has these parameters:
# 
# `loc`:
#   This variable shifts the distribution left or right.
#   For a normal distribution, this is the mean.  It defaults to 0.
# 
# `scale`:
#    For a normal distribution, this is the standard deviation.


from scipy.stats import norm



# your code goes here


# Question 3
# ----------
# 
# Create a single plot of the pdf of a normal distribution with mean=0 and standard deviation ranging from 1 to 3.  Plot this on the range from -10 to 10.


x = linspace(-10,10, 1001)



# your code goes here


# Question 4
# ----------
# 
# Create a "frozen" normal distribution object with mean=20.0, and standard deviation=3


# your code goes here


# Question 5
# ----------
# 
# Plot this distribution's pdf and cdf side by side in two separate plots.


x = linspace(0, 40, 1001)



# your code goes here


# Question 6
# ----------
# 
# Get 5000 random variable samples from the distribution, and use the `stats.norm.fit` method to estimate its parameters. Plot the histogram of the random variables as well as the pdf for the estimated distribution.

# Hint: Try using `stats.histogram`. There is also `matplotlib.pyplot.hist` which makes life easier.


from scipy.stats import histogram
# Note that scipy.stats.histogram behaves differently from the
# numpy.histogram.



# your code goes here


# Copyright 2008-2016, Enthought, Inc.  
# Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.  
# http://www.enthought.com
