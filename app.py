import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

#from security import identity,authenticate

from resources.sentiment_analysis import Sentiment
from resources.spam_classification import Spam_detection

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'chris'
CORS(app)


api = Api(app)


api.add_resource(Sentiment,'/sentiment')
api.add_resource(Spam_detection,'/spam_detection')

if __name__ == '__main__':

    app.run(port=5000,debug=True)
