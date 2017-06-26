#!/usr/bin/python

from numpy import array, linspace

heights = array([1.46, 1.56, 2.2,1.77, 1.47, 1.48])

print "mean, ", heights.mean()
print "min, ",heights.min()
print "max ", heights.max()
print "std ", heights.std()


import scipy.stats.stats as st

#print "median, ",st.nanmedian(heights)
print "mode ", st.mode(heights)
print "skewness ",st.skew(heights)
print "kurtosis, ",st.kurtosis(heights)

#heights[2] = nan
#print heights.mean()
#print st.nanmean(heights)


from scipy.stats import norm

x_norm =  norm.rvs(size=500)
print type(x_norm), x_norm.shape

h = hist(x_norm)
print "counts, ", h[0]
print "bin centers, ",h[1]

h = hist(x_norm,normed=True,bins=20)

x_mean,x_std,= norm.fit(x_norm)
print "mean, ",x_mean
print "std, ",x_std

x = linspace(-3,3,50)
h = hist(x_norm,normed=True,bins=20)
p=plot(x,norm.pdf(x),'r-')


from scipy.integrate import trapz
x1 = linspace(-2,2,100)
p = trapz(norm.pdf(x1),x1)

print "{:.2%} of values lie between -2 and 2 ".format(p)

fb = fill_between(x1,norm.pdf(x1),color="green")
p = plot(x,norm.pdf(x), 'k-')
 
p = plot(x, norm.pdf(x, loc=0, scale=1))
 
p = plot(x, norm.pdf(x, loc=0.5, scale=1))
  
  # Continious distribution
  
  
from scipy.stats import lognorm, t, dweibull


x = linspace(0.01,3,100)
from pylab import legend, title

p = plot(x,lognorm.pdf(x,1),label='s=1')
p = plot(x,lognorm.pdf(x,2),label='s=2')
p = plot(x,lognorm.pdf(x,0.1),label='s=0.1')
l = legend()


x = linspace(0.01,3,100)
p = plot(x,dweibull.pdf(x,1), label="s=1 - constat failure rate")
p = plot(x,dweibull.pdf(x,2), label="s>1 - increasing failure rate")
p = plot(x,dweibull.pdf(x,0.1), label="0<s<1 - decreasing failure rate")
l=  legend()
t =title("Weibull 'time to failure' distribution")


from scipy.stats import t

x = linspace(-3,3,100)
p = plot(x, t.pdf(x,1), label="dof=1")
p = plot(x, t.pdf(x,2), label="dof=2")
p = plot(x, t.pdf(x,100), label="dof=100")
p = plot(x[::5], norm.pdf(x[::5]),"kx",label="normal")
l=legend()
pt = title("Student's t-distribution")

# discreet distribution

from scipy.stats import binom, poisson,randint

min = -10
max = 10

x = arange(min,max+1,0.5)
p = stem(x,randint(min,max).pmf(x))
t = title("Uniform distribution")

num_trails = 50
x= arange(num_trails)
p = plot(x,binom(num_trails,0.5).pmf(x),"o-",label="p=0.5")
p = plot(x,binom(num_trails,0.2).pmf(x),"o-",label="p=0.2")
l=legend(loc="upper right")
t=title("Binomial distribtion with 50 trails")

x=arange(0,21)
p=plot(x,poisson(1).pmf(x),'o-',label=r"$\lambda$=1")
p=plot(x,poisson(4).pmf(x),'o-',label=r"$\lambda$=4")
p=plot(x,poisson(9).pmf(x),'o-',label=r"$\lambda$=9")
l=legend()
t =title("Poisson 'number of occurances' distributions")



Creating your own disctrete distribtion

from scipy.stats import rv_discrete

xk = [1,2,3,4,5,6] #the values of the die 1-6
pk = [0.3, 0.35, 0.25, 0.05, 0.025, 0.025] # list of prob for each value

loaded = rv_discrete(values=(xk,pk))

loaded.rvs(size=2) # roll a pair of die


samples = loaded.rvs(size=100)
bins = linspace(0.5,6.5,7)

h= hist(samples,bins=bins,normed=True)
s = stem(xk,loaded.pmf(xk),markerfmt='ro',linefmt='r-')



#Hypothesis Testing
from numpy import concatenate
from scipy.stats import norm
from scipy.stats import ttest_ind, ttest_rel, ttest_1samp
from scipy.stats import t

n1 = norm(0.1,scale=1.0)
n2 = norm(0,scale=1.0)
n1_samples = n1.rvs(size=100)
n2_samples = n2.rvs(size=100)
samples = concatenate([n1_samples,n2_samples],axis=0)
loc, scale = norm.fit(samples)
n = norm(loc=loc,scale=scale)


x = linspace(-3,3,100)
h = hist([samples,n1_samples,n2_samples],normed=True)
p = plot(x,n.pdf(x),'b-')
p = plot(x,n1.pdf(x),'g-')
p = plot(x,n2.pdf(x),'r-')

t,p =ttest_ind(n1_samples,n2_samples) #independent t test
print "t = {}".format(t)
print "p -value = {}".format(p)


#pair samples


#measuring paired two samples before and after treatment 

pop_size = 35

pre_treat = norm(loc=0., scale=1.0)
n0 = pre_treat.rvs(size=pop_size)
x = linspace(-3,3,100)
plot(x,pre_treat.pdf(x))


effect = norm(loc=0.05,scale=0.2)
eff = effect.rvs(size=n0.shape[0])
plot(x,effect.pdf(x))

n1=n0+eff
loc,scale = norm.fit(n1)
post_treat = norm(loc=loc,scale=scale)

fig = figure(figsize=(10,4))
ax1 = fig.add_subplot(1,2,1)
h = ax1.hist([n0,n1],normed=True)
p = ax1.plot(x,pre_treat.pdf(x),'b-')
p =ax1.plot(x,post_treat.pdf(x),'g-')
ax2 = fig.add_subplot(1,2,2)
h= ax2.hist(eff,normed=True)

#independent samples test

t_val,p_val = ttest_ind(n0,n1)
print "t={}".format(t_vale)
print "p-value = {}".format(p_val)

t_val,p_val = ttest_rel(n0,n1)
print "t={}".format(t_vale) # what is the liklihood your distribution is in the tails
print "p-value = {}".format(p_val) # the amount of the curve that is in the tails

my_t = t(n0.shape[0]) #pass the dof = number of samples
p = plot(x, my_t.pdf(x), 'b-', linewidth=2)
lower_x = x[x <= -abs(t_val)]
upper_x = x[x >= abs(t_val)]
p = fill_between(lower_x, my_t.pdf(lower_x), color="gray")
p = fill_between(upper_x, my_t.pdf(upper_x), color="gray")

my_t.cdf(-abs(t_val)) * 2 # this is turning a t value to a p value 
# it basicaly integrate the tail the more you have on the tail its unlikly there are coming from the same sidtribtuions
