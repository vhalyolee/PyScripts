#!/usr/bin/python

# coding: utf-8

# An Example of Sets in Action
# ============================
# 
# Here we're going to work through an example of working with sets that is borrowed from the Python documentation.
# 
# The idea is that there is a company that has sets of employees---engineers, programmers and managers---and these groups can overlap:

# In[ ]:

engineers = {'John', 'Jane', 'Jack', 'Janice'}
programmers = {'Jack', 'Sam', 'Susan', 'Janice'}
managers = {'Jane', 'Jack', 'Susan', 'Zack'}


# So, for example, Jack is an engineer, programmer and a manager as well.
# 
# We can look at these, for example, to see the set of engineers:

# In[ ]:

print engineers


# One thing we'd like to do is to create a set that is all the employees.  We can do this with:

# In[ ]:

employees = engineers | programmers | managers
print employees


# This is everyone that is in the company.
# 
# You might also want to know who is in a full-time management role, so that would be:

# In[ ]:

managers_only = managers - engineers - programmers
managers_only


# And we see that Zack is the only person in a purely management role.
# 
# Now we might want to add a new employee, say "Marvin" to the engineers, so we could do this by:

# In[ ]:

engineers.add('Marvin')
engineers


# Or perhaps another company was acquired, represented by another set of engineers:

# In[ ]:

acme_engineers = {'Joe', 'Elaine'}


# And in this case you can add this to the set of engineers:

# In[ ]:

engineers.update(acme_engineers)
engineers


# We can check that we have included everyone from Acme engineering by using set containment operations:

# In[ ]:

engineers >= acme_engineers


# and this is indeed True.
# 
# If you have one element you can check that is an element of the set using the `in` operator, just like with lists.  So if we wanted to see if Joe is an engineer, we can use:

# In[ ]:

'Joe' in engineers


# and that's true, but if we instead did:

# In[ ]:

'Zack' in engineers


# we see this is false, because Zack is only in the set of managers.

# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
