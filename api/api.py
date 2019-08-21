import models

import os
import sys
import secrets

from PIL import Image
from flask import Blueprint, request, jsonify, url_for, send_file
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict
# first arg is the blueprint name
# second is import name
# 3rd what we prefix to the url
api = Blueprint('api', 'api', url_prefix="/data")

# index page
@api.route('/', methods=["GET"])
def get_all_data_markets():
    try:
        dataMarket = [model_to_dict(product) for product in models.Product.select()]
        return jsonify(data=products, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": " There was an error getting the resource"})

# new data set create
@api.route('/data_id', methods=["POST"])
def create_data_sets():
    ## request object hold the info from the request
    # request.form
    # request.files
    payload = request.get_json()
    print(payload, 'payload', type(payload), 'type')
    # dog = models.Dog.create(name=payload["name"], owner=payload['owner'], breed=payload['breed'])
    # both these line accomplish the same exact task
    data = models.Product.create(**payload, user=1)
    print(datamarket.__dict__, ' looking inside the data Model', type(data))
    data_dict = model_to_dict(datamarket)
    return jsonify(data=data_dict, status={"code": 201, "message": "Success"})

#purchasing page 
@api.route('/<id>', methods=["GET"])
def get_one_data_set(id):
    # note we have to pass the variable name (param)
    # to the view the function
    data = models.Product.get_by_id(id) # peewee query
    return jsonify(data=model_to_dict(data), status={"code": 200, "message": "Success"})

# user profile page
@api.route('/<id>', methods=["GET"])
def get_one_user(id):
    # note we have to pass the variable name (param)
    # to the view the function
    user = models.User.get_by_id(id) # peewee query

    return jsonify(data=model_to_dict(user), status={"code": 200, "message": "Success"})





