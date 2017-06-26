#!/usr/bin/python

# fitting with python

from numpy import set_printoptions

set_printoptions(precision=3,threshold=7,edgeitems=3,suppress=True)

from numpy import polyfit,poly1d, linspace,array,random, pi,sin,hstack,ones
from numpy import newaxis

from matplotlib.pyplot import figure, fill_between, hist, plot, axis



x = linspace(-5,5,100)

y = 4*x+1.5

noisy_y = y+random.randn(y.shape[-1])*2.5

p = plot(x,noisy_y,'rx')
p = plot(x,y,'b:')

coefficients = polyfit(x,noisy_y,1)
print coefficients

p = plot (x,noisy_y,'rx')
p = plot(x,coefficients[0]*x+coefficients[1],'k-')
p = plot(x,y,'b--')

f = poly1d(coefficients)
p = plot(x,noisy_y,'rx')
p = plot(x,f(x))



# Sine curve example


x = linspace(-pi,pi,100)
y = sin(x)

y1 = poly1d(polyfit(x,y,1))
y3 = poly1d(polyfit(x,y,3))
y5 = poly1d(polyfit(x,y,5))
y7 = poly1d(polyfit(x,y,7))
y9 = poly1d(polyfit(x,y,9))


x = linspace(-3*pi,3*pi,100)
p = plot(x,sin(x),'k')
p = plot(x,y1(x))
p = plot(x,y3(x))
p = plot(x,y5(x))
p = plot(x,y7(x))
p = plot(x,y9(x))
a = axis([-3*pi,3*pi,-1.25,1.25])




# Least square fitting
# curve fitting with data
#linear algebra

from scipy import linalg, sqrt,exp
from scipy.linalg import lstsq
from scipy.stats import linregress
from scipy.optimize import leastsq

x = linspace(0,5,100)
y = 0.5*x+random.randn(x.shape[-1])*0.35
p = plot(x,y,'x')



#scipy.linalg.lstsq


X= hstack((x[:,newaxis],ones((x.shape[-1],1))))

C,resid,rank,s=linalg.lstsq(X,y)
p = plot(x,y,'rx')
p = plot(x,C[0]*x+C[1],'k--')
print "Coeffiencients :{}".format(C)
print "Sum squared residual = {:.3f}".format(resid)
print "rank of  the X matrix = {}".format(rank)
print "singular values of X = {}".format(s)


# Scipy stats linregress


slope, intercept, r_value, p_value,stderr=linregress(x,y)
p = plot(x,y,'rx')
p = plot(x,slope*x+intercept,'k--')
print slope
print intercept
print "R value (correlation coefficient) = {:.3f}".format(r_value)
print "P_value (probability there is no correlation) = {:.3e}".format(p_value)
print "root mean squared error (sigma) of the fir = {:3f}".format(sqrt(stderr))

# Curve fitting with callables

from numpy import exp, pi, linalg, linspace, newaxis, sin, sqrt
from matplotlib.pyplot import plot, axis



def function(x,a,b,f,phi):
    """a function of x with four p"""
    result = a * exp(-b*sin(f*x+phi))
    return result
    
    
x = linspace(0,2*pi,50)
actual_parameters = [3,2,1.25,pi/4]
y = function(x,*actual_parameters)
plot(x,y)

    
    