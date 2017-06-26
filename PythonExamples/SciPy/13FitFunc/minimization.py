#!/usr/bin/python


from numpy import set_printoptions,linspace
from numpy import sin, cos, pi, meshgrid
from matplotlib.pyplot import figure,plot,xlabel,ylabel,title


set_printoptions(precision=3,threshold=7,edgeitems=3,suppress=True)

def dist(theta,v0):
    """calculate the distance travelled by the projectile 
    at theta with v0 initial velocity)
    """
    g= 9.8
    theta_rad = pi*theta/180
    return 2*v0**2/g *sin(theta_rad)*cos(theta_rad)

theta = linspace(0,90,90)
p = plot(theta,dist(theta,1.))
xl = xlabel('launch angle $\Theta ^{\circ}$')
yl = ylabel('horizontal distance traveled')

def neg_dist(theta,v0):
    return -1*dist(theta,v0)
        
        
        
from scipy.optimize import minimize
result = minimize(neg_dist,40,(1))
print "optimal angle = {:.1f} degrees".format(result.x[0])
        
        
# Te Result object

print type(result)
# dictionary 
# x array of the result
# nfev number of func evaluation
# njev num of time that is evaluated the jacobian

print result

# The Rosenbrock function
# f(x) = Sum (i=1,N-1) 100*(x_i-x_i-1**2)**2 +(1-x_i-1**2)

from scipy.optimize import rosen
from mpl_toolkits.mplot3d import Axes3D

x,y = meshgrid(linspace(-2,2,25), linspace(-0.5,3.5,25))
z = rosen([x,y])

fig = figure(figsize = (12,5.5))
ax = fig.gca(projection="3d")
ax.azim = 70 
ax.elev = 48
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlim(0,1000)
p = ax.plot_surface(x,y,z,rstride=1, cstride=1,cmap=cm.jet)
rosen_min = ax.plot([1],[1],[0],"ro")

x0 = [1.3,1.6,-0.5,-1.8,0.8]
result = minimize(rosen,x0)
print result.x

x0 = random.randn(5)
result = minimize(rosen,x0)
print x0
print result.x


