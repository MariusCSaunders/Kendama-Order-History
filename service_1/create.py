#Marius Saunders
#QA Project 2
#Kendama Order History

#Imports all the needed modules
from application import db
from application.models import Orders

#Destroys previous database and creates a new one
db.drop_all()
db.create_all()

order = Orders(dama="Krom Gas", accessory="String Pack", price=48.49)

#Adds first entry to Orders table
db.session.add(order)

#Commits the changes
db.session.commit()