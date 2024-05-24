import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_song_sentiment(lyrics):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(lyrics)
    
    return sentiment_scores

if __name__ == "__main__":
    print(analyze_song_sentiment("Happy birthday! I hope you have a great day!"))