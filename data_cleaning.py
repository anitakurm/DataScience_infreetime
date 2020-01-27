#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Notes for data cleaning in Python
Author: Anita Kurm; code is solutions to DataCamp.com exercises by Daniel Chen
"""

import pandas as pd

df = pd.read_csv("url/filename")

###--------------------------------------###
###-----------Data inspection------------###
###--------------------------------------###

#df.head(), df.tail(), df.info() are methods, whereas df.shape and df.columns are attributes
print(df.head())
print(df.tail())
print(df.info())

print(df.shape)
print(df.columns)

#frequency counts (incl. nan values) .value_counts(dropna = False)
print(df['Borough'].value_counts(dropna=False))



###--------------------------------------###
###---------Data visualization-----------###
###--------------------------------------###

# Import matplotlib.pyplot, you need pandas too
import matplotlib.pyplot as plt


#-----------Histogram-----------#
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy= True)
plt.show()


#-----------Boxplot-----------#
df.boxplot(column="initial_cost", by="Borough", rot=90)
plt.show()


#-----------Scatter plot-----------#
# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()



###--------------------------------------###
###--------------RESHAPING---------------###
###--------------------------------------###

#-----------Melt-----------#
#id_vars - columns to keep as is 
# e.g.:
airquality_melt = pd.melt(airquality, id_vars='Date')

#or also give column names
airquality_melt = pd.melt(airquality, id_vars='Date', var_name='measurement', value_name='reading')



#-----------Pivot-----------#
airquality_pivot = airquality_melt.pivot_table(index='Date', columns='measurement', values='reading')

#reset index to get back the original DataFrame
airquality_pivot_reset = airquality_pivot.reset_index()

#pivoting with duplicate values - use .pivot_table() with a specified aggregating function
import numpy as np
airquality_pivot = airquality_dup.pivot_table(index='Date', columns='measurement', values='reading', aggfunc=np.mean)



#-----------Splitting columns using .str[index]-----------#
# Melt tb: tb_melt
tb_melt = pd.melt(tb, id_vars=['country', 'year'])

# Create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
tb_melt['age_group'] = tb_melt.variable.str[1:]

# Print the head of tb_melt
print(tb_melt.head())



#-----------Splitting columns using .str.split and .str.get-----------#
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

# Create the 'str_split' column - will contain several elements
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

# Create the 'type' column - get the value by giving an index of the relevant element
ebola_melt['type'] = ebola_melt['str_split'].str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt['str_split'].str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())