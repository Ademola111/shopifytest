from dataclasses import fields
import re

from sqlalchemy import ForeignKey
from shopifytestapp import db, ma

class Inventory(db.Model):
    id=db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name=db.Column(db.String(255), nullable=False)

    #relationship setup
    productobj = db.relationship('Product', back_populates='inventoryobj')

    def __init__(self, name):
        self.name=name

class InventorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class Product(db.Model):
    id=db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name=db.Column(db.String(255), nullable=False)
    price=db.Column(db.Float(), nullable=False)
    description=db.Column(db.Text(), nullable=False)
    size=db.Column(db.String(255), nullable=False)
    image=db.Column(db.String(255), nullable=False)
    status=db.Column(db.Enum('active','deactive'))
    #foreignkey setup
    inventoryid=db.Column(db.Integer(), db.ForeignKey('inventory.id'))

    #relationship setup
    inventoryobj = db.relationship('Inventory', back_populates='productobj')

    def __init__(self, name, price, description, size, image, status, inventoryid):
        self.name=name
        self.price = price
        self.description = description
        self.size = size
        self.image = image
        self.status = status
        self.inventoryid= inventoryid

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price', 'description', 'size', 'image', 'status', 'inventoryid')


