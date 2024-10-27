# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:56:15 2024

@author: Hajanirina
"""

"""
--------------------------------------------------------------------
                         THE CSS PROJECT 1
--------------------------------------------------------------------
"""

import pandas as pd

df = pd.read_csv('movie_dataset.csv')
print(df)

print("Information: \n", df.info(), "\n")
print("Description: \n", df.describe(), "\n")

""" 
REMOVING ALL THE SPACE IN THE COLUMNS NAMES
"""

df.columns = df.columns.str.replace(' ', '_')
print("Information: \n", df.info(), "\n")

"""
DEALING WITH THE MISSING VALUES
"""
# Identification of the columns with NaN values

col_with_missing_value = df.columns[df.isna().any() == True]
print("The columns with the NaNs values: \n", col_with_missing_value.tolist(), "\n")

# Calcul of the median of the columns with NaN values

med_Rev = df["Revenue_(Millions)"].median()
med_Meta = df["Metascore"].median()

# Filling the NaN values of the respective columns by its median

df["Revenue_(Millions)"].fillna(med_Rev, inplace= True)
df["Metascore"].fillna(med_Meta, inplace= True)

print("Description: \n", df.describe(), "\n")

"""
THE HIGHEST RATED MOVIE IN THE DATASET
"""

max_rating = df["Rating"].max()
# print(max_rating)

highest_Rated = df[df["Rating"] == max_rating]
print("The highest rated movie: \n", highest_Rated["Title"].to_string(index=False), "\n")

"""
THE AVERAGE REVENUE OF ALL MOVIES
"""
print("The average revenue of all movie: \n", df["Revenue_(Millions)"].mean(), "\n")

"""
THE AVERAGE REVENUE BETWEEN 2015 AND 2017
"""
# Since 2016 is the recent year in the dataset,
# we can just extract all the date greater or equal to 2015

from_2015_to_2017 = df[df["Year"] >= 2015]
print("The average revenue of movies from 2015 to 2017: \n", from_2015_to_2017["Revenue_(Millions)"].mean(), "\n")

"""
TOTAL OF MOVIES RELEASED IN 2016
"""

Y16 = df[df["Year"] == 2016] # extract all the movies released in 2016
nmbr_2016 = Y16["Year"][Y16["Year"] == 2016].count() # Count the total of movies released in 2016

print("The total of movies released in 2016: \n", nmbr_2016, "\n")

"""
TOTAL OF MOVIES DIRECTED BY CHRISTOPHER NOLAN
"""

Nolan = df[df["Director"] == "Christopher Nolan"] # extract all the movies directed by C. Nolan
print("The total of movies directed by Christopher Nolan: \n", Nolan["Title"].count(), "\n")

"""
THE TOTAL OF MOVIE IN THE DATASET RATED AT LEAST 8.0
"""

rating_8 = df[df["Rating"] >= 8] # extract all the movies have rating at least 8.0
print("The total of movies in the dataset rated at least 8.0: \n", rating_8["Rating"].count(), "\n")

"""
THE MEDIAN RATING OF MOVIES DIRECTED BY CHRISTOPHER NOLAN
"""

print("The median rating of movies directed by Christopher Nolan: \n", Nolan["Rating"].median(), "\n")

"""
THE YEAR WITH THE HIGHEST AVERAGE RATING
"""

each_year = df.groupby('Year').mean() # group all the movies by the year when they realesed and calculate the mean of each rating
high_rating = each_year["Rating"].max() # take the maximum average rating
year_with_high_rating = each_year[each_year["Rating"] == high_rating].index[0] # extract the corresponding year of the max rating
print("The year with the highest average rating: \n", year_with_high_rating, "\n")

"""
THE PERCENTAGE INCREASE IN NUMBER OF MOVIES MADE BETWEEN 2006 AND 2016
"""
Y06 = df[df["Year"] == 2006] # extract all the movies released in 2006
nmbr_2006 = Y06["Year"][Y06["Year"] == 2006].count() # count the number of movies released in 2006
percent_increase = ((nmbr_2016 - nmbr_2006)/nmbr_2006)*100 # compute the percentage rate
print("The percentage increase in number of movies made between 2006 and 2016: \n", percent_increase, "\n")

"""
THE MOST COMMON ACTOR IN ALL THE MOVIES
"""

most_common_actor = df['Actors'].str.split(', ').explode().str.strip().value_counts().idxmax()
print("The most common actor is: \n", most_common_actor, "\n")

"""
THE TOTAL OF UNIQUE GENRES IN THE DATASET
"""

most_common_genre = df['Genre'].str.split(',').explode().str.strip().unique()

print("The total of unique genre in the dataset: \n", len(most_common_genre), "\n")


