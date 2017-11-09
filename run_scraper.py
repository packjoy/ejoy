from packjoy import db
from packjoy.common.models import User, Role, Email, Token
from scraper.scraper import Scraper as sp

def save_data_to_db(data):
	if data['emails'] is not None:
		business_customer = Role.query.filter_by(name='customer_b').first()
		account = User(email=data['emails'][0], active=True, 
					city=data['city'], emails=[Email(email=e) for e in data['emails']],
					roles=[business_customer])
		db.session.add(account)
		db.session.commit()


