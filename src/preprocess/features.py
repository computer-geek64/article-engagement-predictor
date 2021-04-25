#!/usr/bin/python3
# features.py

import os
import pandas as pd


def delete_incomplete_columns(file, to_be_deleted=[], not_to_be_deleted=[], special=False):
    data = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data', file))

    for tbd in to_be_deleted:
        del data[tbd]

    if len(not_to_be_deleted) > 0:
        data = data.filter(not_to_be_deleted)

    for feature in data:
        data = data[data[feature].notnull()]

    if special:
        unwanted = ['Interactive Feature', 'Obituary (Obit)', 'briefing', 'Letter']
        data = data[data['material'].isin(unwanted)]

    data.to_csv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data', os.path.splitext(file)[0] + '-dropped.csv'), index=False)


# main function
def drop_features():
    # calling the function on articles
    tbd = ['newsdesk', 'keywords', 'pub_date']  # param2 columns we want to delete
    delete_incomplete_columns('nyt-articles-2020.csv', to_be_deleted=tbd, special=True)

    # calling the function on comments
    tbd = ['commentBody', 'articleID']  # param2 columns we want to delete
    delete_incomplete_columns('nyt-comments-2020-sample.csv', not_to_be_deleted=tbd)
