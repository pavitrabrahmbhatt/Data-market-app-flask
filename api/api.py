import models

from flask import Blueprint, request, jsonify, url_for, send_file
from playhouse.shortcuts import model_to_dict

# first arg is the blueprint name
# second is import name
# 3rd what we prefix to the url
api = Blueprint('api', 'api', url_prefix="/data")

# index page
@api.route('/', methods=["GET"])
def get_all_data_markets():
    try:
        products = [model_to_dict(product) for product in models.Product.select()]
        return jsonify(data=products, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": " There was an error getting the resource"})

# new data set create
@api.route('/sell', methods=["POST"])
def create_data_sets():
    payload = request.get_json()
    print(payload, 'payload', type(payload), 'type')
    product = models.Product.create(**payload, user=1)
    print(product.__dict__, ' looking inside the data Model', type(product))
    product_dict = model_to_dict(product)
    return jsonify(data=product_dict, status={"code": 201, "message": "Success"})

#purchasing page 
@api.route('/<id>', methods=["GET"])
def get_one_data_set(id):
    # note we have to pass the variable name (param)
    # to the view the function
    product = models.Product.get_by_id(id) # peewee query
    return jsonify(data=model_to_dict(product), status={"code": 200, "message": "Success"})

# user profile page
@api.route('/<id>', methods=["GET"])
def get_one_user(id):
    # note we have to pass the variable name (param)
    # to the view the function
    user = models.User.get_by_id(id) # peewee query
    return jsonify(data=model_to_dict(user), status={"code": 200, "message": "Success"})





