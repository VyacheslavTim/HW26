from flask import Blueprint, request, jsonify

from entity import User
from models import BatchRequestSchema
from utils import build_query

main_bp = Blueprint('main', __name__)

FILE_NAME = 'data/apache_logs.txt'


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json
    validated_data = BatchRequestSchema().load(data)

    result = None
    for query in validated_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=FILE_NAME,
            data=result,
        )

    return jsonify(result)


@main_bp.route('/users')
def get_users():
    result = User.query.all()

    return [
        {
            'id': user.id,
            'username': user.username,
        } for user in result
    ]