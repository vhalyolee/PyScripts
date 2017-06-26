#!/usr/bin/python

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
#get_ipython().magic(u'matplotlib inline')
import pylab 

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

#print " The frequncy : ",F
#print "Y : ",Y
#print "Period  : ",P

# And then display the signal and its frequency data on a semi-log plot:

# In[ ]:

figure(figsize=(14, 10))
subplot(1, 2, 1)
plot(t, y)
#pylab.show()
xlabel('t (seconds)')
ylabel('Amplitude')
title('Signal')

subplot(1, 2, 2)
semilogy(fftshift(F), fftshift(P))
#pylab.show()
axis(xmin=-10, xmax=10, ymin=0, ymax=1)
xlabel('Hz')
ylabel('Power (dB)')
title('Frequency Domain')
grid(True)
