#!/usr/bin/python

# coding: utf-8

# Strings
# =======
# 
# Let's look at how you can create simple strings.
# 
# You can just put double quotes around the characters and that creates a string:

# In[ ]:

s = "hello world"
print(s)


# You can also use single quotes:

# In[ ]:

s = 'hello world'
print(s)


# There's no difference between using single and double quotes, but you need to be consistent in which one you choose for a given string.
# 
# You can add two strings, concatenating them together:

# In[ ]:

"hello " + "world"


# You can also multiply strings by an integer, which duplicates the string that number of times:

# In[ ]:

"echo" * 3


# You can get the length of a string with the generic function `len()` which operates on any Python sequence, but works with strings in particular:

# In[ ]:

s = "hello"
len(s)


# String Methods
# --------------
# 
# Strings are Python objects, so they have methods.
# 
# You can split a string wherever it has white space (a sequence of spaces, tabs or newlines) using the `split()` method:

# In[ ]:

s = "hello world"
word_list = s.split()
print(word_list)


# The result is a list, which we'll learn about later, containing the strings `"hello"` and `"world"`.
# 
# You can put the words back together by starting with a single space and then using its `join()` method with the word list to join the strings together with a space between each item:

# In[ ]:

space = ' '
space.join(word_list)


# Strings have a nice convenience method for replacing text in the string.  It's not as powerful as full regular expression engine (you can get that from the `re` module), but for simple substitution it works very well.
# 
# In this case we'll replace the `"world"` with `"Mars"`:

# In[ ]:

s = "hello world"
s.replace("world", "Mars")


# The `upper()` method converts all of the string's characters to upper case:

# In[ ]:

s = "hello world"
s.upper()


# The `strip()` method removes excess characters from the ends of a string. This is useful in the real world as strings often come with extra garbage characters at the front and back that you don't care about.
# 
# By defualt `strip()` removes whitespace:

# In[ ]:

s = "\t  hello  \n"
s.strip()


# There are many other methods on strings, and Python's `dir()` function will list all the methods on an object:

# In[ ]:

dir(s)


# IPython makes it even easier: if you have a string `s` you can just type `s.` and then hit the "tab" key and get a list of all the methods.

# In[ ]:

s = "hello" 


# In[ ]:

## s.             #Try this out for yourself - put cursor after the period and press <TAB>


# Looking through the methods you will see the ones we just talked about, but also things like `lstrip()` and `rstrip()` which strip from the left and right respectively, and a whole host of others.

# Multi-Line Strings
# ------------------
# 
# If you have a string which breaks across a line, you can use triple quotes around it:

# In[ ]:

a = """hello
world"""
print(a)


# Triple single quotes also work:

# In[ ]:

a = '''hello
world'''
print(a)


# If you look at the raw representation of the resulting string, you'll see that it has a new line character (`\n`) in it:

# In[ ]:

a


# If you have a string which is too long to fit on one line, but you don't want the new line charcater in it, one approach is to use parentheses to group strings together:

# In[ ]:

a = ("hello "
     "world")
print(a)


# Python takes the group and concatenates the strings together without any additional characters.
# 
# You can also use the line continuation character `\` at the end of the first line, but you need to be careful that the line continuation character is the very last character on the line:

# In[ ]:

a = "hello "     "world"
a


# This is slightly less convenient than using parenthesis since if you have 4 or 5 lines you'll need a continuation character at the end of each line, whereas parentheses are only needed at the start and end.
# 
# If you do want a newline, but don't want to use triple quotes, you can simply include it in a string with the `"\n"` escape sequence:

# In[ ]:

a = "hello\nworld"
print(a)


# Number/String Conversions
# -------------------------
# 
# In a previous lecture we saw that you could convert a number to a string in two ways: `str()` and `repr()`.
# 
# `str()` gives the "pretty" conversion:

# In[ ]:

str(1)


# In[ ]:

str(1.1 + 2.2)


# While `repr()` gives the "full" conversion:

# In[ ]:

repr(1.1 + 2.2)


# If you evaluate the `repr()` string, the convention is that it should give you back the original value that you had, which is not guaranteed for the `str()` version.
# 
# There are a few functions for converting integers to strings in various bases.  `hex()` returns the hexadecimal representation:

# In[ ]:

hex(255)


# `oct()` returns the octal representation:

# In[ ]:

oct(255)


# `bin()` returns the binary representation:

# In[ ]:

bin(255)


# To go in the other direction, if you have a string which is the representation of a valid integer, you simply use `int()` to convert it to an integer:

# In[ ]:

int('23')


# You can even pass in a second argument which is the base of the string representation:

# In[ ]:

int('FF', 16)


# Finally, `float()` does the same work as `int()` but returns a floating point number:

# In[ ]:

float('23')


# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
