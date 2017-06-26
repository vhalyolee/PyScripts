#!/usr/bin/python


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import (clf, close, colorbar, figure, 
                               grid, hold, imshow, legend, 
                               plot, scatter, show, subplot, 
                               title, xlabel, ylabel, )
import scipy.fftpack

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
figure()
plot(y)



yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

get_ipython().magic(u'matplotlib inline')
subplot(2,1,1)
plot(y)

subplot(2,1,2)
plot(xf, 2.0/N * np.abs(yf[:N//2]))


import pandas


#import seaborn
%matplotlib inline

# the OP's data
x = pandas.read_csv('http://pastebin.com/raw.php?i=ksM4FvZS', skiprows=2, header=None).values
y = pandas.read_csv('http://pastebin.com/raw.php?i=0WhjjMkb', skiprows=2, header=None).values
fig, ax = plt.subplots()
ax.plot(x, y)


x = np.linspace(0,5,100)
y = np.sin(2*np.pi*x)
plot(y)

## fourier transform
f = np.fft.fft(y)
## sample frequencies
freq = np.fft.fftfreq(len(y), d=x[1]-x[0])
plt.plot(freq, abs(f)**2) ## will show a peak at a frequency of 1 as it should.




%fig, ax = plt.subplots()
%ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
%plt.show()