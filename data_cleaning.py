#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Notes for data cleaning in Python
Author: Anita Kurm; code is snippets of solutions to DataCamp.com exercises by Daniel Chen
Snippets are not meant to make a coherent script together and just aid way-finding of tools for data cleaning
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




#---------Several plots-----------#
# Add first subplot
plt.subplot(2, 1, 1) 

# Create a histogram of life_expectancy
gapminder.life_expectancy.plot(kind='hist')


# Group gapminder: gapminder_agg
gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()

# Print the head of gapminder_agg
print(gapminder_agg.head())

# Print the tail of gapminder_agg
print(gapminder_agg.tail())

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
gapminder_agg.plot()

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
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


###--------------------------------------###
###-----------COMBINING DATA-------------###
###--------------------------------------###

#-----------Combining rows-----------#
# Concatenate uber1, uber2, and uber3: row_concat (add rows)
row_concat = pd.concat([uber1, uber2, uber3])


#-----------Combining columns (axis = 1)-----------#
# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis = 1)

#or concatenate the DataFrames column-wise (add columns)
gapminder = pd.concat([g1800s, g1900s, g2000s], axis=1)


#-----------Finding files with matching pattern-----------#
# Import necessary modules
import pandas as pd
import glob 

# Write the pattern: pattern
pattern = '*.csv'

# Save all filename matches: csv_files
csv_files = glob.glob(pattern)

# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)


#-----------Merging-----------#
#Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')





###--------------------------------------###
###-----------CLEANING DATA-------------###
###--------------------------------------###


#-----------Checking info-----------#
# Print the info of pd dataframe called tips
print(tips.info())

#-----------Converting-----------#
# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert 'total_bill' to a numeric dtype
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')





#-----------String parsing using regex-----------#
# Import the regular expression module
import re

"""Common regex patterns:
\ - in some cases to escape regex syntax and use symbols literally 
\d - digits
\w -  alphanumeric characters
[A-Z] - any capital letter
{number of symbols to match} - restrict the number of symbols to be matched
* - an arbitrary number of symbols
\s - white space
A-Za-z - any letter upper or lower case
""" 

# Compile the pattern that matches a phone number of the format xxx-xxx-xxxx: prog
prog = re.compile('\d{3}\-\d{3}\-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result2 = prog.match('1123-456-7890')
print(bool(result2))



# Find the numeric values (\d - for any digit, + for matching the previsous element one or more times (ensures 10 is one number): matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)



# Write the first pattern {number of symbols to match}
pattern1 = bool(re.match(pattern='\d{3}\-\d{3}\-\d{4}', string='123-456-7890'))
print(pattern1)

# Write the second pattern (\ to escape regex syntax; * to match an arbirtary number of symbols)
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

# Write the third pattern([A-Z] to match any capital letter; \w* to match an arbitrary number of alphanumeric characters)
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)



#Another case:
# Create the series of countries: countries
countries = gapminder.country

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
#The set of lower and upper case letters.
#Whitespace between words.
#Periods for any abbreviations
pattern = '^[A-Za-z*\s*\.\s*A-Za-z]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~mask

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)



#-----------Custom functions to clean data-----------#
# Define recode_gender() – just an example
# you can also use the replace method. You can also convert the column into a categorical type.
def recode_gender(gender):

    # Return 0 if gender is 'Female'
    if gender == 'Female':
        return 0
    
    # Return 1 if gender is 'Male'    
    elif gender == 'Male':
        return 1
    
    # Return np.nan    (import numpy as np beforehand)
    else:
        return np.nan

# Apply the function to the sex column
#apply on axis 0 (default) will apply the function column-wise
#apply on axis 1 
tips['recode'] = tips.sex.apply(recode_gender)

# Print the first five rows of tips
print(tips.head())



#-----------Lambda functions to clean data-----------#
# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))


#is the same as:

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0]) 
#re.findall gives a list, so [0] is used to get the first element of the list




#-----------Dropping duplicate data-----------#
# Drop the duplicates from df called tracks: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()





#-----------Fillin in missing data-----------#
# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality['Ozone'].fillna(oz_mean)

# Print the info of airquality
print(airquality.info())




#-----------Testing the data with asserts----------#
# Assert that there are no missing values
#.all() method returns True if all values are True
#The first .all() method will return a True or False for each column, while the second .all() method will return a single True or False
assert ebola.notnull().all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()

#if the assert statements did not throw any errors, 
# -> you can be sure that there are no missing values in the data and that all values are >= 0



#another example of asserting:
def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

# Check whether the first column is 'Life expectancy'
assert g1800s.columns[0] == 'Life expectancy'

# Check whether the values in the row are valid
assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Check that there is only one instance of each country
#index 0 of .value_counts() will contain the most frequently occurring value. If this is equal to 1 for the 'Life expectancy' column, then you can be certain that no country appears more than once in the data
assert g1800s['Life expectancy'].value_counts()[0] == 1


