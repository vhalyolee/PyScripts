
# coding: utf-8

# # Introducing NumPy Arrays

# In[ ]:

# Imports required but not shown in the video lecture.
import numpy

from numpy import array


# In[ ]:

print numpy.__version__


# Simple Array Creation
# =====================
# There are a number of ways to create an NumPy array.  Here we start with a simple list, `lst`, that we'll convert to a numpy array, `a` using the **`array`** function.

# In[ ]:

lst = [0, 1, 2, 3]
lst


# In[ ]:

a = array(lst)
a


# You can also just create a list (or tuple or any sequence) on the fly and convert it directly to an array.  For example, instead of the two-step process above, you will often see this:

# In[ ]:

a = array([0,1,2,3])
a


# Checking the Type
# =================
# 
# If you check the data type of `a` you'll see that the `array` function retuns something called a `numpy.ndarray`.  The `nd` here stands for N-dimenional or multi-dimensional.  So, even though this example is a one dimensional array, they also can be two, three, or more dimensional.
# 
# Even though it has this fancy name, we (and everyone else) will forever more just refer to the as 'arrays' or 'NumPy arrays.'

# In[ ]:

type(a)


# Numeric 'Type' and bytes of Elements 
# ====================================
# 
# 
# NumPy arrays are special compared to Python lists because the are 'homogenous,' meaning that each and every element in the array has the same data type. (Remember that Python lists, on the other hand, can have a different type of data in each position.)  This homogenity is one of the secrets to NumPy's speed and memory efficiency.
# 
# The **`dtype`** attribute of an array will tell you its data type.  In the presentation videos, the type is `dtype('int32')` which means each element is a 4 byte (or 32 bit) integer.  This is because it was originally designed running on a 32 bit operating system.  This notebook was created on a 64-bit OSX machine, so the default data type for integers is larger at 8 bytes (64 bits).  You can double-check this by checking the **`itemsize`** attribute for the array.  This takes up twice the memory, but also means that it can represent larger (and smaller) numbers than the 32-bit arrays.  If you select 'Cell' on the menu above and then 'Run All', it will re-run this notebook on your machine.  What is the default integer array type for you?
# 
# *Note: We will see later, that NumPy arrays can actually hold heterogenous data types (hint: `array([1,1.2,'hello'], dtype=object)`).  This is a great feature, but it does impact both speed and memory efficiency.*

# In[ ]:

a.dtype


# In[ ]:

a.itemsize


# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
