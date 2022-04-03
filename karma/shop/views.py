from flask import render_template,  Blueprint, session, redirect, url_for
from karma import db
import json
shop = Blueprint('shop', __name__)


@shop.route('/category', methods=["POST","GET"])
def category():
        products = db.child("products").get().val()
        categories = db.child("categories").get().val()
        return render_template('category.html', products=products, categories = categories)


@shop.route('/cart', methods=["POST","GET"])
def cart():
    if session.get('login'):
        userid = session['id']
        data = db.child("cart").child(session['id']).get().val()
        if data != None:
            totalprice = data['totalprice']
        else:
            totalprice = 0 
        if data:
            data.pop("totalprice")
        session['data'] = data
        session['totalprice'] = totalprice
        return render_template('cart.html', data = data, totalprice=totalprice)
    else:
        return redirect(url_for('pages.login'))


@shop.route('/wishList', methods=["POST","GET"])
def wishList():
    if session.get('login'):
        wldata = db.child('wishList').child(session['id']).get().val()
        return render_template('wishList.html', data = wldata)
    else:
        return  redirect(url_for('pages.login'))


