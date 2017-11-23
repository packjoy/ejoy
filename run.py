from packjoy import create_app


app = create_app('../config_prod.py')

if __name__ == "__main__":
	app.run()