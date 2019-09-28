from sanic import Sanic
from sanic_cors import CORS
from .api import api_bp


app = Sanic(__name__)
CORS(app)


app.blueprint(api_bp)
