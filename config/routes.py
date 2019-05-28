from app import app
from controllers import farms
from controllers import auth
from controllers import products



app.register_blueprint(farms.router)
app.register_blueprint(auth.router)
app.register_blueprint(products.router)
