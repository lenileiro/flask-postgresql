from flask import Blueprint, request, make_response, jsonify

from db.user import UserModel
from utils.validator.validateuser import Validate as vl

bp = Blueprint('user-v2', __name__, url_prefix='/api/v2/user')


@bp.route('/signup', methods=['POST'])
def create_account():
    data = request.get_json()
    error = vl.init_data(data)
    if error:
        return make_response(jsonify({'status': 200, 'data': error}), 200)
    else:
        response = UserModel.insert_user(data)
        return make_response(jsonify({'status': 200, 'data': response}), 200)
