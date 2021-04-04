#!/usr/bin/python3
# text2.py

import pandas as pd

data = pd.read_csv('../../data/nyt-articles-2020.csv')
l1 = len(data)
print(l1)

for feature in data:
    data = data[data[feature].notnull()]

print(len(data))