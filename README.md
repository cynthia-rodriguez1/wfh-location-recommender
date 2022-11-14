# Remote Work Location Recommender

**Table of Contents**
<br>[Executive Summary](#executive-summary)
<br>[Data Dictionary](#data-dictionaries)
<br>[Data Acquisition & Cleaning](#data-acquisition-and-cleaning) 
<br>[EDA](#exploratory-data-analysis)
<br>[Building Recommendation Functions](#building-recommendation-functions)
<br>[Conclusion and Next Steps](#conclusion-and-next-steps)


# Executive Summary

**Problem Statement**: TO DO

**Approach & Goal**: TO DO

**Software Requirements**: TO DO


# Data Dictionaries

Due to the usage of several datasets, all data dictionaries are in their respective directories and linked separately here:

- Data dictionary for [Airbnb Dataset](./datasets/airbnbs/airbnb_data_dict.md)
- Data dictionary for [Chain Restaurant Dataset](./datasets/things_to_do/chain_rest_data_dict.md)
- Data dictionary for [Cost of Living Dataset](./datasets/cost_of_living/cost_of_living_data_dict.md)
- Data dictionary for [Weather Dataset](./datasets/weather/weather_data_dict.md)
- Data dictionary for [Walkability Dataset](./datasets/walkability/walkability_data_dict.md)

# Data Acquisition and Cleaning 
Notebook can be viewed [here](./notebooks/01_data_acq_clean.ipynb).

In order to build a system that could recommend a location based on user input, we needed to compile data that coincided with the questions we believe we'd be asking of the user. Below are brief summaries of the datasets used, as well as the sources.

Datasets:
<br>Airbnb Data - 279k observations 
- 13 features for each Airbnb listing including neighborhood, price per night, and minimum nights required for booking, all downloaded from [Inside Airbnb](http://insideairbnb.com/get-the-data/).

<br>Chain Restaurant Data - 155k observations 
- 13 features relating to each restaurant listed, including name, type of cuisine, urban area location, and whether the restaurant qualifies as a chain. Data provided courtesy of [Friendly Cities Lab](https://github.com/friendlycities-gatech/chainness).

<br>Cost of Living Data - 33 observations 
- 16 features relating to various socioeconomic and political characteristics of each location. Data was pulled from [BestPlaces.net](https://www.bestplaces.net/) for each location and aggregated.

<br>Weather Data - 33 observations 
- Two separate datasets detailing monthly temperature and rainfall trends for each location, from [The National Centers for Environmental Information](https://www.ncei.noaa.gov/). Data was aggregated into one larger dataset for EDA usage.

<br>Walkability Data - 40k observations 
- 46 features for each census block including population demographics, auto and transit scores, and walkability from the [US Environmental Protection Agency](https://www.epa.gov/smartgrowth/smart-location-mapping#walkability).

# Exploratory Data Analysis 
Notebook can be viewed [here](./notebooks/02_eda.ipynb).

The purpose of this notebook is to explore the various aspects in each of the datasets, helping us to hone in on the useful features that can be used in our functions and identify any patterns or inconsistencies that might cause problems when making recommendations. Following are summaries/examples of the explorations conducted:

**Key Findings** 

TO DO
  

# Building Recommendation Functions 
Notebook can be viewed [here](./notebooks/03_building_rec_function.ipynb).

TO DO

# Conclusion and Next Steps

**BULLET POINT 1**

TO DO

**BULLET POINT 2**

TO DO

**BULLET POINT 3**

TO DO

**NEXT STEPS**

- TO DO 1
- TO DO 2

**Presentation**

See [here](TO DO) for a brief, fairly non-technical presentation summarizing our data collection process, exploration, and final recommendation system.

**Works Cited**
Please see [here](TO DO) for an exhaustive list of resources used in this project.