#Marius Saunders
#QA Project 2
#Kendama Order History

from . import db

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dama = db.Column(db.String(30), nullable=False)
    accessory = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float)

    