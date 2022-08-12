import pickle
import os

#spam classifier suppor vector machine model 94% accuracy
class Spam_Classification():
    
    def __init__(self):      
                
        with open(os.path.abspath('ml_models/text_classification/spam_classification_svm.pkl'),'rb') as f:
            self.svm = pickle.load(f)

        #with open('/home/python/Desktop/career/ml_models_API/python_restful/ml_models/text_classification/spam_classification_svm.pkl','rb') as f:
        #    self.svm = pickle.load(f)        

    def message_clasiffication(self,data):
        # Obtain the classification for your message
        classification = self.svm.predict(data)
        #classification = {"classification":str(classification[0])}
        return classification[0]

    
