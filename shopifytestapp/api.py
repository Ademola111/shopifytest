""" API Section """
from flask_sqlalchemy import SQLAlchemy
import requests, random, os, math
from flask import request, flash, session, jsonify
from sqlalchemy import desc
from flask_marshmallow import Marshmallow

from shopifytestapp import app,db, csrf
from shopifytestapp.models import Inventory, Product, ProductSchema, InventorySchema

""" product schema"""
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

"""inventory schema"""
inventory_schema = InventorySchema()
inventories_schema = InventorySchema(many=True)




"""get all products"""
@app.route('/product/v1/get', methods=['GET'])
def get_product():
    pdt=db.session.query(Product).all()
    results= products_schema.dump(pdt)
    return jsonify(results)

"""get individual product"""
@app.route('/product/v1/get/<id>', methods=['GET'])
def get_one_product(id):
    pdt=db.session.query(Product).get(id)
    result= product_schema.dump(pdt)
    return jsonify(result)

"""get all inventory"""
@app.route('/inventory/v1/get', methods=['GET'])
def get_inventory():
    inv=db.session.query(Inventory).all()
    results= inventories_schema.dump(inv)
    return jsonify(results)

"""get individual inventory"""
@app.route('/inventory/v1/get/<id>', methods=['GET'])
def get_one_inventory(id):
    inv=db.session.query(Inventory).get(id)
    result= inventory_schema.dump(inv)
    return jsonify(result)
    

"""Post products"""
@app.route('/product/v1/add', methods=['POST'])
@csrf.exempt
def add_product():
    name = request.json['name']
    price = request.json['price']
    description = request.json['description']
    size = request.json['size']
    image = request.json['image']
    status = "active"
    inventoryid = request.json["inventoryid"]

    if name !="" or size!=""  or description!="" or inventoryid !="" or price!="":
        prots=Product(name=name, size=size, description=description, price=price, status=status, inventoryid=inventoryid, image=image)
        db.session.add(prots)
        db.session.commit()
        return product_schema.jsonify(prots)
    


"""Post inventory"""
@app.route('/inventory/v1/add', methods=['POST'])
@csrf.exempt
def add_inventory():
    name = request.json['name']
    if name != "":
        invent = Inventory(name)
        db.session.add(invent)
        db.session.commit()
        return inventory_schema.jsonify(invent)

"""Put api for image update"""
@app.route('/product/v1/update/<id>', methods=['PUT'])
@csrf.exempt
def add_image(id):
    img=request.files['file']
    original_name = img.filename
    #checking if file is not empty
    if original_name !="":
        extension = os.path.splitext(original_name)
        if extension[1].lower() in ['.jpg','.png','gif']:
            fn=math.ceil(random.random()*10000000000)
            save_as=str(fn)+extension[1]
            img.save(f'shopifytestapp/static/images/{save_as}')
            imag=Product.query.get(id)
            imag.image=save_as
            db.session.commit()
            return product_schema.jsonify(imag)

"""Put api for content update"""
@app.route('/product/v1/update/content/<id>', methods=['PUT'])
@csrf.exempt
def update_content(id):
    name = request.json['name']
    price = request.json['price']
    description = request.json['description']
    size = request.json['size']
    status = "active"
    inventoryid = request.json["inventoryid"]
    content=Product.query.get(id)
    content.name=name
    content.price=price
    content.descriprion=description
    content.size=size
    content.status=status
    content.inventoryid=inventoryid
    db.session.commit()
    return product_schema.jsonify(content)


"""Put api for inventory update"""
@app.route('/inventory/v1/update/<id>', methods=['PUT'])
@csrf.exempt
def update_inventory(id):
    name = request.json['name']
    
    evnt=Inventory.query.get(id)
    evnt.name=name
    db.session.commit()
    return inventory_schema.jsonify(evnt)

"""Delete api for product"""
@app.route('/product/v1/delete/<id>', methods=['DELETE'])
@csrf.exempt
def delete_product(id):
    produ=Product.query.get(id)
    db.session.delete(produ)
    db.session.commit()
    return product_schema.jsonify(produ)

"""Delete api for invetory"""
@app.route('/inventroy/v1/delete/<id>', methods=['DELETE'])
@csrf.exempt
def delete_inventory(id):
    evet=Inventory.query.get(id)
    db.session.delete(evet)
    db.session.commit()
    return inventory_schema.jsonify(evet)