import models

import os
import sys
import secrets


from flask import Blueprint, request, jsonify, url_for, send_file
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import current_user
from playhouse.shortcuts import model_to_dict


order = Blueprint('order', 'order', url_prefix="/order")

# create a new order
@order.route('/<id>', methods=["POST"])
def create_order(id):

    user = str(current_user)

    print(user, "THIS IS USER")
    #order = models.Order.create(**payload, user=1)
    order = models.Order.create(user_id=user, product_id=id)
    query = models.Product.update(status=False).where(models.Product.id==id)
    query.execute()
    print(order.__dict__, ' looking inside the data Model', type(order))
    order_dict = model_to_dict(order)
    return jsonify(data=order_dict, status={"code": 201, "message": "Success"})