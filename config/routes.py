from app import app
from controllers import farms
from controllers import auth
from controllers import products



app.register_blueprint(farms.router, url_prefix='/api')
app.register_blueprint(auth.router, url_prefix='/api')
app.register_blueprint(products.router, url_prefix='/api')
