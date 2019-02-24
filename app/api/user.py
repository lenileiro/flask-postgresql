from flask import Blueprint, request, make_response, jsonify

from db.user import UserModel

bp = Blueprint('user-v2', __name__, url_prefix='/api/v2/user')


@bp.route('/signup', methods=['POST'])
def create_account():
    data = request.get_json()
    response = UserModel.insert_user(data)

    return make_response(jsonify({'status': 200, 'data': [response]}), 200)
