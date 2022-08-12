from flask_restful import Resource,reqparse
from ml_models.text_classification.spam_classification import Spam_Classification

class Spam_detection(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sentence',
            type=str,
            required=True,
            help='This field cannot be left blank.'
        )     
    
    def get(self):
        
        data = Spam_detection.parser.parse_args()
        data = [data.sentence]
        classification = Spam_Classification()
        print(classification.message_clasiffication(data))
        return {'class':classification.message_clasiffication(data)},200

    