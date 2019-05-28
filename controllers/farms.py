from flask import Blueprint, request, jsonify, abort, g
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Farm import Farm, FarmSchema
from lib.secure_route import secure_route

router = Blueprint(__name__, 'farms')

@router.route('/farms', methods=['GET'])
@db_session

def index():
    schema = FarmSchema(many=True)
    farms = Farm.select()
    return schema.dumps(farms)

@router.route('/farms', methods=['POST'])
@db_session
@secure_route
def create():

    schema = FarmSchema()

    try:
        data = schema.load(request.get_json())
        data['user'] = g.current_user
        farm = Farm(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message':'Validation failed', 'errors':err.messages}), 422
    return schema.dumps(farm), 201

@router.route('/farms/<int:farm_id>', methods=['GET'])
@db_session
def show(farm_id):
    schema = FarmSchema()
    farm = Farm.get(id=farm_id)
    if not farm:
        abort(400)
    return schema.dumps(farm)

@router.route('/farms/<int:farm_id>', methods=['PUT'])
@db_session
def update(farm_id):

    schema = FarmSchema()
    farm = Farm.get(id=farm_id)
    if not farm:
        abort(400)
    try:
        data = schema.load(request.get_json())
        data['user'] = g.current_user
        farm.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(farm)


@router.route('/farms/<int:farm_id>', methods=['DELETE'])
@db_session

def delete(farm_id):
    farm = Farm.get(id=farm_id)
    if not farm:
        abort(404)

    farm.delete()
    db.commit()

    return '', 204
