#!/usr/bin/python3
# text2.py

import pandas as pd



#main function
def delete_incomplete_columns(file, to_be_deleted):
    data = pd.read_csv('../../data/'+file)
    for tbd in to_be_deleted:
        del data[tbd]

    for feature in data:
        data = data[data[feature].notnull()]

    data.to_csv('../../processed_data/complete-nyt-articles-2020.csv')

#calling the function on articles
file = 'nyt-articles-2020.csv' #param1 i.e. which file we want to clean
to_be_deleted = ['newsdesk', 'material', 'keywords', 'pub_date', 'uniqueID'] #param2 columns we want to delete
delete_incomplete_columns(file, to_be_deleted)