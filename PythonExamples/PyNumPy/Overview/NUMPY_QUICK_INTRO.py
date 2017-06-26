
# coding: utf-8

# # Introduction to NumPy

# In[21]:

# Imports required but not shown in the video lecture.


import numpy

from numpy import array, linspace, pi, sin
from numpy.random import randn
from numpy.fft import fft, fftfreq, fftshift
from matplotlib.pyplot import (axis, figure, grid, plot, semilogy, 
                               subplot, title, xlabel, ylabel)
get_ipython().magic(u'matplotlib inline')


# In[15]:

print numpy.__version__


# This quick tour reviews a few of the defining features of NumPy arrays as motivation for where they might fit into your day-to-day needs.  
# 
# Mathematical Operations
# -----------------------
# 
# By now, we're pretty use to lists being the workhorse sequential data structure in Python.  It's great for many things, but it turns out that another data structure, the NumPy array, provides a different set of functionality that is really useful -- especially for numeric computations.
# 
# Here we start with a list, and illustrate the difference in syntax for mathematical operations on a list and an array.
# 
# Imagine you want to add 1 to every element in a sequence.  Here is a comparison between doing this with an array 
# and a list.
# 
# Let's look at a list

# In[16]:

a = [1, 2, 3, 4]
a


# If you add 1 to a list, you get an error because you can't add list and int types.

# In[17]:

a+1


# This will work, but it is a bit cryptic to the uninitiated:

# In[18]:

[val + 1 for val in a]


# But if we convert `a` to a NumPy `array`, then it does work:

# In[19]:

a = array(a)
a+1


# This is the first thing that the array provides: when you perform a mathematical operation on an array, the operation is performed on every element of the array.  So the result is 1+1 is 2, 2+1 is 3, 3+1 is 4 and 4+1 is 5.
# 
# Operations on two Arrays
# ------------------------
# 
# NumPy always carries out element-by-element operations when operating on two arrays.  Here are several examples with `+`,`*`, and `**` operators.
# 
# Let's create another array `b`:

# In[20]:

b = array([2, 3, 4, 5])


# They both have 4 elements.  If we add a and b:

# In[9]:

a + b


# then the operation is performed element-by-element: 1+2 is 3, 2+3 is 5, 3+4 is 7 and 4+5 is 9.
# 
# This doesn't just work for addition.  You can multiply:

# In[10]:

a*b


# You can exponentiate:

# In[11]:

a**b


# All operations are performed element-by-element.
# 
# Selecting Elements from an Array
# --------------------------------
# 
# You can index arrays like lists:

# In[12]:

a[0]


# You can also slice:

# In[ ]:

a[:2]


# In[ ]:

a[-2:]


# You could even take the first 2 and add to the last 2:

# In[13]:

a[:2] + a[-2:]


# Multi-dimensional Arrays
# ------------------------
# 
# Arrays can have more than one dimension.  Here we reshape the `a` array so that it has a two rows and two columns
# 
# Arrays have a `shape`:

# In[ ]:

a.shape


# and we can change its shape on the fly:

# In[ ]:

a.shape = (2, 2)
a


# and now `a` is a 2-by-2 array.
# 
# If you multiply a by itself:

# In[ ]:

a*a


# Notice that mathematical operations, even on a 2D array, are element-by-element operations.  `*` is not overloaded to mean matrix multiplication.  In this way, all operations are always consistent, no matter what dimensionality the arrays are. (There is a `numpy.matrix` object if you want the matrix operation behavior.)
# 
# Plotting
# --------
# 
# NumPy and matplotlib combine to providing a nice toolset for calculations and visualizations of your data.
# 
# Let's create another array with `linspace`:

# In[ ]:

a = linspace(0, 2*pi, 21)


# this creates an array from 0 to $2\pi$ with 21 values:

# In[ ]:

# Set the printout precision to only show 3 decimal values.
get_ipython().magic(u'precision 3')


# In[ ]:

a


# I can then say:

# In[ ]:

b = sin(a)
b


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


# This should give you an idea of the sorts of things you can do.
# 
# A More Complex Example
# ----------------------
# 
# Let's do a more involved example.  First we create a slightly noisy 5 Hz signal which is 3 seconds long with 1001 samples:

# In[ ]:

T= 3.0
N = 1001

t = linspace(0, T, N)
y = sin(5*t*2*pi) + 0.2 * randn(N)


# Now let's find the frequency content of the signal:

# In[ ]:

F = fftfreq(N, T/N)
Y = fft(y)
P = (abs(Y)/N)**2


# And then display the signal and its frequency data on a semi-log plot:

# In[ ]:

figure(figsize=(14, 10))
subplot(1, 2, 1)
plot(t, y)
xlabel('t (seconds)')
ylabel('Amplitude')
title('Signal')

subplot(1, 2, 2)
semilogy(fftshift(F), fftshift(P))
axis(xmin=-10, xmax=10, ymin=0, ymax=1)
xlabel('Hz')
ylabel('Power (dB)')
title('Frequency Domain')
grid(True)


# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
