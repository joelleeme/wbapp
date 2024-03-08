from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RealEstate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'address': self.address,
            'price': self.price
        }

class CrimeRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(120), nullable=False)
    crime_rate = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'location': self.location,
            'crime_rate': self.crime_rate
        }