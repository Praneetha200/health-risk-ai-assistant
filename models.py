from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)

    dob = db.Column(db.String(20), nullable=False)

    email = db.Column(db.String(120), nullable=False)

    glucose = db.Column(db.Float, nullable=False)

    haemoglobin = db.Column(db.Float, nullable=False)

    cholesterol = db.Column(db.Float, nullable=False)

    risk_level = db.Column(db.String(50))

    health_score = db.Column(db.Integer)

    remarks = db.Column(db.Text)