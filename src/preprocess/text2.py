#!/usr/bin/python3
# text2.py

import pandas as pd
from stop_words import get_stop_words

#main function
def delete_incomplete_columns(file, to_be_deleted=[], not_to_be_deleted=[]):
    data = pd.read_csv('../../data/' + file)
    features = data.keys()

    for tbd in to_be_deleted:
        del data[tbd]
    
    for feature in features:
        data = data[data[feature].notnull()]

    data.to_csv('../../processed_data/complete-nyt-articles-2020.csv')

#calling the function on articles
tbd = ['newsdesk', 'keywords', 'pub_date'] #param2 columns we want to delete
delete_incomplete_columns('nyt-articles-2020.csv', to_be_deleted=tbd)

#calling the function on articles
# tbd = ['newsdesk', 'material', 'keywords', 'pub_date'] #param2 columns we want to delete
# delete_incomplete_columns('nyt-articles-2020.csv', to_be_deleted=tbd)


#stopwords
def is_stop_word(word):
    stop_word = get_stop_words('en')
    return word in stop_word