# Writing a Data Science Blog Post
## Udacity Data Science Nanodegree

This is a repository for Data Scientist Nanodegree program's first project. It contains the source code of the project "Write a Data Science Blog Post" that was generated to write the project's [blog post](https://medium.com/@locmelis.audris/getting-a-virtual-break-in-copenhagen-99c9abf2bfc2).

## Motivation
Using AirBnB data from Copenhagen I will try to answer the following 3+ questions.

1. Which neighbourhoods are the nicest to stay in?
    * Best average rating
    * Best location
    * Other important differentiators?
2. How does a map of most desireable locations in Copenhagen look like?
3. Predicting the rating
    * What are the strongest positive or negative predictors for the rating of a listing?

## Files
* **.gitignore** - file specifying what types of files not to include in the repository
* **README.md** - this file
* **Copenhagen_AirBnB.ipynb** - project notebook

## Data
The data used is AirBnB data from Copenhagen, Denmark. 
http://insideairbnb.com/get-the-data.html

## Requirements
You have to have the followin libraries installed: `numpy, pandas, matplotlib, plotly, statistics, sklearn, pandas_profiling`

## Summary
There are 6 neighborhoods with the average location score above the average score across all listings (i.e., 9.59). Also, the less frequent neighborhoods with less than a 100 listings have a rather high location score.

For predicting the rating there were top 3 positive and negative factors identified.
* Positive: real bed types, non-traditional properties, superhost status\*
* Negative: super strict cancellation policy, shared room, hotel room.
