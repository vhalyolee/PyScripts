#!/usr/bin/python
# -*- coding: utf-8 -*-

# ##Symbolic Integration

# In[1]:

import numpy as np
from numpy import pi, linspace, vectorize,exp
from matplotlib.pyplot import plot, title,annotate
get_ipython().magic(u'matplotlib inline')


# In[2]:

np.set_printoptions(precision=3)


# Integrals are *anti-derivatives*
# 
# $$\frac{d}{dx}F(x) = f(x)$$
# 
# $$ \Rightarrow F(x) = \int f(x) dx $$

# In[14]:

#from IPython.external.mathjax import install_mathjax
#install_mathjax()
#%load_ext sympyprinting

from sympy import init_printing; init_printing()


# In[15]:

#%reload_ext sympyprinting


# In[16]:

from sympy import symbols, integrate
import sympy


# In[17]:

x, y = symbols('x y')
sympy.sqrt(x ** 2 + y **2)


# In[18]:

z = sympy.sqrt(x ** 2 + y **2)
z.subs(x, 3)


# In[19]:

z.subs(x, 3).subs(y, 4)


# In[20]:

from sympy.abc import theta
y = sympy.sin(theta) ** 2
y


# In[21]:

Y = integrate(y)
Y


# In[22]:

Y.subs(theta, pi) - Y.subs(theta, 0)


# In[23]:

integrate(y, (theta, 0, sympy.pi))


# In[24]:

integrate(y, (theta, 0, sympy.pi)).evalf()


# In[25]:

Y_indef = sympy.Integral(y)
print type(Y_indef)
Y_indef


# In[26]:

Y_definite = sympy.Integral(y, (theta, 0, sympy.pi))
print type(Y_definite)
Y_definite


# In[27]:

Y_definite.evalf()


# In[30]:

Y_raw = lambda x: integrate(y, (theta, 0, x))
Y = vectorize(Y_raw)


# In[29]:

x = linspace(0, 2 * pi, 100)
p = plot(x, Y(x))
t = title(r"$y = \int_{0}^{x} sin^2(\theta) d\theta $")

# Numerical Integration of callable function


from scipy.special import jv
def f(x):
    return jv(2.5,x)

x = linspace(0,10,100)
p = plot(x,f(x),'k-')

from scipy.integrate import quad
interval = [0,6.5]
value, max_err = quad(f,*interval)
from matplotlib.pyplot import figure,fill_between

print value
print max_err

print "integral = {:.9f}".format(value)
print "upper bound on error: {:.2e}".format(max_err)
x = linspace(0,10,100)
p = plot(x,f(x),'k-')
x = linspace(0,6.5,45)
p = fill_between(x,f(x),where=f(x)>0,color="blue")
p = fill_between(x,f(x),where=f(x)<0,color="red",interpolate=True)

from numpy import inf
interval = [0,inf]

def g(x):
    return exp(-x**1/2)
    
value,max_err = quad(g,*interval)
x = linspace(0,10,50)
fig = figure(figsize=(10,3))
p = plot(x,g(x),'k-')
p = fill_between(x,g(x))
annotate("$\int_0^{\infty}e^{-x^1/2}dx = $" + "{}".format(value),(4,0.6),fontsize=16)
print "upper bound on error : {:.1e}".format(max_err)

# Double integration 

def h(t,x,n):
    """core function takes x,t,n"""
    return exp(-x*t)/(t**n)

# note quad return value and err so er want only value
# the vectorize is for the scalar func to use properly a numpy array

from numpy import vectorize
@vectorize
def int_h_dt(x,n):
    """Time integrand of h(x). """
    return quad(x,1,inf,args=(x,n))[0]
    
@vectorize
def I_n(n):
    return quad(int_h_dt,0,inf,args=(n))
        
I_n([0.5,1.0,2.0,5])
    
    
from scipy.integrate import dblquad
@vectorize
def I(n):
    """ Same as I_n but using the built in dblquad"""    
    x_lower = 0
    x_upper = inf
    return dblquad(h,x_lower,x_upper,
        lambda t_tower:1,lambda t_upper:inf,args=(n,))

I([0.5,1.0,2.0,5])  
    
        
            
                    
        