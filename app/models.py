from . import db
from . import ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    cellphone = db.Column(db.String(11), nullable=False)
    feet = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    brand = db.Column(db.String(20), nullable=False)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'cellphone','feet','color', 'country', 'city', 'gender','brand')

user_schema = UserSchema(many=False)
users_schema = UserSchema(many=True)