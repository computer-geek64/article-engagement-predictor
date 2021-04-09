#!/usr/bin/python3
# sentiment_col.py

from transformers import pipeline
import pandas as pd


def generate_sentiment_col(articles_path='../../processed_data/complete-nyt-articles-2020.csv', comments_path='../../processed_data/complete-nyt-comments-2020.csv'):
    articles = pd.read_csv(articles_path)
    comments = pd.read_csv(comments_path)
    nlp = pipeline('sentiment_analysis')

    for row in comments.index:
        result = nlp(comments.at[row, 'commentBody'])
        sentiment = abs(result['score'])
        comments.at[row, 'sentiment'] = sentiment
    for article_row in articles.index:
        article_id = articles.at[article_row, 'uniqueID']
        sentiments_for_article = []
        for comment_row in comments.index:
            if comments.at[comment_row, 'articleID'] == article_id:
                sentiments_for_article.append(comments.at[comment_row, 'sentiment'])
        articles.at[article_row, 'comment_sentiment'] = sum(sentiments_for_article) / len(sentiments_for_article)

    articles.to_csv(articles_path)
    comments.to_csv(comments_path)

