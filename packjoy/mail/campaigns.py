from flask import render_template
from packjoy.common.helpers.moltin_helper import get_brand_by_slug, get_prods_by_slug
from packjoy.common.models import Token


'''
The campaigns are responsible for
	- collecting the data for templates:
		- products
		- brand
		- token (welcome template)
	- loading the template
'''
class Base:
	campaign_type = None
	brand = get_brand_by_slug(brand_slug='packjoy')
	products = get_prods_by_slug(slug=None)

	def __init__(self, template_name=None):
		self.template = self.load_template(template_name=template_name,
				products=self.products, brand=self.brand)

	def load_template(self, template_name, *args, **kwargs):
		return render_template('mail/{}.html'.format(template_name), *args, **kwargs)

	def __repr__(self):
		return 'campaign'




class PriceDecrease(Base):
	def __init__(self, template_name='price_decrease'):
		Base.__init__(self, template_name=template_name)



class BackInStock(Base):
	def __init__(self, template_name='back_in_stock'):
		Base.__init__(self, template_name=template_name)



class Welcome(Base):
	def __init__(self, template_name, token=None):
		Base.__init__(self, template_name=template_name or 'token')
		print(token)
		self.token = token
		self.template = self.load_template(template_name=template_name, products=self.products,
									brand=self.brand, token=self.token.token_code)



class NewArrivals(Base):
	def __init__(self, template_name='new_arrivals'):
		Base.__init__(self, template_name=template_name)

