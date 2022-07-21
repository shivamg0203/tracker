from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer(), primary_key = True)
  username = db.Column(db.String(),unique = True, nullable = False)
  email = db.Column(db.String())
  course = db.Column(db.String())
  institute = db.Column(db.String())
  about = db.Column(db.String())