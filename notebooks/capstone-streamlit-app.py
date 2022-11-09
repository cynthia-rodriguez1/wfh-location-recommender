# Defining user survey function
def user_preferences():
    import numpy as np
    import pandas as pd
    import streamlit as st
    from keras.utils import load_img, img_to_array

    st.markdown('You selected: New York City, NY')
    st.subheader("Let's answer a few questions")
    # Weather preferences
    weather = st.slider('What is your ideal temperature range?', min_value = None, max_value = 120,
    value=(0, 25))
    # Monthly budget
    st.number_input('How much are you willing to spend on accomodations each month?')

def run():

    import numpy as np
    import pandas as pd
    import streamlit as st
    from keras.utils import load_img, img_to_array
    # from stlib import new_york_city

# This is the main page that users will land on
    st.title('Where do you want to go?')

    places = ('Asheville, NC', 'Austin, TX', 'Boston, MA', 'Cambridge, MA',
'Chicago, IL', 'Columbus, OH', 'Dallas, TX', 'Denver, CO',
'Fort Lauderdale, FL', 'Fort Worth, TX', 'Hawaii, HI', 'Jersey City, NJ', 'Las Vegas, NV', 'Los Angeles, CA',
'Nashville, TN', 'New Orleans, LA', 'Newark, NJ', 'New York City, NY', 'Oakland, CA', 'Portland, OR',
'Rhode Island, RI', 'Salem, OR', 'San Diego, CA', 'San Francisco, CA', 'San Mateo, CA', 'Santa Clara, CA',
'Santa Cruz, CA', 'Seattle, WA', 'Twin Cities, MN', 'Washington DC')

# Dropdown menu to select a location - all selections will open up to the same survey
    selection = st.selectbox('Select your location here', options = places)

# Ohio page response
    if selection == 'Columbus, OH':
        st.info('Ohio? Are you sure?')
        if st.button("I'm sure.") == True:
            user_preferences()

# All other selections response
    elif selection == True:
        user_preferences()

# st.write('You selected: ', selection)

if __name__ == "__main__":
    run()
