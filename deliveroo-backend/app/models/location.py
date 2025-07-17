from . import db

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    current_location = db.Column(db.String, nullable=True)

    parcels = db.relationship("Parcel", back_populates="location")
