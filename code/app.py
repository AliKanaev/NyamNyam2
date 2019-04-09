from flask import Flask
from config import Configuration

from foods.blueprint import foods

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(foods, url_prefix='/admin')