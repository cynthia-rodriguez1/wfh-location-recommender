import numpy as np
import pandas as pd
import streamlit as st
from keras.utils import load_img, img_to_array
from time import sleep
import new_york_city
    # from stlib import new_york_city

def empty():
    next_page.empty()
    sleep(0.5)

next_page = st.empty()

def main_app():

# This is the main page that users will land on
    with next_page.container():
        st.title('Where do you want to go?')

        places = ('Asheville, NC', 'Austin, TX', 'Boston, MA', 'Cambridge, MA',
'Chicago, IL', 'Columbus, OH', 'Dallas, TX', 'Denver, CO',
'Fort Lauderdale, FL', 'Fort Worth, TX', 'Hawaii, HI', 'Jersey City, NJ', 'Las Vegas, NV', 'Los Angeles, CA',
'Nashville, TN', 'New Orleans, LA', 'Newark, NJ', 'New York City, NY', 'Oakland, CA', 'Portland, OR',
'Rhode Island, RI', 'Salem, OR', 'San Diego, CA', 'San Francisco, CA', 'San Mateo, CA', 'Santa Clara, CA',
'Santa Cruz, CA', 'Seattle, WA', 'Twin Cities, MN', 'Washington DC')

# Dropdown menu to select a location - all selections will open up to the same survey
        selection = st.selectbox('Select your location here', options = places, key = 'main_page1')

# Ohio page response
        if selection == 'Columbus, OH':
            st.info('Ohio? Are you sure?')
            if st.button("I'm sure.") == True:
                empty()
                with next_page.container():
                    st.write('Bummer!')
        # user_preferences()

# All other selections response
        elif selection == 'New York City, NY':
            empty()
            with next_page.container():
                new_york_city.app()

main_app()

# st.write('You selected: ', selection)

# if __name__ == "__main__":
#     run()
