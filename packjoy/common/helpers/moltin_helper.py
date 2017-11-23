from flask import current_app
from packjoy import pp
from packjoy.common.models import Product, Brand
from moltin.exception import RequestError
from moltin.moltin import Moltin


# Moove somewhere else
m = Moltin(current_app.config['MOLTIN_CLIENT_ID'], current_app.config['MOLTIN_CLIENT_SECRET'])
access_token = m.authenticate()

product = m.Product

# A freeeeaking helper 
# to get an index of a list, 
# or handle exception
def get_list_index(list, di, default):
	try:
		return list[di]
	except:
		return default


# Gives us back a product dictionary
# (Product Model instances)
# or None
# based on slug
def get_prods_by_slug(slug):
	if slug is None:
		try:
			prod_list = product.list()
			data = [Product(prod) for prod in prod_list]
		except TypeError as e:
			print(e)
			print(product.list())
		except RequestError as e:
			print('Request error: {}'.format(str(e)))
			return None
		return data
	try:
		data = m.get('products/?slug={}'.format(slug))				
	except RequestError as e:
		data = e
		print('Request Error: {}'.format(e))
	except:
		print(m.get('products/?slug={}'.format(slug))+'asdasdsa')
	prod = get_list_index(data, 0, None)
	if prod:
		return Product(prod)
	else: 
		return None

# Gives back a brand object (model)
# or None
def get_brand_by_slug(brand_slug):
	# Test this
	data = product.list()
	data = [prod for prod in data if prod['brand']['data']['slug'] == brand_slug]
	if len(data) == 0 or data is None:
		return None
	prod_list = [Product(prod) for prod in data]
	brand = Brand(products=prod_list)
	return brand