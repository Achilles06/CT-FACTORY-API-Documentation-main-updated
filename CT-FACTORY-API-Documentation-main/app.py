from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from blueprints.customer import customer_bp
from blueprints.orders import orders_bp
from blueprints.products import products_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register Blueprints
app.register_blueprint(customer_bp, url_prefix='/api/customers')
app.register_blueprint(orders_bp, url_prefix='/api/orders')
app.register_blueprint(products_bp, url_prefix='/api/products')

# Swagger-UI Configuration
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "CT Factory API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
