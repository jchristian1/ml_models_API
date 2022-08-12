from flask_restful import Resource,reqparse
from ml_models.semantic_sentiment.nltk_sentiment import Nltk_sentiment_analyzer

class Sentiment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sentence',
            type=str,
            required=True,
            help='This field cannot be left blank.'
        )        
    parser.add_argument('label',
            type=str,
            required=True,
            help='We need a label to see how the model perform.'
        )        
    
    def get(self):
        
        data = Sentiment.parser.parse_args()        
        
        sentiment = Nltk_sentiment_analyzer(data)
        
        print(sentiment.review_rating())
        
        return {'score':sentiment.review_rating()},200

    