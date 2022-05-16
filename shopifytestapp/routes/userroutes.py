"""this file contains all our routes, it is like the controller that determines what happhens when the user visit our app"""
from filecmp import dircmp
import requests, random, os, math
from flask import make_response, render_template, request, redirect, url_for,flash, session
from sqlalchemy import desc

from shopifytestapp import app,db
from shopifytestapp.models import Inventory, Product

"""home"""
@app.route('/')
def home():
    dir=Inventory.query.all()
    prod=Product.query.join(Inventory).filter(Product.inventoryid=='1', Product.status=='active').all()
    prod1=Product.query.join(Inventory).filter(Product.inventoryid=='2', Product.status=='active').all()
    prod2=Product.query.join(Inventory).filter(Product.inventoryid=='3', Product.status=='active').all()
    return render_template('user/index.html', dir=dir, prod=prod, prod1=prod1, prod2=prod2)

"""add inventory"""
@app.route('/addinventory', methods=['POST'])
def addinventory():
    addcat=request.form.get('addinventory')

    #checking if title and level is empty
    if addcat=="":
        flash('Inventory name cannot be empty')
        return redirect('/admin/dashboard/')
    else:        
        #inserting into the database
        bc = Inventory(name=addcat)
        db.session.add(bc)
        db.session.commit()
        flash('Successfully add an inventory')
        return redirect('/')

"""add product"""
@app.route('/addproduct', methods=['POST'])
def addproduct():
    name=request.form.get('name') #category id, also as cake name
    category=request.form.get('inventory')
    size=request.form.get('size')
    description=request.form.get('description')
    price=request.form.get('price')

    if name=="" or size==""  or description=="" or category=="" or price=="":
        flash('one or more field is empty')
        return render_template('user/index.html')
    else:
        #requesting image from form
        image=request.files.get('filename')
        original_name = image.filename
        #checking if file is not empty
        if original_name !="":
            extension = os.path.splitext(original_name)
            if extension[1].lower() in ['.jpg','.png','gif']:
                fn=math.ceil(random.random()*10000000000)
                save_as=str(fn)+extension[1]
                image.save(f'shopifytestapp/static/images/{save_as}')
                
                k=Product(name=name, size=size, description=description, inventoryid=category, price=price, image=save_as)
                db.session.add(k)
                db.session.commit()
                flash('Product Added successfully')
                return redirect('/')
            else:
                flash("File Type Not Allowed")
                return redirect("/")
        else:
            #if no picture supplied
            save_as==""

            k=Product(name=name, size=size, description=description, inventoryid=category, price=price, image=save_as)
            db.session.add(k)
            db.session.commit()
            flash('Product Added successfully')
            return redirect('/')


"""view each product detals"""
@app.route('/detail/<id>')
def detail(id):
    dir=Inventory.query.all()
    prod=Product.query.filter(Product.id==id).first()
    return render_template('user/detail.html', prod=prod, dir=dir)

"""edit product"""
@app.route('/edit/product/<id>')
def editproduct(id):
    dir=Inventory.query.all()
    pro=Product.query.filter(Product.id==id).first()
    return render_template('user/editproduct.html', pro=pro, dir=dir)

"""update product"""
@app.route('/update/product', methods=['POST'])
def update():
    prodid=request.form.get('prodid')
    name=request.form.get('name')
    size=request.form.get('size')
    price=request.form.get('price')
    description=request.form.get('desc')

    if name=="" or size==""  or description=="" or price=="" or id=="":
        flash('one or more field is empty')
        return render_template('user/editproduct.html')
    else:
        #requesting image from form
        image=request.files.get('filename')
        original_name = image.filename
        #checking if file is not empty
        if original_name !="":
            extension = os.path.splitext(original_name)
            if extension[1].lower() in ['.jpg','.png','gif']:
                fn=math.ceil(random.random()*10000000000)
                save_as=str(fn)+extension[1]
                image.save(f'shopifytestapp/static/images/{save_as}')
                k=Product.query.get(prodid)
                k.name=name
                k.size=size
                k.description=description
                k.price=price
                k.image=save_as
                db.session.commit()
                flash('Product Added successfully')
                return redirect(url_for('home'))
            else:
                flash("File Type Not Allowed")
                return redirect("/update/product")
        else:
            #if no picture supplied
            save_as==""

            k=Product.query.get(prodid)
            k.name=name
            k.size=size
            k.description=description
            k.price=price
            k.image=save_as
            db.session.commit()
            flash('Product Added successfully')
            return redirect(url_for('detail'))

"""Delete product"""
@app.route('/delete', methods=['POST'])
def delete():
    prodid=request.form.get("prodid")
    if prodid=="":
        flash('product not deleted due to some errors')
        return redirect(url_for('delete'))
    if prodid !="":
        db.session.execute(f"UPDATE `product` SET `status` = 'deactive' WHERE `product`.`id` = {prodid}") 
        db.session.commit()
        flash('product deleted successfully')
        return render_template('user/delete.html')


"""bages views"""
@app.route('/product/<variable>/<id>')
def bags(variable,id):
    dir=Inventory.query.all()
    bag=Product.query.filter(Product.inventoryid==id).all()
    return render_template('user/bags.html', dir=dir, bag=bag, variable=variable)

"""shoes views"""
@app.route('/product/<variable>/<id>')
def shoes(variable,id):
    dir=Inventory.query.all()
    shoes=Product.query.filter(Product.inventoryid==id).all()
    return render_template('user/shoes.html', dir=dir, shoes=shoes, variable=variable)

"""shoes views"""
@app.route('/product/<variable>/<id>')
def caps(variable,id):
    dir=Inventory.query.all()
    caps=Product.query.filter(Product.inventoryid==id).all()
    return render_template('user/caps.html', dir=dir, caps=caps, variable=variable)


