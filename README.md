# Introduction:

The New York Times is an American newspaper that is widely regarded as one of the popular and well-established news sources in the world. Over the past few years, user engagement has steadily grown leading to stronger online opinions as well as the need to classify and measure the sort of engagement on articles. By predicting the public response, the newspaper can give more targeted articles which will draw in more readers and keep the public well informed and engaged about critical current events in the world. To do so, we will use an open-source dataset of 16,000 New York Times articles and 5 million corresponding comments, with over 30 features to examine. 

# Problem Definition:

Given various features of a New York Times article as inputs, the goal of our project is to generate an overall **engagement metric**. This engagement metric can provide editors with necessary insight and feedback on their writing to gauge the audience reaction before they publicly publish their article.

* Article Features: headline, article newsdesk, article section, article length, keywords, abstract, etc
* Output of the first model: Number of comments for the article 
* Output of the second model: Forecasted average sentiment magnitude
* Final output: Engagement metric (calculated through a weighted sum of the number of comments and the magnitude of the sentiment that the article is forecasted to receive)

# Data
Two CSV files from Kaggle, articles.csv and comments.csv. These are linked through unique IDs which correspond to the info about articles and the individual comments corresponding to each comment. 
* Article columns - newsdesk, section, subsection, material, headline, abstract, keyword, word count, publish date, number comments, link ID
* Comment columns - comment ID, status, user ID, flagged, trusted, comment body, link ID

# Project Flow / Methods
## Preprocessing

:heavy_check_mark:**Data Cleaning:**
* Removing incomplete features that don’t have data points for every column
* Trim whitespace on raw text
* Expand contractions and similar constructs 
* Lowercase all text, remove non-English characters 
* Convert English number words to actual numbers 
* Remove stopwords and words of length <= 2

:heavy_check_mark:**Feature Engineering:**
Drop appropriate columns from each CSV with justification
* Article Columns Drop Justification
  * Newsdesk = Section column is a greater encompassing feature for the article’s area
  * Material = Drop every row of Material that has one of these: ['Interactive Feature', 'Obituary (Obit)', 'briefing', 'Letter'] as these are not news articles intended for engagement prediction
  * Keywords = The abstract is better suited for an NLP model to extract useful information rather than uncontextualized keywords
  * Publication Date = If we are looking to gain insight on an article about to be published, the date of past articles will not help us because we cannot use the date to understand why an article had a certain sentiment since we don’t know what events occurred around that date.
* Comment Columns Drop Justification
  * Drop everything except comment body and link ID. We only need to have the comment content as well as the corresponding article to generate a sentiment value based on the comment text. The link ID will not be used in actually building the model, but only for linking an article with its corresponding comments.
  
Initial tests of our project will use all the features listed above, since feature selection will be performed after the later parts of the project have been completed (building the models to predict the number of words and the sentiment). We plan to use the [Extra Trees Regressor's](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html) ability to fit an estimator and provide feature importances in order to select which features may be more or less relevant in our final model.    
  
:heavy_check_mark:**Generation of Sentiment Column:**
Run a sentiment analysis model that will generate the sentiment column in the articles dataset based on each comment body (in comments dataset). Use transformers sentiment model for each comment row with the comment text as input features. Add new column “average sentiment” in article csv which averages all the sentiment columns for comments which have the corresponding article ID. These sentiment values were previously calculated in the sentiment analysis model. 

:heavy_check_mark:**Datasets after preprocessing and adding the sentiment column:**
More than 90% of the dataset was found to still be usable for the predictions of the number of words and the sentiment. All of the preprocessing steps are robust in that they help standardize the dataset by removing or modifying anomalies (converting all numbers to digit form, removing non-English characters, removing less relevant words). By dropping features that are not directly relevant to the problem and sanitizing the dataset, we can ensure our model can make more useful predictions. A short example of our preprocessing capability is the input sentence:

> "Thirty white horses, on a red hill. First they champ, then they stamp, then they stand still."

After preprocessing, it becomes:

> "30 white horses red hill first champ stamp stand still"

which is more semantically useful for our model.



## Prediction of Number of Words and Sentiment ##
**Number of Comments Model:**
After midterm report - use numerical features and text features together (columns which were not dropped) as features to predict # of comments for a given new article. 

**Sentiment Prediction Model:**
After midterm report - use numerical features and text features (including number of comments and not dropped columns) as features together to predict “average sentiment” for a new article. 

**Engagement Metric Calculation:**
For a given new article, run number of comments model first and use the predicted comment value as one of the input features into the sentiment prediction model to get predicted sentiment value. The engagement metric will then be calculated based on number of comments and predicted sentiment value.


# Discussion:

By analyzing and predicting the number of comments anticipated for an article, the publishers can determine the level of public interest in a given topic and can choose to follow up with corresponding related articles. Additionally, the sentiment analysis allows  the editors to determine how polarizing an article is, and potentially provide items such as blog posts to provide a forum for further public discussion. Low sentiment can tell the editor that perhaps the article should be revised to make it more engaging.

# Dataset:

[https://www.kaggle.com/benjaminawd/new-york-times-articles-comments-2020](https://www.kaggle.com/benjaminawd/new-york-times-articles-comments-2020)

# References:

Tsagkias, M., Weerkamp, W., & De Rijke, M. (2009, November). Predicting the volume of comments on online news stories. In Proceedings of the 18th ACM conference on Information and knowledge management (pp. 1765-1768).

Schumaker, R. P., Zhang, Y., Huang, C. N., & Chen, H. (2012). Evaluating sentiment in financial news articles. Decision Support Systems, 53(3), 458-464.

Althaus, S. L., & Tewksbury, D. (2002). Agenda Setting and the “New” News: Patterns of Issue Importance Among Readers of the Paper and Online Versions of the New York Times. Communication Research, 29(2), 180–207. https://doi.org/10.1177/0093650202029002004
