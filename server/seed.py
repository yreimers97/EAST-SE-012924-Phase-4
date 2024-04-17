#!/usr/bin/env python3

from app import app
from models import db, Hotel

with app.app_context():
    Hotel.query.delete()
    hotel_1 = Hotel(name = 'MargaritaVille')
    hotel_2 = Hotel(name = 'Sandals Resort')
    hotel_3 = Hotel(name = 'Majestic Resort')
    db.session.add_all([hotel_1, hotel_2, hotel_3])
    db.session.commit()
    print("🌱 Hotels successfully seeded! 🌱")