import models

from flask import Blueprint, request, jsonify, url_for, send_file
from playhouse.shortcuts import model_to_dict


api = Blueprint('order', 'order', url_prefix="/order")

@api.route('/<id>', methods=["POST"])
def create_order(id):

    payload = request.get_json()
    print(payload, 'payload', type(payload), 'type')
    order = models.Order.create(**payload, user=1)
    print(order.__dict__, ' looking inside the data Model', type(order))
    order_dict = model_to_dict(order)
    return jsonify(data=order_dict, status={"code": 201, "message": "Success"})