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
        products = [model_to_dict(product) for product in models.Product.select().order_by(models.Product.created_at.desc())]
        return jsonify(data=products, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": " There was an error getting the resource"})

# data sets list
@api.route('/datalist', methods=["GET"])
def get_all_data_sets_by_industry():
    try:
        products = [model_to_dict(product) for product in models.Product.select().order_by(models.Product.industry)]
        #query = models.Product.select(*).order_by(models.Product.industry)

        #query.execute()
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


#update product
@api.route('/<id>', methods=["PUT"])
def update_one_data_set(id):

    payload = request.get_json()

    query = models.Product.update(**payload).where(models.Product.id==id)

    query.execute() # run the query, must do for update and delete
    # execute as per the docs returns the row updated

    # if we want to return the updated resource we have to find it
    updated_data_set = models.Product.get_by_id(id)

    return jsonify(data=model_to_dict(updated_data_set), status={"code": 200, "message": "resource updated successfully"})






