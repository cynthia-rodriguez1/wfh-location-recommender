import numpy as np
import pandas as pd
import re
import streamlit as st
from PIL import Image
from time import sleep
import datetime
from datetime import date
import user_input_converter
import generate_rec

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

def show_rec(df):

    final_rec = generate_rec.find_rec(df)
    string = 'You should go to: ' + str(final_rec) + '!'
    st.header(string)


    rec_image_display = Image.open('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/images/location_images/' + str(final_rec) + '.jpg')
    st.image(rec_image_display)

    # Here we're grabbing the average temperature for the user's selected month(s) to display
    # Finding the length of the trip
    trip_dates_diff = (trip_dates[1].month - trip_dates[0].month)
    # Creating a season dictionary if the trip is longer than one month
    season_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
    # If the selected dates fall in one month only, we'll return the average temp for that month
    if trip_dates_diff == 0:
        trip_season = trip_dates[1].strftime('%b')
        display_month = trip_dates[1].strftime('%B')
    # If the selected dates span across multiple months, we'll return the average temp for the closest season to the selected dates
    elif trip_dates_diff <= 2:
        trip_season = (season_dict[(trip_dates[0].month)])
        display_month = trip_season
    # However, if the user selected a 4-month or longer date range, we'll return the average temp for only the last season in the selection
    else:
        trip_season = (season_dict[(trip_dates[1].month)])
        display_month = trip_season

    # Displaying what the average temp is in the designated month/season
    season_display_text = 'Average Temperature in ' + display_month

    # Reading in our weather dataframe to pull temperatures from
    weather = pd.read_csv('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/datasets/cleaned_data/weather_combined.csv')
    # Reformatting the location name to match our function output
    weather['place'] = weather[['place', 'state']].apply(lambda x: ', '.join(x), axis=1)
    # Creating an index to help us look up our location
    full_df_indices = pd.Series(df.index, index=df['place'])
    weather_indices = pd.Series(weather.index, index = weather['place'])
    weather_lookup_col = trip_season.lower() + '_avg_temp'

    # Lastly, going into both dataframes using our defined indices to pull out the average monthly price and temperature for the user's recommended location
    expected_monthly_price = (df.iloc[(full_df_indices[final_rec])]['avg_monthly_price'])
    expected_temp = str(round(weather.iloc[(weather_indices[final_rec])][weather_lookup_col], 1)) + '°F'

    # Displaying using streamlit's metric display element
    col1, col2 = st.columns(2)
    col1.metric('Average Price per Month', '${:,.0f}'.format(expected_monthly_price))
    col2.metric(season_display_text, expected_temp)

    # This dataframe contains all of Airbnb's individual place IDs for each of our recommendation possibilities
    place_id_df = pd.read_csv('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/datasets/airbnb_place_id.csv')
    place_id_indices = pd.Series(place_id_df.index, index = place_id_df['place'])
    # Pulling the place ID from the above dataframe for the user's recommended location and appending to use in the Airbnb URL
    final_rec_place_id = (place_id_df.iloc[(place_id_indices[final_rec])]['place_id']) + '&'

    # String modification to build our specific landing page to the user's selections
    # Splitting each word
    rec_split_list = re.split(r'\W+', final_rec.replace(',', ''))
    # Defining variables for the city and state
    rec_split_list_city = '-'.join([i for i in rec_split_list[:-1]])
    rec_split_list_state = rec_split_list[-1]
    # This is specific to Airbnb's URL format
    pct_20 = ('%20'.join([i for i in rec_split_list[:-1]]) + '%2C' + '%20' + rec_split_list_state)

    # Generating the full link
    link = '[here.](https://www.airbnb.com/s/' + rec_split_list_city + '--' + rec_split_list_state + '--USA/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=' + pct_20 + '&date_picker_type=calendar&place_id=' + final_rec_place_id + check_in + check_out + num_guests + '&source=structured_search_input_header&search_type=autocomplete_click)'
    st.write('Check it out ', link, unsafe_allow_html = True)
