from packjoy import create_app


app = create_app('../config_prod.py')
app.run()