# This Works With `python -m unittest discover`

import unittest
from packjoy import create_app
from packjoy.common.models import db


class MyTest(unittest.TestCase):
	def setUp(self):
		app = create_app(config_filename='config_test.py')
		app.config.from_object('packjoy.config.Testing')
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_index(self):
		response = self.app.get('/')
		print(response)
		self.assertEqual(response.status_code, 400)
		

if __name__ == '__main__':
	unittest.main()