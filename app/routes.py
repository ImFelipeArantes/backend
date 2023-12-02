from flask import Blueprint, request, jsonify
from .models import User, user_schema, users_schema
from. import db
# from .teste import convert_dict
routes = Blueprint('routes',__name__)



@routes.route('/get-users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)

@routes.route('/user-details/<int:id>', methods=['GET'])
def user_datails(id):
    user = User.query.get(int(id))
    if user:
        result = user_schema.dump(user)
        return jsonify(result)
    else:
        return jsonify({'message': 'Usuário não encontrado!', 'type': 'error'})

@routes.route('/create-users', methods=['POST'])
def create_users():
    req = request.get_json()
    user_name = User.query.filter_by(name=req['name']).first()
    user_email = User.query.filter_by(email=req['email']).first()
    if user_name or user_email:
        return jsonify({'message': 'Usuário já cadastrado!', 'type': 'error'})
    user = User(name=req['name'],
                email=req['email'],
                cellphone=req['cellphone'],
                feet=req['feet'],
                color=req['color'],
                country=req['country'],
                city=req['city'],
                gender=req['gender'],
                brand=req['brand'],)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Inscrição feita com sucesso!', 'type': 'success'})

@routes.route('/update-user/<int:id>', methods=['PUT'])
def update_user(id):
    req = request.get_json()
    user = User.query.get(int(id))
    if user:
        user.name = req['name']
        user.email = req['email']
        user.cellphone = req['cellphone']
        user.feet = req['feet']
        user.color = req['color']
        user.country = req['country']
        user.city = req['city']
        user.gender = req['gender']
        user.brand = req['brand']
        db.session.commit()
        return jsonify({'message': 'Atualização feita com sucesso!','type': 'success'})
    else:
        return jsonify({'message': 'Usuário não encontrado!', 'type': 'error'})
@routes.route('/delete-user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(int(id))
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Exclusão feita com sucesso!', 'type': 'success'})
    else:
        return jsonify({'message': 'Usuário não encontrado!', 'type': 'error'})