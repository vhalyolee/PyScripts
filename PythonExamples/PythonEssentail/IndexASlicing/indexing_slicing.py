
# coding: utf-8

# Indexing and Slicing
# ====================
# 
# A common operation with ordered sequences is to pull out a single element or a range of elements from the sequence.  This is possible in strings, lists, tuples and anything that supports the expected interface for ordered sequences in Python.
# 
# Indexing
# --------
# 
# Let's use a string:

# In[ ]:

s = "hello world"


# Indexing is 0-based instead of 1-based, so the index 0 gives the first character.
# 
# When thinking about indices, it's useful to think of them as being between the elements, rather than on the elements:
#     
# We'll see how this mental model really helps in understanding how slicing works later.
# 
# To index into an object in python, take your object and put the index in square brackets after it:

# In[ ]:

s[0]


# To get the 5th element, use index 4:

# In[ ]:

s[4]


# Python also has the idea of negative indices which count from the back of the sequence:
# 
# So the last element of the sequence is index -1.  For example:

# In[ ]:

s[-3]


# This means that you never need to compute the length of your sequence and then subtract from it, you can just use negative indexes.
# 
# When you ask for an index out of the range of the array, you get an `IndexError` exception:

# In[ ]:

s[11]


# Slicing
# -------
# 
# Slicing is used to extract a subsequence out of your sequence, and has a special notation in Python:
# 
#     var[lower:upper:step]
# 
# The element which has index equal to the lower bound is included in the slice, but the element which has index equal to the upper bound is excluded, so mathematically, the ie slice is `[lower, upper)`.  If you think of the indices as being between the elements, then this mentally works very nicely, as we'll see.
# 
# The `step` argument is optional, and indicates the strides between elements in the subsequence, so a step of 2 takes every second element.
# 
# As an example, let's extract elements 1 through 3:

# In[ ]:

s = "hello"
s[1:3]


# To understand this, we find index 1 and index 3, and take all the elements in between:
# 
# Notice that 3 - 1 = 2, which is the length of the string we extracted.
# 
# You can also use negative indexing in slices:

# In[ ]:

s[1:-2]


# In[ ]:

s[-4:3]


# You can choose to omit indices in the slicing notation.  Omitting the first index means that we start the slice from the start of the sequence:

# In[ ]:

s[:3]


# Omitting the last index means that the slice goes to the end of the sequence:

# In[ ]:

s[-3:]


# If you omit both, then the slice goes from the beginning to the end of the sequence.  For example:

# In[ ]:

s[::2]


# means that the slice starts at the beginning, goes to the end, and takes every second element.  In other words, we get the elements at indices 0, 2, 4, etc.
# 
# When slicing, indexes out of range behave differently than when indexing.  So if we were to ask for a slice which is too long, such as asking for the first 6 characters in a string of length 5:

# In[ ]:

s[:6]


# You can see that this worked OK.  Slices give you whatever elements come between those two indices, even if the ends of the slice are out of range.
# 
# Finally, you can slice all of the elements with a slice like this:

# In[ ]:

s[:]


# and this is equivalent to the explicit slice:

# In[ ]:

s[0:len(s)]


# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
