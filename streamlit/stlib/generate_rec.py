import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity


def find_rec(df, input_row = 'User Input'): # Defining the input row here because we will always be evaluating/recommending for the 'User Input' row

    '''Scaling all numeric columns'''
    feature_cols = df.columns[1:]
    minmax = MinMaxScaler()
    scaled_df = minmax.fit_transform(df[feature_cols])

    '''Setting all place indices for reference'''
    indices = pd.Series(df.index, index=df['place'])
    user_index = indices[input_row]

    '''Finding the cosine similarities between all location vectors'''
    cosine_sim = cosine_similarity(scaled_df)

    '''Filtering and sorting the cosine similarity values for input data'''
    sim_scores = list(enumerate(cosine_sim[user_index]))
    sim_scores_sorted = sorted(sim_scores, key = lambda x:x[1], reverse=True)

    '''Finding and returning the location most similar to user's preferences'''
    best_fit_score = sim_scores_sorted[1]
    best_fit_index = best_fit_score[0]
    recommended_place = df['place'].iloc[best_fit_index]

    return recommended_place
