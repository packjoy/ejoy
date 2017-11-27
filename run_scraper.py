from packjoy import db
from packjoy.common.models import User, Role, Email, Token
from scraper.scraper import Scraper as sp
import pprint

pp = pprint.PrettyPrinter(indent=4)


def save_data_to_db(data):
	'''
	Saves business customers 
	to the db
	'''
	user = User.query.filter_by(name=data['name']).first()
	if user:
		# then update the emails
		for email in [Email(email=e) for e in data['emails'] if Email.query.filter_by(email=e).count() == 0]:
			user.append(e)
		db.session.add(user)
		db.session.commit()
	else:
		# new customer
		business_customer = Role.query.filter_by(name='customer_b').first()
		account = User(active=True, name=data['name'],
					emails=[Email(email=e) for e in data['emails'] if Email.query.filter_by(email=e).count() == 0],
					roles=[business_customer])
		if account.emails:
			db.session.add(account)
			db.session.commit()
	print('Customer Saved')





def run_me(offset=0):
	'''
	This runs the scraping
	script on ZILESINOPTI
	website
	'''
	cities = ['timisoara', 
			'targu-mures', 'satu-mare']
	for city in cities:
		index = offset if offset < 30 else abs(30 - offset)
		current_page = 1
		if offset >= 30:
			current_page = int(offset/30) + 1
		while True:
			print('Going to {} page in {}'.format(current_page, city))
			shop_pages = sp.collect_shop_pages(slug=city, current_page=current_page)
			if not shop_pages:
				break 
			for shop_link in shop_pages[index:]:
				try:
					shop_data = sp.collect_shop_data(url=shop_link)
				except:
					continue
				print('Scraping {} on {} site'.format(shop_data['name'], shop_data['url']))
				model = sp.get_emails_from_page(page=shop_data)
				print('{} email found'.format(len(model['emails'])))
				if len(model['emails']):
					save_data_to_db(model)
			current_page = current_page + 1
			if current_page > 10:
				break
			

def scrape_other_sites():
	shops = list()
	shops.append({ 'name' : 'mindblower', 'url' : 'https://mindblower.ro/'})
	shops.append({ 'name' : 'MrGift', 'url' : 'http://www.mrgift.ro/'})
	shops.append({ 'name' : 'Zaragoo', 'url' : 'http://www.zaragoo.ro/'})
	shops.append({ 'name' : 'TheGift', 'url' : 'http://www.thegift.ro/'})
	shops.append({ 'name' : 'GiftsBoutique', 'url' : 'https://www.giftsboutique.ro/'})
	shops.append({ 'name' : 'Tu.Ro', 'url' : 'https://www.tu.ro/cadouri.html'})
	shops.append({ 'name' : 'Smuff', 'url' : 'https://www.smuff.ro/cadouri/cadouri-traznite'})
	shops.append({ 'name' : 'Cadouri de decoratiuni', 'url' : 'http://www.cadouridecoratiuni.ro/'})
	shops.append({ 'name' : 'BlueGifts', 'url' : 'https://bluegifts.ro/'})
	shops.append({ 'name' : 'Tu.Ro', 'url' : 'https://www.tu.ro/cadouri.html'})

	for shop in shops:
		try: 
			shop_data = sp.get_emails_from_page(page=shop)
		except:
			print('EXCEPT')
			continue
		save_data_to_db(shop_data)


# FIND A SOLUTION FOR THIS
# def stream_read_json(fn='google_results.json'):
# 	import json
# 	start_pos = 0
# 	with open(fn, 'r') as f:
# 		while True:
# 			try:
# 				obj = 'testing'
# 				data = json.load(f)
# 				yield obj
# 			except json.JSONDecodeError as e:
# 				f.seek(start_pos)
# 				print('Error Position: '.format(e.pos))
# 				json_str = f.read(e.pos)
# 				obj = json.loads(json_str)
# 				start_pos += e.pos
# 				yield obj


def scrape_google_search_results(filename='google_results.json'):
	import json
	import pprint as pp
	with open(filename, 'r') as f:
		data = json.load(f)
		for query in data:
			for result in query['results']:
				try:
					user = User.query.filter_by(name=result['domain']).first()
				except:
					db.session.rollback()
					raise
				if not user:
					if not result['link_type'] == 'ads_main':
						try:
							page_info = dict(zip(['name', 'url'], [result['domain'], result['link']]))
							shop_data = sp.get_emails_from_page(page=page_info, fn=save_data_to_db)
							if shop_data['emails'] is not None:
								save_data_to_db(shop_data)
						except:
							print('Error')
							continue
				else: 
					print('Skip this, already in the db')

if __name__ == "__main__":
	scrape_google_search_results(filename='google_results_v2.json')
