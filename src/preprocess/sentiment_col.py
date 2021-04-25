#!/usr/bin/python3
# sentiment_col.py

import os
import pandas as pd
from transformers import pipeline


def generate_sentiment_col(articles_path=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data', 'nyt-articles-2020-dropped-cleaned.csv'), comments_path=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data', 'nyt-comments-2020-sample-dropped-cleaned.csv')):
    articles = pd.read_csv(articles_path)
    comments = pd.read_csv(comments_path)
    nlp = pipeline('sentiment-analysis')

    for row in comments.index:
        result = nlp(comments.at[row, 'commentBody'])[0]
        sentiment = abs(result['score'])
        comments.at[row, 'sentiment'] = sentiment
    for article_row in articles.index:
        article_id = articles.at[article_row, 'uniqueID']
        sentiments_for_article = []
        for comment_row in comments.index:
            if comments.at[comment_row, 'articleID'] == article_id:
                sentiments_for_article.append(comments.at[comment_row, 'sentiment'])
        articles.at[article_row, 'comment_sentiment'] = sum(sentiments_for_article) / len(sentiments_for_article)

    articles.to_csv(articles_path, index=False)
    comments.to_csv(comments_path, index=False)
