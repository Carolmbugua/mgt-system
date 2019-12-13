from app import db

class Inventories(db.Model):
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(100, nullable=False))
    type = db.column(db.string(100, nullable=False))
    BP = db.column(db.integer(100, nullable=False))
    SP = db.column(db.integer(100, nullable=False))
    stock = db.column(db.integer(100, nullable=False))