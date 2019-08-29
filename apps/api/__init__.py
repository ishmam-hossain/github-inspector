from sanic import Blueprint
from .views import UserOverView


api_bp = Blueprint('api', url_prefix='/api')
api_bp.add_route(UserOverView.as_view(), '/user/<user_name>')
