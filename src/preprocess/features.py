#!/usr/bin/python3
# features.py

import pandas as pd
from stop_words import get_stop_words


# main function
def delete_incomplete_columns(file, to_be_deleted=[], not_to_be_deleted=[], special=False):
    data = pd.read_csv('../../data/' + file)

    for tbd in to_be_deleted:
        del data[tbd]

    if len(not_to_be_deleted) > 0:
        data = data.filter(not_to_be_deleted)

    for feature in data:
        data = data[data[feature].notnull()]

    if special:
        unwanted = ['Interactive Feature', 'Obituary (Obit)', 'briefing', 'Letter']
        data = data[data['material'].isin(unwanted)]

    data.to_csv('../../processed_data/complete-' + file)


if __name__ == '__main__':
    # calling the function on articles
    tbd = ['newsdesk', 'keywords', 'pub_date']  # param2 columns we want to delete
    delete_incomplete_columns('nyt-articles-2020.csv', to_be_deleted=tbd, special=True)

    # calling the function on articles
    tb = ['commentBody', 'articleID']  # param2 columns we want to delete
    delete_incomplete_columns('nyt-comments-2020.csv', not_to_be_deleted=tb)
