# Function to convert user input to correct format

import pandas as pd
import numpy as np


def wfh(user_input_data, dataframe):
    '''Inserting placeholder for location name'''
    user_input_data.insert(0, 'User Input')

    '''Converting user list to dictionary'''
    feat_keys = ['place', 'low_temp', 'high_temp', 'food_pref', 'walk_pref', 'pol_dem_pref', 'misc_costs', 'monthly_budget']
    user_input_dict = dict(zip(feat_keys, user_input_data))

    '''Creating indices for ordinal input values'''

    # Food preferences
    chain_mean = dataframe['chain_ratio'].mean()
    chain_std = dataframe['chain_ratio'].std()

    chain_input_options = ['I only eat at Mom-n-Pop restaurants', 'I prefer non-chain restaurants', 'I like a combination of both', 'I would rather go somewhere that has a drive-thru', 'The faster the food the better']
    chain_input_index = [chain_mean - (2*chain_std), chain_mean - (1*chain_std), chain_mean, chain_mean + (1*chain_std), chain_mean + (2*chain_std)]
    chain_mapper = dict(zip(chain_input_options, chain_input_index))

    # Walkability
    walk_mean = dataframe['walkability_idx'].mean()
    walk_std = dataframe['walkability_idx'].std()

    walk_input_options = ['Not important at all', 'Not very important', 'Neutral', 'A little important', 'Extremely important']
    walk_input_index = [walk_mean - (2*walk_std), walk_mean - (1*walk_std), walk_mean, walk_mean + (1*walk_std), walk_mean + (2*walk_std)]
    walkability_mapper = dict(zip(walk_input_options, walk_input_index))

    # Political lean preferences
    # Using the mean here instead of 50/50 because most locations have a slight to moderate left lean, meaning that if we set the default value to 0.5, we'd be unintentionally biasing the results
    pol_mean = dataframe['political_left_lean'].mean()
    pol_std = dataframe['political_left_lean'].std()

    pol_pref_options = ['Strong left lean preferred', 'Moderate left lean preferred', 'Moderate right lean preferred', 'Strong right lean preferred']
    pol_pref_index = [pol_mean + (2*pol_std), pol_mean + (1*pol_std), pol_mean - (1*pol_std), pol_mean - (2*pol_std)]
    pol_pref_mapper = dict(zip(pol_pref_options, pol_pref_index))

    '''Mapping food preference to numerical value'''
    for k, v in chain_mapper.items():
        if user_input_dict['food_pref'] == k:
            user_input_dict['food_pref'] = v

    '''Mapping walkability preference to numerical value'''
    for k, v in walkability_mapper.items():
        if user_input_dict['walk_pref'] == k:
            user_input_dict['walk_pref'] = v

    '''Mapping political preference to numerical value'''
    for k, v in pol_pref_mapper.items():
        if user_input_dict['pol_dem_pref'] == k:
            user_input_dict['pol_dem_pref'] = v
        else:
            user_input_dict['pol_dem_pref'] = pol_mean

    pol_rep_pref = 1 - user_input_dict['pol_dem_pref']

    '''Estimating miscellaneous cost index based on user input'''
    misc_mean = dataframe['miscellaneous_cost_idx'].mean()
    misc_std = dataframe['miscellaneous_cost_idx'].std()

    user_input_dict['misc_costs'] = misc_mean + (user_input_dict['misc_costs'] * misc_std/5)

    '''Converting dictionary values to list'''
    user_input_list = list(user_input_dict.values())

    '''Adding a Repulican-lean political value'''
    user_input_list.insert(6, pol_rep_pref)

    '''Adding the updated list as a new row in our dataframe'''
    dataframe.loc[len(dataframe)] = user_input_list

    # return user_input_list
    return user_input_list
