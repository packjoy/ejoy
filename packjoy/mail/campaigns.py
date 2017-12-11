from flask import render_template
from packjoy.common.helpers.moltin_helper import get_brand_by_slug, get_prods_by_slug
from packjoy.common.models import Token


class Base:
	campaign_type = None
	brand = get_brand_by_slug(brand_slug='packjoy')
	products = get_prods_by_slug(slug=None)

	def __repr__(self):
		return self.campaign_type


class PriceDecrease(Base):
	def __init__(self, template_name='price_decrease'):
		self.template = render_template('mail/{}.html'.format(template_name),
							products=self.products)


class BackInStock(Base):
	def __init__(self, template_name='back_in_stock'):
		self.template = render_template('mail/{}.html'.format(template_name),
							products=self.products)


class Welcome(Base):
	def __init__(self, template_name='token', token=None):
		self.token = 'INVALID_TOKEN_OBJECT'
		self.template = render_template('mail/{}.html'.format(template_name),
							products=self.products, brand=self.brand, token=self.token)


class NewArrivals(Base):
	def __init__(self, template_name='new_arrivals'):
		self.template = render_template('mail/{}.html'.format(template_name),
							products=self.products)
