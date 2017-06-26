
# coding: utf-8

# # Matplotlib Basics

# In[ ]:

# Imports required but not shown in the video lecture.
import numpy
import matplotlib

from numpy import array, cos, linspace, mgrid, pi, sin, sqrt
from numpy.random import rand, randn
from matplotlib.pyplot import (clf, close, colorbar, figure, 
                               grid, hold, imshow, legend, 
                               plot, scatter, show, subplot, 
                               title, xlabel, ylabel, )
from matplotlib import cm
get_ipython().magic(u'matplotlib inline')


# In[ ]:

print numpy.__version__
print matplotlib.__version__


# `matplotlib` provides tons of tools for creating line plots, image plots, and even some 3D plots.  By default, many of the matplotlib functions are available at the command line or in notebooks within Canopy.  When you write scripts using these tools, you will need to import the desired functions.  There are a couple of common approaches.  The first is to import the specific functions you want using:
#     
#     from matplotlib.pyplot import plot, subplot, figure, etc.
# 
# An alternative that is also used quite often is:
#     
#     import matplotlib.pyplot as plt
# 
# Using this approach, you can refer to the plot commands through the `plt` name such as `plt.plot`.
# 
# Within Canopy, the command line and notebooks use `pylab` mode which, from a plotting perspective, is equivalent to running:
#     
#     from matplotlib.pyplot import *
# 
# at the command line.
# 
# 
# Line Plots
# ==========
# 
# The **`plot`** command is the swiss army knife of plotting commands.  It defaults to creating line plots, but it is possible to control many different aspects of data display (marker types, color, transparency, etc.) through its key word arguments.

# Plot Against Indices
# --------------------
# 
# When calling **`plot`** with a single argument (in this case `sin(x)`), the values of the array are used as the y values, and the indices of the array (0, 1, 2, ...) are used as the x axis.

# In[ ]:

x = linspace(0, 2*pi, 50)
plot(sin(x))


# When calling plot with two arguments, the first is used as the x value, and the second is used as the y value.

# In[ ]:

plot(x,sin(x))


# Multiple Data Sets
# ------------------
# 
# Calling **`plot`** with multiple argument pairs results in multiple lines within a plot.

# In[ ]:

plot(x, sin(x), x, sin(2*x))


# Launching External Plots Windows
# ================================
# 
# By default, the notebooks in Canopy put the plot command output 'inline' within the notebook.  It is possible, however, to launch an external plot window from using the magic command **`%pylab qt`**.  This will bring up the standard plot window that you get when running plot commands from Canopy's console window.  There are multiple benefits to external windows including much more interactive plots (zooming, panning, etc.).  You can use this window to experiment with the various toolbars.  

# In[ ]:

get_ipython().magic(u'matplotlib qt')
plot(x, sin(x))


# To switch back to inline plots, use the magic command **`%pylab inline`**.

# In[ ]:

get_ipython().magic(u'matplotlib inline')
plot(x, sin(x))


# Plot Format Strings
# ===================
# 
# If and x,y data pair is followed by a string, it is interpreted as a format string for the line that allows you to specify color, line type, and marker type.  To see a full list of options for format strings, type **`plot?`** at the prompt.

# In[ ]:

plot(x, sin(x), 'r-^')


# In[ ]:

plot(x, sin(x), 'b-o', x, sin(2*x), 'r-^')


# Scatter Plots
# =============
# 
# The **`scatter`** function can create simple x, y scatter plots.

# In[ ]:

x = linspace(0, 2*pi, 50)
y = sin(x)
scatter(x,y)


# It also takes 4 arguments to produce a x,y scatter plot that also varies the size and color for each marker.

# In[ ]:

x = randn(200)
y = randn(200)
size = rand(200) * 30
color = rand(200)
scatter(x, y, size, color)
colorbar()


# Multiple Plot Windows
# =====================
# 
# The **`figure`** function will create new plot windows (when not in the inline plot display mode in notebooks).  In notebooks, it simply creates two separate plots.

# In[ ]:

get_ipython().magic(u'matplotlib qt')
t = linspace(0, 2*pi, 50)
x = sin(t)
y = cos(t)

# create the first window
figure()
plot(x)

# create the second window.
figure()
plot(y)


# Multiple Plots in one Window
# ============================
# 
# The **`subplot`** function allows you to position two separate plots within a single plot window.

# In[ ]:

get_ipython().magic(u'matplotlib inline')
x = array([1,2,3,2,1])
y = array([1,3,2,3,1])

subplot(2,1,1)
plot(x)

subplot(2,1,2)
plot(y)


# Adding Lines to a Plot
# ======================
# 
# By default, multiple **`plot`** calls in a row will add plots to the same window. This behavior is controlled by the **`hold`** function.  By default, `hold` is `True`.

# In[ ]:

x = linspace(0, 2*pi, 50)
plot(sin(x))
plot(cos(x))


# Calling the **`hold`** function with `False` as its argument will turn off this behavior.  Now all subsequent `plot` functions will erase any existing data before displaying their data.  In the call below, you'll notice that only `cos(x)` is displayed.   

# In[ ]:

plot(sin(x))
hold(False)
plot(cos(x))
hold(True) # Turn hold back on so that subsequent plots will overplot.


# Legends
# =======
# 
# The **`legend`** function will add a legend to plots, using the specified `label` keyword argument that was passed into each plot function.

# In[ ]:

plot(sin(x), label='sin')
plot(cos(x), label='cos')
legend()


# Here is an example where we have three lines, but have only labeled two.  **`legend`** is smart enough to only put the labeled lines into the legend.

# In[ ]:

plot(sin(x), label='sin')
plot(sin(2*x))
plot(cos(x), label='cos')
legend()


# If the plot functions have not assigned a label to the lines, then you can pass a list of labels to the **`legend`**.  The labels are assigned to the data sets in the same order they were added to the plot.

# In[ ]:

plot(sin(x))
plot(cos(x))
legend(['sin', 'cos'])


# Titles And Grid
# ===============
# 

# In[ ]:

plot(x, sin(x))
xlabel('radians')
ylabel('amplitude', fontsize='large')
title('Sin(x)')


# In[ ]:

plot(x, sin(x))
xlabel('radians')
ylabel('amplitude', fontsize='large')
title('Sin(x)')
grid()


# Clearing and Closing Plots
# ==========================

# In[ ]:

get_ipython().magic(u'matplotlib qt')
plot(x, sin(x)) # This line will create a plot.
clf() # And this will clear it.


# In[ ]:

close() # And this closes the window.
close('all') # And this will close all windows.


# In[ ]:

# Turn the inline plots back on.
get_ipython().magic(u'matplotlib inline')


# In[ ]:

from scipy.misc import ascent
img = ascent()
imshow(img, extent=[-25, 25, -25, 25], cmap=cm.bone)
colorbar()


# Histograms
# ==========
# 
# **`hist`** will create a histogram with 10 bins by default.  This can be changed by specifying the `bins` keyword argument.
# 
# Note that matplotlib's `hist` function can be slow on large data sets.  In these cases, it can be beneficial to use the `scipy.stats.histogram` method which is faster.  However, it only does the calculations. It'll be up to you to make the plot from the returned values.
# 

# In[ ]:

hist(randn(1000))


# In[ ]:

hist(randn(1000), 30)


# In[ ]:

from mpl_toolkits.mplot3d import Axes3D
x, y = mgrid[-5:5:35j, 0:10:35j]
z = x*sin(x)*cos(.25*y)
fig = figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.jet)
xlabel('x')
ylabel('y')


# In[ ]:

t = linspace(0, 30, 1000)
x, y, z = (t*cos(t) , t*sin(t), t)
fig = figure()
ax = Axes3D(fig)
ax.plot(x, y, z)
xlabel('x')
ylabel('y')


# In[ ]:

from scipy import special
x, y = mgrid[-25:25:100j, -25:25:100j]
r = sqrt(x**2+y**2)
s = special.j0(r) * 25

# You'll need to be in 'qt' mode to be able to interact with
# the plot correctly.
get_ipython().magic(u'matplotlib qt')
from mayavi import mlab
mlab.surf(x, y, s)
mlab.colorbar()
mlab.axes()


# In[ ]:

get_ipython().magic(u'matplotlib inline')


# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
