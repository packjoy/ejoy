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
		template_name = template_name if template_name is not None else self.campaign_type
		return render_template('mail/{}.html'.format(template_name), *args, **kwargs)

	def __repr__(self):
		return 'campaign'




class PriceDecrease(Base):
	campaign_type = 'price_decrease'
	def __init__(self, template_name=None):
		Base.__init__(self, template_name=template_name)



class BackInStock(Base):
	campaign_type = 'back_in_stock'
	def __init__(self, template_name=None):
		Base.__init__(self, template_name=template_name)



class Welcome(Base):
	campaign_type = 'token'
	def __init__(self, template_name=None, token=None):
		Base.__init__(self, template_name)
		self.token = token
		self.template = self.load_template(template_name=template_name, products=self.products,
									brand=self.brand, token=self.token.token_code)



class NewArrivals(Base):
	campaign_type = 'new_arrivals'
	def __init__(self, template_name=None):
		Base.__init__(self, template_name=template_name)

