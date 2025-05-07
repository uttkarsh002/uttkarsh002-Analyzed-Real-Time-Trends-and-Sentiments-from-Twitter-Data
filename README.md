# 🌍 Twitter Trend & Sentiment Analysis – #WeLoveTheEarth

This project focuses on analyzing Twitter trends globally and in the US, and performs detailed sentiment analysis on tweets related to the hashtag **#WeLoveTheEarth**. The aim is to understand which topics are trending, the sentiment behind public opinion, and the influential contributors in the conversation.

---

## 📌 Features

- 🔍 Extract and compare **Worldwide vs US Twitter Trends**
- 💬 Analyze sentiment of tweets using **TextBlob**
- 📊 Visualize:
  - Sentiment polarity distribution
  - Language distribution of tweets
- 📈 Identify most mentioned users and hashtags
- 🧑‍🤝‍🧑 Discover most influential users based on retweets and followers

---

## 📁 Dataset

### Input Files (in JSON format)
- `WWTrends.json` — Twitter trending topics worldwide
- `USTrends.json` — Twitter trending topics in the US
- `WeLoveTheEarth.json` — Sample of tweets related to #WeLoveTheEarth

---

## 🛠️ Technologies Used

| Purpose                | Library           |
|------------------------|-------------------|
| Data handling          | `pandas`, `json`  |
| Sentiment analysis     | `textblob`        |
| Visualization          | `matplotlib`      |
| Counting frequency     | `collections.Counter` |

---

## 📈 Visual Output

- **Sentiment Polarity Histogram**:
  Shows the distribution of tweet sentiments from negative to positive.

- **Most Mentioned Users & Hashtags**:
  Lists the top 10 most frequent user mentions and hashtags in the tweets.

- **Retweet Impact Table**:
  Highlights the tweets with the most followers and engagement.

- **Language Histogram**:
  Displays which languages are most used in the tweets.

---

## 🧪 How It Works (High-Level Workflow)

1. **Load JSON Files** containing trend and tweet data.
2. Extract trend names and compare common trends between worldwide and US.
3. Use `TextBlob` to calculate sentiment polarity for each tweet text.
4. Use `Counter` to analyze hashtag and user mention frequency.
5. Create a structured `DataFrame` of retweets showing reach and popularity.
6. Plot histograms for **sentiment** and **language distribution**.

---

## 💡 Example Insights

- Identify how positively or negatively people react to environmental campaigns.
- Spot top influencers promoting the campaign.
- Understand language diversity and reach of the topic.

---

## 🏁 Getting Started

### 📦 Prerequisites

Install the required libraries:
```bash
pip install textblob matplotlib pandas
