# Introduction:

The New York Times is an American newspaper that is widely regarded as one of the popular and well-established news sources in the world with over 130 Pulitzer prizes. Ranked 3rd in the US, it continues to publish about 150 articles per day, which users can read and comment on with their own views. Over the past few years, user engagement has steadily grown leading to stronger online opinions and the need to classify and measure the sort of engagement on articles is at an all-time high. As a rapidly evolving newspaper source, it is key for the New York Times to identify the most popular articles and attempt to predict readers’ critical responses. By predicting the public response, the newspaper can give more targeted articles which will draw in more readers and keep the public well informed and engaged about critical current events in the world. With deep polarization being a key issue in the United States, we decided to do our part and measure the quality of engagement, and the bias present within these comments.

# Problem Definition:

Given the comments of a New York Times article as inputs, with the size of the comments, sentiment, and a number of comments as features for each article, it is possible to generate an overall engagement metric, which can provide editors with necessary insight and feedback on their writing.

* Article Features: headline, article newsdesk, article section, article length, keywords, abstract
* Comment Features: comment/comment thread body, depth, comment length, create date == update date
* Output of the model: Number of comments
* Output of the sentiment analysis: Magnitude of the sentiment
* Final output: Engagement metric (calculated by the number of comments, the magnitude of the sentiment, and the weighted sum of the magnitude of the sentiment of comment replies)


# Methods:
**Pre-processing:** 
Eliminate rows that lack data for each feature (this is invalid data and should be discarded)
Use a sentiment analysis natural language processing model to create an additional column on the comments dataset for the sentiment magnitude 

**Machine learning models used:**
Two NLP models will be used (one model for prediction of the number of comments, one model for the average sentiment magnitude of the comments)
Sentiment magnitude prediction uses the column we created in the preprocessing step
The number of comments and average sentiment magnitude are directly correlated to levels of user engagement

**Post-processing:**
The number of comments and average sentiment magnitude can be combined into a final engagement metric through a mathematical formula



# Potential Results:

* Number of comments that a potential published article could receive as well as the general sentiment towards that topic
  * These values could be combined to create an overall engagement metric that determines the strength of interactions that an article could generate
* Classified groupings into different classes of articles based on topics
  * Within each group, average number of comments
* The model with the ability to predict the number of comments if an article with the input features is selected

# Discussion:

By analyzing and predicting the number of comments anticipated for a given article, the publishers can determine the level of public interest in a given topic and can choose to follow up with corresponding related articles. In addition, the sentiment analysis will allow the editors to determine how polarizing an article is, and potentially provide items such as blog posts to provide a forum for further public discussion. Note that all of this analysis hinges on the dataset’s given inputs which allow us to classify into article categories, and then breakdown the respective comments.

# Dataset:

[https://www.kaggle.com/benjaminawd/new-york-times-articles-comments-2020](https://www.kaggle.com/benjaminawd/new-york-times-articles-comments-2020)

# References:

Article from people who also performed sentiment analysis on NYT news articles, but for Financial Signal Prediction:
[https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.5693&rep=rep1&type=pdf](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.5693&rep=rep1&type=pdf)

Schumaker, R. P., Zhang, Y., Huang, C. N., & Chen, H. (2012). Evaluating sentiment in financial news articles. Decision Support Systems, 53(3), 458-464.

Predicting the volume of comments on online news stories:
[https://dl.acm.org/doi/abs/10.1145/1645953.1646225?casa_token=6uYvAaNOCnwAAAAA%3AzNjh1At3MQRrbf5q28ZTgFcfvZsmlrOy831jKJqZVZcGZCJS3nPd3A1mzLHeRQ-F0BUVR1HonWcfLg](https://dl.acm.org/doi/abs/10.1145/1645953.1646225?casa_token=6uYvAaNOCnwAAAAA%3AzNjh1At3MQRrbf5q28ZTgFcfvZsmlrOy831jKJqZVZcGZCJS3nPd3A1mzLHeRQ-F0BUVR1HonWcfLg)

