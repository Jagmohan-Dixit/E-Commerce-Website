import sys

from flask import render_template, Blueprint, session
import json
import os
from karma import app, db


blog = Blueprint('blog', __name__)

@blog.route('/blogs')
def blogs():
    return render_template('blogs.html')

@blog.route('/singleblog')
def singleblog():
    return render_template('singleblog.html')

@blog.route('/') 
def index():
    filename = os.path.join(app.static_folder, 'json/feature.json') 
    f = open(filename) 
    file = json.load(f) 
    products = db.child("products").get().val()
    hotdealsproductfromDB = db.child('hotdealsproduct').get().val()
    unpackedproduct = {}
    hotdealsid = ""
    hotdealsproducts = {}
    for key,value in hotdealsproductfromDB.items():
        for keyinner, valueinner in value.items():
            hotdealsproducts[keyinner] = valueinner
    return render_template('index.html', data=file , hotdealsproducts = hotdealsproductfromDB, products=products)

