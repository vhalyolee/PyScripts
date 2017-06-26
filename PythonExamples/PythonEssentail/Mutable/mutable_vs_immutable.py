#!/usr/bin/python
# coding: utf-8

# Mutable vs. Immutable Data Structures
# =====================================
# 
# In this lecture we'll look at the difference between mutable and immutable objects in Python, or the idea of whether an object is changeable or not.
# 
# A list is an example of a mutable object.  We can change the value of an element in a list:

# In[ ]:

a = [1, 2, 3, 4]
a[0] = 100
print(a)


# We can insert values into it:

# In[ ]:

a = [100, 2, 3, 4]
a.insert(3, 200)
print(a)


# We can sort the values:

# In[ ]:

a = [100, 2, 3, 200, 4]
a.sort()
print(a)


# All of these are in-place operations that are actually changing the list a.
# 
# A string is an example of an immutable object.  If you try to set a character in a string to a new value, you get a `TypeError` exception:

# In[ ]:

s = "hello world"
s[0] = 'z'


# When you use the `replace()` method in a string, rather than modifying the string, you get a completely new string back:

# In[ ]:

s.replace('world', 'Mars')


# The original is unchanged:

# In[ ]:

s


# Having seen strings and lists, and the way that their operations and methods work, an obvious question which arises is how do we know whether a data structure will be modified, or a new data structure created?
# 
# The answer lies in knowing which objects are mutable and which are immutable.  Of the most commonly used types we have:
# 
# ### mutable:
# 
# - list
# - dictionary
# - set
# - NumPy array
# - user-defined objects
# 
# ### immutable:
# 
# - integer
# - float
# - complex
# - long
# - string
# - tuple
# - frozenset
# 
# One common question which arises is what do you do if you want to modify an immutable data type?  You can't, but there are patterns for doing equivalent operations which generate new objects.
# 
# For example, inserting values into a string fails:

# In[ ]:

s = 'abcde'
s[1:3] = 'xy'


# But you can build up a new string and overwrite the original like this:

# In[ ]:

s = s[:1] + 'xy' + s[3:]
print(s)


# This gives you the string that you want.
# 
# If you truly need a mutable string, there is the `bytearray` object.  Byte arrays _are_ mutable and have many of the same methods as strings.  So for example, I can create a byte array like this:

# In[ ]:

s = bytearray('abcde')
s


# and then assign into a slice:

# In[ ]:

s[1:3] = 'xy'
s


# and this works.  But you can't use a byte array in all the places that you can use a string.
# 
# Another question which might occur is why have immutable objects at all?  If there are byte arrays that are "mutable strings" then why doesn't Python use them instead of the current "immutable strings"?
# 
# The first reason is that mutable data structures can have surprising "action at a distance" behaviour.  Consider what happens when two variables are associated with the same list:

# In[ ]:

a = [1, 2, 3, 4]
b = a


# If we change `b`, look at what happens to `a`:

# In[ ]:

b[0] = 100
print(a)


# Because `a` and `b` are referring to the same object, `a` is unexpectedly changed.  And this could happen in completely different parts of your program if they happen to be referring to the same object.
# 
# Because strings are immutable, this can't happen: once you have a string you know that the value can't change, and this is important to Python's internals where this fact is used to allow a number of optimizations on string operations which make them faster.
# 
# Also strings are viewed as a fundamental data type, like integers and floats.  And just as integers and floats are immutable, strings are as well.
# 
# Finally, but possibly most importantly, immutability of strings allows them to be used as keys in a dictionary.  Dictionaries are a major data type in Python that we will talk about in another lecture, but dictonaries have a requirement that their keys be immutable or hashable, and strings are things that you frequently want to use as the keys of dictionaries.

# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
