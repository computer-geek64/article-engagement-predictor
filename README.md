# Introduction:

The New York Times is an American newspaper that is widely regarded as one of the popular and well-established news sources in the world. Over the past few years, user engagement has steadily grown leading to stronger online opinions and the need to classify and measure the sort of engagement on articles is at an all-time high. By predicting the public response, the newspaper can give more targeted articles which will draw in more readers and keep the public well informed and engaged about critical current events in the world. To do so, we will use an open-source dataset of 16,000 New York Times articles and 5 million corresponding comments, with over 30 features to examine. 

# Problem Definition:

Given various features of a New York Times article as inputs, the goal of our project is to generate an overall **engagement metric**. This engagement metric can provide editors with necessary insight and feedback on their writing to gauge the audience reaction before they publicly publish their article.

* Article Features: headline, article newsdesk, article section, article length, keywords, abstract
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

Tsagkias, M., Weerkamp, W., & De Rijke, M. (2009, November). Predicting the volume of comments on online news stories. In Proceedings of the 18th ACM conference on Information and knowledge management (pp. 1765-1768).

Schumaker, R. P., Zhang, Y., Huang, C. N., & Chen, H. (2012). Evaluating sentiment in financial news articles. Decision Support Systems, 53(3), 458-464.

Althaus, S. L., & Tewksbury, D. (2002). Agenda Setting and the “New” News: Patterns of Issue Importance Among Readers of the Paper and Online Versions of the New York Times. Communication Research, 29(2), 180–207. https://doi.org/10.1177/0093650202029002004
