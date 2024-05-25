from app import db

class Bag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    items = db.relationship('Item', backref='bag', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    packed = db.Column(db.Boolean, default=False)
    bag_id = db.Column(db.Integer, db.ForeignKey('bag.id'), nullable=False)
