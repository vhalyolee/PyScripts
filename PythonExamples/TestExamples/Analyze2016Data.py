!#/bin/python



# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import numpy as np

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)



#location = r'/home/beanie/MyWorkplace/PythonExamples/TestExamples/2016NationalPopularVoteTracker_v2.csv'

# I had to change in the csv type the % values to regular numeric values (in the html)

location = r'/home/beanie/MyWorkplace/PythonExamples/TestExamples/2016NationalPopularVoteTracker_v2.csv'

df1 = read_csv(location)


print df1

df1.head(5)

df1.tail

df1.shape

df1.columns


df2 = df1.copy()

 df2.columns = ['title','State',  'Clinton',  'Trump', 'Others',  'Clinton %'  ,' Trump %', 'Others %', '2012 Dem margin', '2016 Dem margin','margin shift',  'total 12 votes','total 16 votes','raw vs 12']

from numpy import array

swinga = array(range(12,25))
df2_sub_swing= df2.iloc[swinga,[1,2,3,4,5,6,7,9]]


print df2_sub_swing

print df2_sub_swing.shape

print df2_sub_swing.dtypes


df2_sub_swing[['Clinton',  'Trump', 'Others','Clinton %',' Trump %', 'Others %', '2016 Dem margin']]=df2_sub_swing[['Clinton',  'Trump', 'Others','Clinton %',' Trump %', 'Others %', '2016 Dem margin']].apply(pd.to_numeric)

print df2_sub_swing.dtypes

# need to learn to use whats below
#df.apply(lambda x: pd.to_numeric(x, errors='ignore'))


nswinga= array(range(27,65))

df2_sub_nswing= df2.iloc[nswinga,[1,2,3,4,5,6,7,9]]

print df2_sub_nswing

df2_sub_nswing.shape

print df2_sub_nswing.dtypes

df2_sub_nswing[['Clinton',  'Trump', 'Others','Clinton %',' Trump %', 'Others %', '2016 Dem margin']]=df2_sub_nswing[['Clinton',  'Trump', 'Others','Clinton %',' Trump %', 'Others %', '2016 Dem margin']].apply(pd.to_numeric)

print df2_sub_nswing.dtypes

allstatesa = concatenate((swinga,nswinga),axis=0)

df2_sub_allstates = df2.iloc[allstatesa,[1,2,3,4,5,6,7,9]]

print df2_sub_allstates

print df2_sub_allstates.shape

print df2_sub_allstates.dtypes

df2_sub_allstates[['Clinton',  'Trump', 'Others','Clinton %',' Trump %', 'Others %', '2016 Dem margin']]=df2_sub_allstates[['Clinton',  'Trump', 'Others','Clinton %',' Trump %', 'Others %', '2016 Dem margin']].apply(pd.to_numeric)

print df2_sub_allstates.dtypes


# problem is the % in the column data

df2_sub_swing['Clinton'].max()
df2_sub_swing['Clinton'].plot()

#test = df2_sub_swing.groupby('State')

ax = df2_sub_nswing[['Clinton','Trump','Others']].plot(kind='bar', title ="Swing States",color = ['blue', 'red', 'green'],  figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("States", fontsize=12)
ax.set_ylabel("Voters", fontsize=12)
plt.show()

# Pull plot for Clinton and Trump  (x_i-mean)/std
for i in df2_sub_swing.index:
    print df2_sub_swing.ix[i, 'Clinton'] 




def PullDis(df,colname,outputarray):
    """ Calculate Pull distribution """
    j=-1
    for i in df.index:
        j=j+1
        outputarray[j] = (df.ix[i,colname]-df[colname].mean())/df[colname].std()


#      
#        print outputarray
outputarray = zeros(df2_sub_swing['Clinton'].size)
PullDis(df2_sub_swing,'Clinton',outputarray)
plt.hist(outputarray)
plt.title("Pull Dis Histogram")
plt.xlabel("Value")
plt.ylabel("Pull Dis")
plt.show()

#hist, bin_edges = np.histogram(outputarray)
#print (bin_edges)
#print hist
#plt.bar(bin_edges[:-1], hist)
#plt.xlim(min(bin_edges), max(bin_edges))
#plt.show()




allstatesa = zeros(df2_sub_allstates['Trump'].size)
PullDis(df2_sub_allstates,'Trump',allstatesa)
plt.hist(allstatesa)
plt.title("Pull Dis Histogram")
plt.xlabel("Value")
plt.ylabel("Pull Dis")
plt.show()






