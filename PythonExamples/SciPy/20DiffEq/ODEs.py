#!/usr/bin/python
# -*- coding: utf-8 -*-

# coding: utf-8

# ## Integral solution to ODE's

# In[ ]:

# Imports required but not shown in the video lecture.
from matplotlib.pyplot import plot, legend, xlabel, ylabel
from numpy import linspace, pi, cos, sin
from scipy.integrate import odeint


# Simple example:
# 
# $$\frac{dy}{dt} = sin(t)$$

# In[ ]:

def dy_dt(y, t):
    return sin(t)


# In[ ]:

t = linspace(0, 2*pi, 100)
result = odeint(dy_dt, 0, t)

print result
# In[ 
fig = figure(figsize=(12,4))
p = plot(t, result, "rx", label=r"$\int_{0}^{x}sin(t) dt $")
p = plot(t, -cos(t) + cos(0), label=r"$cos(0) - cos(t)$")
p = plot(t, dy_dt(0, t), "g-", label=r"$\frac{dy}{dt}(t)$")
l = legend(loc="upper right")
xl = xlabel("t")


# ## Higher order ODE's

# Projectile motion (vertical)
# 
# $$
# \frac{d^2x}{dt^2} = g - \frac{D}{m}\frac{dx}{dt}
# $$
# 
# 
# $$y = \left[x, \frac{dx}{dt}\right] $$
# 
# $$\begin{aligned}
# \frac{dy_0}{dt} &= y_1 \\\
# \frac{dy_1}{dt} &= -g - \frac{D}{m} y_1 \\\
# \end{aligned}
# $$

# In[ ]:

# vector y = [y0= x position , y1 = dx/dt velocity ]


def dy_dt(y, t):
    """Governing equations for projectile motion with drag.
    y[0] = position
    y[1] = velocity
    g = gravity (m/s2)
    D = drag (1/s) = force/velocity
    m = mass (kg)
    """
    g = -9.8
    D = 0.1
    m = 0.15
    dy1 = g - (D/m) * y[1]
    dy0 = y[1] if y[0] >= 0 else 0.
    return [dy0, dy1]

# ODE ordinary diff equation
# In[ ]:

position_0 = 0.
velocity_0 = 100
t = linspace(0, 12, 100)
y = odeint(dy_dt, [position_0, velocity_0], t)


# In[ ]:

p = plot(t, y[:,0])
yl = ylabel("Height (m)")
xl = xlabel("Time (s)")


# In[ ]:

y, infodict = odeint(dy_dt, [position_0, velocity_0], t, full_output=True, printmessg=True, )
print sorted(infodict.keys())
print "cumulative number of function evaluations at each calculated point:", infodict['nfe']
print "cumulative number of time steps", infodict['nst']

# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
