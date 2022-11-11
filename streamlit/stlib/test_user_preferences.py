import numpy as np
import pandas as pd
import re
import streamlit as st
from PIL import Image
from time import sleep
import datetime
from datetime import date
import user_input_converter
# import generate_rec

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

icon = Image.open('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/streamlit/images/us1.jpeg')
st.set_page_config(page_title='Remote Work Location Recommender', page_icon = icon)

def empty():
    next_page.empty()
    sleep(0.5)

next_page = st.empty()

df = pd.read_csv('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/streamlit/test_df.csv')

# place = 'New York City, NY'
st.button('Click here to select a new location')


st.title('Where should you go next?')
# image = Image.open('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/streamlit/stlib/nyc.jpg')
# st.image(image)

st.header("Let's answer a few questions.")

# Button to return to home page
# with st.sidebar:
#     st.button('Click here to select a new location.')

# Trip dates
st.subheader('1.  When would you plan on going?')
trip_dates = st.date_input('Select your date range', value = (date.today(), datetime.date(2022, 11, 30)), max_value = datetime.date(2024, 12, 31))
check_in = str(trip_dates[0]) + '&'
check_out = 'checkout=' + str(trip_dates[1])
st.write(str(trip_dates[0]), str(trip_dates[1]))

# Number of guests
st.subheader('2.  How many people would you be staying with?')
total_guests = st.number_input('Enter the total amount of guests', min_value = 1, step = 1)
num_guests = '&adults=' + str(total_guests)

# Weather preferences
st.subheader('3.  What is your ideal temperature range?')
weather = st.slider('Weather preference', min_value = None, max_value = 120, value=(0, 25), label_visibility = 'collapsed')
st.write(weather[0], weather[1])
min_temp = weather[0]
max_temp = weather[1]
# st.write('Range: ', weather)

# Food preferences
food_options = ('I only eat at Mom-n-Pop restaurants', 'I prefer non-chain restaurants', 'I like a combination of both', 'I would rather go somewhere that has a drive-thru', 'The faster the food the better')
st.subheader("4. If you aren't eating at home, which of these best describes your meal preferences?")
food_pref_selected = st.radio('Food pref', options = food_options, index = 2, label_visibility = 'collapsed')
st.write('Chain pref: ', food_pref_selected)

# Walkability
importance_range = ('Not important at all', 'Not very important', 'Neutral', 'A little important', 'Extremely important')
st.subheader('4.  How important is walkability?')
walkability = st.select_slider('Walkability', options = importance_range, value = 'Neutral', label_visibility = 'collapsed')
st.write('Importance: ', walkability)

# Miscellaneous costs
misc_cost_options = ('Clothing', 'Concerts', 'Dining out', 'Entertainment', 'Bars/Clubs')
st.subheader('5. Which of these are you likely to participate in/spend money on?')
misc_cost = st.multiselect('Miscellaneous costs', options = misc_cost_options, label_visibility = 'collapsed')
st.write('Miscellaneous costs selected: ', misc_cost)
st.write(len(misc_cost))
misc_costs_selected = len(misc_cost)

# Monthly budget
st.subheader('10.  How much are you willing to spend on accomodations each month?')
budget_range = st.number_input('Monthly budget range', min_value = 0, step = 1, label_visibility = 'collapsed')
st.write('Budget: ', budget_range)

user_input = [min_temp, max_temp, food_pref_selected, walkability, 'Moderate left lean preferred', misc_costs_selected, budget_range]
st.write(user_input)

# New list of converted input data
new_list = user_input_converter.wfh(user_input, df)
st.write(new_list)
# st.write(type(new_list))
# st.write(df.columns)

# Finding cosine similarities of new df
# Scaling all numeric columns
feature_cols = df.columns[1:]
sc = MinMaxScaler()
scaled_df = sc.fit_transform(df[feature_cols])

# Setting model and indices for reference
indices = pd.Series(df.index, index=df['place'])
cs_df = cosine_similarity(scaled_df)

# Running function to generate recommendation
def find_rec(input_row, model):
    # input_row = 'User Input'
    #
    # model = cs_df

    # '''Indexing the user input row'''
    index = indices[input_row]

    # '''Filtering and sorting the cosine similarity values for input data'''
    sim_scores = list(enumerate(model[index]))
    sim_scores_sorted = sorted(sim_scores, key = lambda x:x[1], reverse=True)

    # '''Finding and returning the location most similar to user's preferences'''
    best_fit_score = sim_scores_sorted[1]
    best_fit_index = best_fit_score[0]
    recommended_place = df['place'].iloc[best_fit_index]

    return recommended_place

final_rec = find_rec('User Input', cs_df)

st.write('You should go to: ', final_rec)
rec_split_list = re.split(r'\W+', final_rec.replace(',', ''))
st.write(rec_split_list)
st.write([i for i in rec_split_list[:-1]])
rec_split_list_city = '-'.join([i for i in rec_split_list[:-1]])
rec_split_list_state = rec_split_list[-1]
pct_20 = ('%20'.join([i for i in rec_split_list[:-1]]) + '%2C' + '%20' + rec_split_list_state)
st.write(rec_split_list_state)
link = '[here.](https://www.airbnb.com/s/' + rec_split_list_city + '--' + rec_split_list_state + '--USA/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=' + pct_20 + '&date_picker_type=calendar&place_id=ChIJOwg_06VPwokRYv534QaPC8g&checkin=' + check_in + check_out + num_guests + '&source=structured_search_input_header&search_type=autocomplete_click)'
st.write('Check it out ', link, unsafe_allow_html = True)

expected_monthly_price = (df.iloc[(indices[final_rec])]['avg_monthly_price'])
# expected_temp =

col1, col2 = st.columns(2)
col1.metric('Average Price per Month', '${:,.0f}'.format(expected_monthly_price))
col2.metric("Average Temperature in Spring", "70 °F")

st.write(check_in)

st.write(df)
# Defining

# def rec_results():
#     # url = ('https://www.airbnb.com/s/Bedford~Stuyvesant--New-York--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&query=Bedford-Stuyvesant%2C%20NY&place_id=ChIJIbiotnVcwokR3OuRZieHvPM&date_picker_type=calendar&checkin=' + str(trip_dates[0]) + '&checkout=' + str(trip_dates[1]) + '&adults=2&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=30')
#     link = '[here.](https://www.airbnb.com/s/Bedford~Stuyvesant--New-York--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&query=Bedford-Stuyvesant%2C%20NY&place_id=ChIJIbiotnVcwokR3OuRZieHvPM&date_picker_type=calendar&checkin=' + str(trip_dates[0]) + '&checkout=' + str(trip_dates[1]) + '&adults=' + str(total_guests) + '&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=30)'
#     st.subheader('You should go to: Bedford-Stuyvesant!')
#     col1, col2 = st.columns(2)
#     col1.metric('Average Price per Month', '$1,200')
#     col2.metric("Average Temperature in Spring", "70 °F")
#     st.write('Check it out ', link, unsafe_allow_html = True)

# if st.button('Submit') == True:
#     empty()
#     with next_page.container():
#         rec_results()
        # link = '[here.](https://www.airbnb.com/s/Bedford~Stuyvesant--New-York--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&price_filter_input_type=0&price_filter_num_nights=28&query=Bedford-Stuyvesant%2C%20NY&place_id=ChIJIbiotnVcwokR3OuRZieHvPM&date_picker_type=flexible_dates&flexible_trip_dates%5B%5D=march&flexible_trip_dates%5B%5D=may&flexible_trip_dates%5B%5D=april&adults=1&source=structured_search_input_header&search_type=filter_change&flexible_trip_lengths%5B%5D=one_month)'
        # st.subheader('You should go to: Bedford-Stuyvesant!')
        # col1, col2 = st.columns(2)
        # col1.metric('Average Price per Month', '$1,200')
        # col2.metric("Average Temperature in Spring", "70 °F")
        # st.write('Check it out ', link, unsafe_allow_html = True)

# Bring in model/new page with recommendation
# link = '[here.](https://www.airbnb.com/s/Bedford~Stuyvesant--New-York--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&price_filter_input_type=0&price_filter_num_nights=28&query=Bedford-Stuyvesant%2C%20NY&place_id=ChIJIbiotnVcwokR3OuRZieHvPM&date_picker_type=flexible_dates&flexible_trip_dates%5B%5D=march&flexible_trip_dates%5B%5D=may&flexible_trip_dates%5B%5D=april&adults=1&source=structured_search_input_header&search_type=filter_change&flexible_trip_lengths%5B%5D=one_month)'
# st.subheader('You should go to: Bedford-Stuyvesant!')
# col1, col2 = st.columns(2)
# col1.metric('Average Price per Month', '$1,200')
# col2.metric("Average Temperature in Spring", "70 °F")
# st.write('Check it out ', link, unsafe_allow_html = True)
