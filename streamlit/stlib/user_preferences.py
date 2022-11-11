import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from time import sleep
import datetime
from datetime import date

icon = Image.open('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/streamlit/images/us1.jpeg')
st.set_page_config(page_title='Remote Work Location Recommender', page_icon = icon)

def empty():
    next_page.empty()
    sleep(0.5)

next_page = st.empty()

# place = 'New York City, NY'
st.button('Click here to select a new location')


st.title('You selected: New York City, NY')
image = Image.open('/Users/cynthiarodriguez/Desktop/DSI-822/Projects/wfh-location-recommender/streamlit/stlib/nyc.jpg')
st.image(image)

st.header("Let's answer a few questions.")

# Button to return to home page
# with st.sidebar:
#     st.button('Click here to select a new location.')

# Trip dates
st.subheader('1.  When would you plan on going?')
trip_dates = st.date_input('Select your date range', value = (date.today(), datetime.date(2022, 11, 30)), max_value = datetime.date(2024, 12, 31))
st.write(str(trip_dates[0]), str(trip_dates[1]))

# Number of guests
st.subheader('2.  How many people would you be staying with?')
total_guests = st.number_input('Enter the total amount of guests', min_value = 1, step = 1)

# Weather preferences
st.subheader('3.  What is your ideal temperature range?')
weather = st.slider('Weather preference', min_value = None, max_value = 120, value=(0, 25), label_visibility = 'collapsed')
st.write(weather[0], weather[1])
# st.write('Range: ', weather)

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

# Monthly budget
st.subheader('10.  How much are you willing to spend on accomodations each month?')
budget_range = st.number_input('Monthly budget range', min_value = 0, step = 1, label_visibility = 'collapsed')
st.write('Budget: ', budget_range)

def rec_results():
    # url = ('https://www.airbnb.com/s/Bedford~Stuyvesant--New-York--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&query=Bedford-Stuyvesant%2C%20NY&place_id=ChIJIbiotnVcwokR3OuRZieHvPM&date_picker_type=calendar&checkin=' + str(trip_dates[0]) + '&checkout=' + str(trip_dates[1]) + '&adults=2&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=30')
    link = '[here.](https://www.airbnb.com/s/Bedford~Stuyvesant--New-York--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&query=Bedford-Stuyvesant%2C%20NY&place_id=ChIJIbiotnVcwokR3OuRZieHvPM&date_picker_type=calendar&checkin=' + str(trip_dates[0]) + '&checkout=' + str(trip_dates[1]) + '&adults=' + str(total_guests) + '&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=30)'
    st.subheader('You should go to: Bedford-Stuyvesant!')
    col1, col2 = st.columns(2)
    col1.metric('Average Price per Month', '$1,200')
    col2.metric("Average Temperature in Spring", "70 °F")
    st.write('Check it out ', link, unsafe_allow_html = True)

if st.button('Submit') == True:
    empty()
    with next_page.container():
        rec_results()
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
