#!/usr/bin/python
# coding: utf-8

# # String Formatting

# String formatting is needed as soon as you want to control how text and data are displayed when printed in the terminal, in a data file or in a report that you need to generate. The recommeded way is by using the `format` method on a string which was added to the language fairly recently (Python 2.6).
# 
# Examples
# --------
# The strategy is to create a string that you want to print (let's assume to the terminal for now). Curly brackets will indicate where (and potentially how) to display variables that are provided to the format method:

# In[21]:

print('{} {} {}')


# In[2]:

print('{} {} {}'.format("a", "b", "c"))


# In[3]:

s = 'My favorite number is {}'
print s.format(3.145926)


# The fields where variables are injected can be numbered too (they must be numbered in Python 2.6):

# In[4]:

print('{2} {1} {0}'.format("a", "b", "c"))


# In[5]:

print('{color} {n} {x}'.format(n=10, x=1.5, color='blue'))


# In[6]:

print('{color} {0} {x} {1}'.format(10, 'foo', x=1.5, color='blue'))


# In[7]:

from math import pi
print('{0:10} {1:10d} {c:10.2f}'.format('foo', 5, c=2*pi))


# In[8]:

'{0:2d}-{1}: {name}, ${price:.2f}'.format(7, 19, name='SC1', price=3.4)


# Format spec
# -----------
# 
# Let's print a floating point number with various precisions:

# In[9]:

print('[{x:5.0f}]  [{x:5.1f}]  [{x:5.2f}]'.format(x=12.3456))


# How to control how to/whether to display the signs of positive and negative numbers:

# In[22]:

'{:-f}; {:-f}'.format(3.14, -3.14)


# In[11]:

'{:+f}; {:+f}'.format(3.14, -3.14)


# In[12]:

'{: f}; {: f}'.format(3.14, -3.14)


# Let's use the alignment options to see how to place a word within a larger string with the different types of caret symbols:

# In[13]:

print('[{0:<10s}]  [{0:>10s}]  [{0:^10s}]'.format('PYTHON'))


# In[14]:

print('[{0:*<10s}]  [{0:*>10s}]  [{0:*^10s}]'.format('PYTHON'))


# Finally, we can use the various codes allowed for integers to display it in various number bases:

# In[15]:

'{0:X} {0:d} {0:o} {0:b}'.format(254)


# ## "Old style" formatting with %

# The old style formatting valid before Python 2.6 used the % symbol. It is still valid syntax for all current versions of Python though it is expected to become deprecated in favor of the format method above. Let's review it anyway because a lot of code has been written  using it and you will encounter it.
# 
# The idea is that you replace the {} in the container string by % and a letter depending on the nature of the value that will be inserted (just like in C):

# In[16]:

s = "some numbers:" 
x = 1.34
y = 2
t = "%s %f, %d" % (s,x,y)
print(t)


# The container string will be followed by a % again and a comma separated list of variables (we will see later that this is called a tuple, not a list) containing the values to be inserted. 
# 
# Controlling the way the sign of numbers is displayed can be done with this style as well:

# In[17]:

y = -2.1
print("%f\n%f" % (x,y))


# In[18]:

print("% f\n% f" % (x,y))


# And just like with the format method, a value can be displayed differently depending on the conversion code used: d, f, e, ...

# In[19]:

print("%4.2f" % x)


# In[20]:

print("%4.2e" % x)


# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
