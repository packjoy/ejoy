from flask import Blueprint, jsonify, request, render_template
from flask import abort, redirect, url_for
from flask_security import current_user
from packjoy import pp
from packjoy.common.helpers.moltin_helper import get_prods_by_slug, get_brand_by_slug
from packjoy.common.models import db


site = Blueprint(
			'site', __name__,
			template_folder='templates',
			static_folder='static',
			static_url_path='/static'
)

@site.route('/')
def amp_index():
    products = get_prods_by_slug(slug=None)
    # print('Email: {}'.format(current_user.email))
    # print('Is admin: {}'.format(current_user.has_role('Admin')))
    # print('Roles: {}'.format(current_user.roles))
    return render_template('site/index-amp.html', products=products)

@site.route('/products')
def products():
    products = get_prods_by_slug(slug=None)
    return render_template('site/products-page-amp.html', products=products)

@site.route('/contact-us')
def contact_us():
    products = get_prods_by_slug(slug=None)
    return render_template('site/contact-us-page-amp.html')

@site.route('/checkout')
def checkout():
    products = get_prods_by_slug(slug=None)
    return render_template('site/checkout-page-amp.html')

@site.route('/<brand>')
def amp_brand_page(brand):
    brand = get_brand_by_slug(brand)
    if brand is None:
        # There is No Such a Brand
        # Abort 404
        return redirect(url_for('site.amp_index'))
    return render_template('site/brand-page-amp.html', brand=brand)

@site.route('/<brand>/<product>')
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
    return render_template('site/product-page-amp.html', product=prod, brand=brand_obj)