from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.
# class Example(db.Model):
#     __tablename__ = 'examples'

#     id = db.Column(db.Integer, primary_key=True)
#     columnname = db.Column(db.String)

class Hotel(db.Model, SerializerMixin):
    __tablename__ = 'hotels'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key = True)
    rating = db.Column(db.Integer)
    text = db.Column(db.String)

    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'))
