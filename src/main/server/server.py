from flask import Flask
from flask_cors import CORS

# Route's
from src.main.routes.app_routes import app_routes_bp

app = Flask(__name__)
CORS(app)

#Register's
app.register_blueprint(app_routes_bp)