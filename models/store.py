from db import db

class StoreModel(db.Model):

    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy = 'dynamic')

    def __init__(self, name):
        self.name = name

    #return a json representation of the model (a dictionary)
    def json(self):
        return{'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #SELECT * FROM items where name=name LIMIT 1

    def save_to_db(self):#this can insert and also update the Resource
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        