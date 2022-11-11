import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity


feature_cols = df.columns[1:]
sc = MinMaxScaler()
scaled_df = sc.fit_transform(df[feature_cols])

# Setting model and indices for reference
indices = pd.Series(df.index, index=df['place'])
cs_df = cosine_similarity(scaled_df)

def find_rec(input_row, model):
    input_row = 'User Input'

    model = cs_df

    '''Indexing the user input row'''
    index = indices[input_row]

    '''Filtering and sorting the cosine similarity values for input data'''
    sim_scores = list(enumerate(model[index]))
    sim_scores_sorted = sorted(sim_scores, key = lambda x:x[1], reverse=True)

    '''Finding and returning the location most similar to user's preferences'''
    best_fit_score = sim_scores_sorted[1]
    best_fit_index = best_fit_score[0]
    recommended_place = df['place'].iloc[best_fit_index]

    return recommended_place
