from packjoy import db
from packjoy.common.models import User, Role, Email, Token
from scraper.scraper import Scraper as sp

def save_data_to_db(data):
	data['emails'] = list(data['emails'])
	if len(data['emails']) is not None:
		business_customer = Role.query.filter_by(name='customer_b').first()
		account = User(active=True, name=data['name'],
					city=data['city'], emails=[Email(email=e) for e in data['emails']],
					roles=[business_customer])
		db.session.add(account)
		db.session.commit()




def run_me(offset=0):
	cities = ['bucuresti', 'cluj-napoca',
			'brasov', 'timisoara', 
			'targu-mures', 'satu-mare']
	for city in cities:
		index = offset if offset < 30 else abs(30 - offset)
		current_page = 1 if offset < 30 else int(offset/30) + 1 
		while True:
			shop_pages = sp.collect_shop_pages(slug=city, current_page=current_page)
			if not shop_pages:
				break 
			print('Going to {} page in {}'.format(current_page, city))
			for shop_link in shop_pages[index:]:
				try:
					shop_data = sp.collect_shop_data(url=shop_link)
				except:
					break
				print('Scraping {} on {} site'.format(shop_data['name'], shop_data['url']))
				model = sp.get_emails_from_page(page=shop_data)
				print('{} email found'.format(len(model['emails'])))
				if len(model['emails']):
					save_data_to_db(model)
					print('Customer Saved')
			current_page = current_page + 1
			




# def create_roles():
# 	roles = [Role(name='Admin', description='Admin Role'), 
# 		Role(name='customer_b', description='Scraped Business Customers')]
# 	for role in roles:
# 		db.session.add(role)
# 	db.session.commit()

# def create_super_user():
# 	user=User(password='gyerebe123', active=True, email='szeka1994@gmail.com', roles=Role.query.all())
# 	db.session.add(user)
# 	db.session.commit()



if __name__ == "__main__":
	# db.create_all()
	# create_roles()
	# create_super_user()
	run_me(offset=21)
