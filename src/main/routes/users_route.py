from flask import Blueprint, jsonify

user_routes_bp = Blueprint('user_routes', __name__)

@user_routes_bp.route('/user', methods=['POST'])
def registry_user():
    # logica e componentes
    return jsonify({"rota": "Rota de cadastro de usuário"}), 200
