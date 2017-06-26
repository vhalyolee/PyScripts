
# coding: utf-8

## Introduction to NumPy
## Plot a function

 


import numpy

from numpy import array, linspace, pi, sin
from numpy.random import randn
from numpy.fft import fft, fftfreq, fftshift
from matplotlib.pyplot import (axis, figure, grid, plot, semilogy, 
                               subplot, title, xlabel, ylabel)
#get_ipython().magic(u'matplotlib inline')



a = linspace(0, 2*pi, 21)

print a

# this creates an array from 0 to $2\pi$ with 21 values:

# In[ ]:

# Set the printout precision to only show 3 decimal values.
# get_ipython().magic(u'precision 3')


#precision 3
u'%.3f'

print a

b = sin(a)
print b


# We'd really like to plot these:

# In[ ]:

plot(a, b)


# Querying an Array
# -----------------
# 
# And someone might ask, where in this plot are the values of b greater than 0?

# In[ ]:

b >= 0


# This is a boolean mask array of True and False values.
# 
# We can put this into a variable:

# In[ ]:

mask = b >= 0


# and then we could even ask to plot the values where this condition holds over the top of the other plot (with red circle markers):

# In[ ]:

plot(a, b)
plot(a[mask], b[mask], 'ro')

