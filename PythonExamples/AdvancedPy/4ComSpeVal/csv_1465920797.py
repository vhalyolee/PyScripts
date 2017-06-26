
# coding: utf-8

# Comma Separated Values
# ======================
# 
# The Python Standard Libarary can read and write CSV (and similar) formatted files using the `csv` module.
# 

# In[1]:

import csv


# For example, to read a file `data.csv` containing the following:
# 
#     "alpha 1",  100, -1.443
#     "beta  3",   12, -0.0934
#     "gamma 3a", 192, -0.6621
#     "delta 2a",  15, -4.515

# In[2]:

data = '''"alpha 1",  100, -1.443
"beta  3",   12, -0.0934
"gamma 3a", 192, -0.6621
"delta 2a",  15, -4.515
'''
with open("data.csv", "wb") as f:
    f.write(data)


# you first create a `reader` on the file:

# In[3]:

r = csv.reader(open("data.csv"))


# and then you can iterate over the rows of the file using `r`:

# In[4]:

for row in r:
    print row


# Notice that the values read in are provided as strings, so you need to do any appropriate type conversion yourself:

# In[5]:

with open("data.csv") as fp:
    data = []
    for row in csv.reader(fp):
        data.append([row[0], int(row[1]), float(row[2])])

data


# Writing to a csv file is similarly straightforward with a `csv.writer`:

# In[6]:

data = [("One", 1, 1.5), ("Two", 2, 8.0)]
with open("out.csv", "wb") as fp:
    w = csv.writer(fp)
    w.writerows(data)


# In[7]:

get_ipython().system(u'cat "out.csv"')


# Notice that we open the file with the write binary flag `"wb"` which ensures that end-of-lines are handled correctly in a cross-platform manner by the `csv` module.
# 
# By default, the readers and writers produce CSV files which are compatible with those produced and consumed by Excel.  This includes how parts of the file can be quoted and escaped.  So for example, if we wanted to write data which contains quotes and commas, the `csv` module handles it correctly:

# In[8]:

data = [("One, \"real\" string", 1, 1.5), ("Two", 2, 8.0)]
with open("out.csv", "wb") as fp:
    w = csv.writer(fp)
    w.writerows(data)


# In[9]:

get_ipython().system(u'cat out.csv')


# You can customize the way these are handled through options that you pass to the `reader` and `writer` objects.
# 
# For example, if you want to read or write a pipe-separated values file, you can set the `delimiter` argument to `"|"`.

# In[10]:

with open("out.psv", "wb") as fp:
    w = csv.writer(fp, delimiter="|")
    w.writerows(data)


# In[11]:

get_ipython().system(u'cat out.psv')


# Other Options
# =============
# 
# It's worth remembering that for CSV files which contain lots of numerical data both `numpy.loadtxt` and `pandas.read_csv` can simplify reading the data in.
# 
# For example, given "trades.csv":
# 
#     Order,Date,Stock,Quantity,Price
#     A0001,2013-12-01,AAPL,1000,203.4
#     A0002,2013-12-01,MSFT,1500,167.5
#     A0003,2013-12-02,GOOG,1500,167.5

# In[12]:

data = """Order,Date,Stock,Quantity,Price
A0001,2013-12-01,AAPL,1000,203.4
A0002,2013-12-01,MSFT,1500,167.5
A0003,2013-12-02,GOOG,1500,167.5
"""
with open("trades.csv", "wb") as f:
    f.write(data)


# Pandas makes turning this into a usable data structure very simple.

# In[13]:

import pandas
df = pandas.read_csv("trades.csv", index_col=0)
print df


# In[14]:

(df["Quantity"]*df["Price"])["A0001"]


# Copyright 2008-2016, Enthought, Inc.<br>Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.<br>http://www.enthought.com
