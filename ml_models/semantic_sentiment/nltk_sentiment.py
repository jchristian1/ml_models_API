# Import SentimentIntensityAnalyzer and create an sid object
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

class Nltk_sentiment_analyzer():
    
    def __init__(self,data):
        self.sid = SentimentIntensityAnalyzer()

        # Write a review as one continuous string (multiple sentences are ok)
        self.data = data
        self.label = data['label']
        self.sentence = data['sentence']

        # Obtain the sid scores for your review
        self.score = self.sid.polarity_scores(self.sentence)


    def review_rating(self):
        scores = self.score
        if scores['compound'] == 0:
            return 'Neutral'
        elif scores['compound'] > 0:
            return 'Positive'
        else:
            return 'Negative'