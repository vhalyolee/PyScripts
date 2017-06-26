
# Katrina Advisory Exercise
# =========================
# 
# Whenever there's a Hurricane spinning out in the Atlantic (or Pacific), the US National Oceanic and Atomospheric Administration ([NOAA](http://www.noaa.gov/)) issues advisories about the storm's strength.  In this example, we will look at one such advisory for infamous [Hurricane Katrina](http://en.wikipedia.org/wiki/Hurricane_Katrina) that did so much damage to New Orleans in 2005.  
# 
# Imagine you would like to build an application that "reads" storm advisories and assigns a danger level without human interaction.  There are a lot of tools that could help with this (like [NLTK](http://www.nltk.org/)) with fancy-dancy algorithms, but we're going to take a very simple approach of scanning the document for mincing words.
# 
# Unlike a few of the other string exercises, the text for this example is located in a file on disk.  We haven't gotten to reading and writing files yet, but that is ok.  The following snippet of code opens the file "katrina_advisory.txt" (which is located in the same directory as this exercise), and dumps its contents into a string called `text`.  From here on out, you can work with `text` just as if you created the string yourself.


f = open("katrina_advisory.txt")
text = f.read()
f.close()
print 'Content of "katrina_advisory.txt"'
print '-' * 51
print
print text


# Question 1
# ----------
# Text and data processing always starts by some clean up. Format the text by converting it to lower case, remove spaces before and 
# after the content. 


# your code goes here


# Question 2
# ----------
# Ok.  Now for our own fancy-dancy algorithm.  Let's count the number of alarming terms in total in the processed `text`. For our purposes, we'll consider the following terms as alarming: "killed", "destroyed", "death", "devastating". (They all seem fairly alarming to me...)


# your code goes here


# Question 3
# ----------
# Let's also track how urgent NOAA thought the message was.  For this, we'll see if they started the message with the word "URGENT" (or "urgent").  Make a variable called `is_urgent` that is `True` if "urgent" is the first word and `False` otherwise.  As a hint, look at the methods available on strings.  At least one of them will be stunningly useful for our purposes...


# your code goes here


# Question 4
# ----------
# Now, let's define the "danger level" as the number of occurrences of alarming terms computed above. But let's further say that if the message started with "urgent", then will increase the danger level by an additional 3.  This is completely arbitrary, but you get the idea.
# 
# So, now its up to you to compute the danger level.  Try and think of a way to do this without using an "`if`" statement (since we haven't talked about it yet).  If you get stuck, look at the hint below.

# Hint: Since `is_urgent` is a `boolean` value, it can be True or False.  In Python, True is also viewed as `1` for mathematical calculations and False is viewed as `0`.  Try printing out `True * 10` and `False * 10` at the command line and see what happens.  Perhaps this gives you an idea of how you can use the `is_urgent` variable you calculated above as part of the danger level calculation.
# 
# The danger level you calculate should be `9`.


# your code goes here


# Copyright 2008-2016, Enthought, Inc.  
# Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.  
# http://www.enthought.com
