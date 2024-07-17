import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

# Load data
WW_trends = json.loads(open('datasets/WWTrends.json').read())
US_trends = json.loads(open('datasets/USTrends.json').read())
tweets = json.loads(open('datasets/WeLoveTheEarth.json').read())

# Extracting and analyzing trends
world_trends = set([trend['name'] for trend in WW_trends[0]['trends']])
us_trends = set([trend['name'] for trend in US_trends[0]['trends']])
common_trends = world_trends.intersection(us_trends)

# Extracting tweet texts
texts = [tweet['text'] for tweet in tweets]

# Performing sentiment analysis
sentiments = [TextBlob(text).sentiment.polarity for text in texts]

# Inspecting the first 10 sentiment scores
print(json.dumps(sentiments[0:10], indent=1), "\n")

# Plotting the distribution of sentiment scores
plt.figure(figsize=(10, 5))
plt.hist(sentiments, bins=20, color='blue', edgecolor='black')
plt.title('Sentiment Polarity Distribution')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.show()

# Extracting screen names and hashtags
names = [user_mention['screen_name'] for tweet in tweets for user_mention in tweet['entities']['user_mentions']]
hashtags = [hashtag['text'] for tweet in tweets for hashtag in tweet['entities']['hashtags']]

# Counting occurrences of names and hashtags
for item in [names, hashtags]:
    c = Counter(item)
    print(c.most_common(10), "\n")

# Extracting retweets data
retweets = [(tweet['retweet_count'], tweet['retweeted_status']['favorite_count'], tweet['retweeted_status']['user']['followers_count'], tweet['retweeted_status']['user']['screen_name'], tweet['text']) for tweet in tweets if 'retweeted_status' in tweet]

# Create a DataFrame and visualize the data
df = pd.DataFrame(retweets, columns=['Retweets', 'Favorites', 'Followers', 'ScreenName', 'Text']).groupby(['ScreenName', 'Text', 'Followers']).sum().sort_values(by=['Followers'], ascending=False)
df.style.background_gradient()

# Plotting the distribution of languages
tweets_languages = [tweet['lang'] for tweet in tweets]
plt.figure(figsize=(10, 5))
plt.hist(tweets_languages, bins=len(set(tweets_languages)), color='blue', edgecolor='black')
plt.title('Language Distribution of Tweets')
plt.xlabel('Language')
plt.ylabel('Frequency')
plt.show()