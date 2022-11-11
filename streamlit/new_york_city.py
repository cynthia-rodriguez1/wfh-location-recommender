import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from time import sleep
import main_test

# def empty():
#     next_page.empty()
#     sleep(0.5)
#
# next_page = st.empty()

# def back_to_main():
#     empty()
#     with next_page.container():
#         st.title('Where do you want to go?')
#
#         places = ('Asheville, NC', 'Austin, TX', 'Boston, MA', 'Cambridge, MA',
#     'Chicago, IL', 'Columbus, OH', 'Dallas, TX', 'Denver, CO',
#     'Fort Lauderdale, FL', 'Fort Worth, TX', 'Hawaii, HI', 'Jersey City, NJ', 'Las Vegas, NV', 'Los Angeles, CA',
#     'Nashville, TN', 'New Orleans, LA', 'Newark, NJ', 'New York City, NY', 'Oakland, CA', 'Portland, OR',
#     'Rhode Island, RI', 'Salem, OR', 'San Diego, CA', 'San Francisco, CA', 'San Mateo, CA', 'Santa Clara, CA',
#     'Santa Cruz, CA', 'Seattle, WA', 'Twin Cities, MN', 'Washington DC')
#
#     # Dropdown menu to select a location - all selections will open up to the same survey
#         selection = st.selectbox('Select your location here', options = places, key = 'nyc')
#
#     # Ohio page response
#         if selection == 'Columbus, OH':
#             st.info('Ohio? Are you sure?')
#             if st.button("I'm sure.") == True:
#                 empty()
#                 with next_page.container():
#                     st.write('Bummer!')
#             # user_preferences()
#
#     # All other selections response
#         elif selection == 'New York City, NY':
#             empty()
#             with next_page.container():
#                 new_york_city.app()


def app():

    # next_page = st.empty()
    #
    # def empty():
    #     next_page.empty()
    #     sleep(0.5)

# place = 'New York City, NY'
    st.button('Click here to select a new location')
        # empty()
        # with next_page.container():
        #     empty()
        #     main_test.main_app()

    st.title('You selected: New York City, NY')
    image = Image.open('/Users/cynthiarodriguez/Desktop/DSI-822/Capstone/notebooks/stlib/nyc.jpg')
    st.image(image)

    st.header("Let's answer a few questions.")

# Button to return to home page
# with st.sidebar:
#     st.button('Click here to select a new location.')

# Weather preferences
    st.subheader('1.  What is your ideal temperature range?')
    weather = st.slider('Weather preference', min_value = None, max_value = 120, value=(0, 25), label_visibility = 'collapsed')
# st.write(weather[0], weather[1])
# st.write('Range: ', weather)

# Walkability
    importance_range = ('Not important at all', 'Not very important', 'Neutral', 'A little important', 'Extremely important')
    st.subheader('2.  How important is walkability?')
    walkability = st.select_slider('Walkability', options = importance_range, value = 'Neutral', label_visibility = 'collapsed')

# Monthly budget
    st.subheader('10.  How much are you willing to spend on accomodations each month?')
    budget_range = st.number_input('Monthly budget range', min_value = 0, step = 1, label_visibility = 'collapsed')
# st.write('Budget: ', budget_range)
