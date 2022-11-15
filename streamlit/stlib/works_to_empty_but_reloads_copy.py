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
import show_rec

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity


icon = Image.open('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/streamlit/images/us1.jpeg')
st.set_page_config(page_title='Remote Work Location Recommender', page_icon = icon)

st.markdown("<style>.element-container{opacity:1 !important}</style>", unsafe_allow_html=True)

def empty():
    next_page.empty()
    sleep(0.5)

next_page = st.empty()

rec_df = pd.read_csv('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/streamlit/location_features_df.csv')

# place = 'New York City, NY'
# st.button('Click here to select a new location')

with next_page.container():


    st.title('Where should you go next?')
    image = Image.open('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/images/location_images/New York City, NY.jpg')
    st.image(image)

    st.header("Let's answer a few questions.")

    # Button to return to home page
    # with st.sidebar:
    #     st.button('Click here to select a new location.')

    # 1. Trip dates
    st.subheader('1.  When would you plan on going?')
    trip_dates = st.date_input('Select your date range', value = (date.today(), datetime.date(2022, 11, 30)), max_value = datetime.date(2024, 12, 31))
    check_in = '&checkin=' + str(trip_dates[0]) + '&'
    check_out = 'checkout=' + str(trip_dates[1])
    # global trip_dates, check_in, check_out
    # st.write(str(trip_dates[0]), str(trip_dates[1]))

    # 2. Number of guests
    st.subheader('2.  How many people would you be staying with?')
    total_guests = st.number_input('Enter the total amount of guests', min_value = 1, step = 1)
    num_guests = '&adults=' + str(total_guests)
    # global num_guests

    # 3. Weather preference
    st.subheader('3.  What is your ideal temperature range?')
    selected_weather_pref = st.slider('Weather preference', min_value = None, max_value = 120, value=(0, 25), label_visibility = 'collapsed')
    st.write(selected_weather_pref[0], selected_weather_pref[1])
    min_temp = selected_weather_pref[0]
    max_temp = selected_weather_pref[1]
    # st.write('Range: ', weather)

    # 4. Chain preference
    chain_options = ('I only eat at Mom-n-Pop restaurants', 'I prefer non-chain restaurants', 'I like a combination of both', 'I would rather go somewhere that has a drive-thru', 'The faster the food the better')
    st.subheader("4. If you aren't eating at home, which of these best describes your meal preferences?")
    selected_chain_pref = st.radio('Chain pref', options = chain_options, index = 2, label_visibility = 'collapsed')
    # st.write('Chain pref: ', selected_chain_pref)

    # 5. Walkability preference
    walk_importance_options = ('Not important at all', 'Not very important', 'Neutral', 'A little important', 'Extremely important')
    st.subheader('5.  How important is walkability?')
    selected_walk_pref = st.select_slider('Walkability', options = walk_importance_options, value = 'Neutral', label_visibility = 'collapsed')
    # st.write('Importance: ', selected_walk_pref)

    # 6. Political lean preference
    st.subheader('6. Do you care about the political lean of the city you would be living in?')
    pol_pref_options = ('Strong left lean preferred', 'Moderate left lean preferred', 'Moderate right lean preferred', 'Strong right lean preferred')
    pol_yes_no = st.radio('Political pref starter', options=['Yes', 'No'], index= 1, horizontal = True, label_visibility = 'collapsed')
    if pol_yes_no == 'No':
        selected_pol_pref = 'Neutral'
    else:
        selected_pol_pref = st.select_slider('Select your preferred political environment:', options = pol_pref_options, value = 'Moderate left lean preferred', label_visibility = 'visible')

    # 7. Miscellaneous costs
    misc_cost_options = ('Clothing', 'Concerts', 'Dining out', 'Entertainment', 'Bars/Clubs')
    st.subheader('7. Which of these are you likely to participate in/spend money on?')
    selected_misc_costs = st.multiselect('Miscellaneous costs', options = misc_cost_options, label_visibility = 'collapsed')
    misc_costs_count = len(selected_misc_costs)

    # 8. Monthly budget
    st.subheader('8.  How much are you willing to spend on accomodations each month?')
    selected_budget = st.number_input('Monthly budget range', min_value = 0, step = 1, label_visibility = 'collapsed')
    # st.write('Budget: ', selected_budget)

    user_input = [min_temp, max_temp, selected_chain_pref, selected_walk_pref, selected_pol_pref, misc_costs_count, selected_budget]

    # return user_input

    # converted_list = user_input_converter.wfh_input_converter(user_input, rec_df)
    #
    # final_rec = generate_rec.find_rec(rec_df)
    #
    # return final_rec, check_in, check_out, trip_dates, num_guests

# with next_page.container():
    # user_input, check_in, check_out, trip_dates, num_guests = main_page()
    # main_page()
    # main_page_run = st.cache(main_page())

# New list of converted input data
    new_list = st.cache(user_input_converter.wfh_input_converter(user_input, rec_df))



    if st.button('Submit') == True:
        with next_page.container():
            empty()
        # show_rec.show_rec(rec_df)
            final_rec = generate_rec.find_rec(rec_df)
            st.header('You should go to: ' + str(final_rec) + '!')



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
            full_df_indices = pd.Series(rec_df.index, index=rec_df['place'])
            weather_indices = pd.Series(weather.index, index = weather['place'])
            weather_lookup_col = trip_season.lower() + '_avg_temp'

                # Lastly, going into both dataframes using our defined indices to pull out the average monthly price and temperature for the user's recommended location
            expected_monthly_price = (rec_df.iloc[(full_df_indices[final_rec])]['avg_monthly_price'])
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