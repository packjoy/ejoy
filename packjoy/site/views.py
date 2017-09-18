from flask import Blueprint jsonify, request, render_template
from flask import abort, redirect, url_for

from packjoy import db, pp
from packjoy.common.helpers.moltin_helper import get_prods_by_slug, get_brand_by_slug


site = Blueprint('site', __name__)


@site.route('/')
def index():
    return render_template('index.html')

@site.route('/amp/')
def amp_index():
    products = get_prods_by_slug(slug=None)
    return render_template('index-amp.html', products=products)

@site.route('/amp/products')
def products():
    products = get_prods_by_slug(slug=None)
    return render_template('products-page-amp.html', products=products)

@site.route('/amp/contact-us')
def contact_us():
    products = get_prods_by_slug(slug=None)
    return render_template('contact-us-page-amp.html')

@site.route('/amp/checkout')
def checkout():
    products = get_prods_by_slug(slug=None)
    return render_template('checkout-page-amp.html')

@site.route('/amp/<brand>')
def amp_brand_page(brand):
    brand = get_brand_by_slug(brand)
    if brand is None:
        # There is No Such a Brand
        # Abort 404
        return redirect(url_for('amp_index'))
    return render_template('brand-page-amp.html', brand=brand)

@site.route('/amp/<brand>/<product>')
def amp_product_page(brand, product):
    prod = get_prods_by_slug(product)
    if prod is None:
        # There is no such a prduct
        # raise a 404 Error
        abort(404) 
    brand_slug = prod.brand['slug']
    brand_obj = get_brand_by_slug(brand)
    if brand_slug != brand:
        return redirect(url_for('amp_product_page', brand=prod.brand['slug'], product=prod.slug))
    return render_template('product-page-amp.html', product=prod, brand=brand_obj)