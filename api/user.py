import models

import os
import sys
import secrets


from flask import Blueprint, request, jsonify, url_for, send_file

from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict


user = Blueprint('users', 'user', url_prefix='/user')

@user.route('/login', methods=["POST"])
def login():
    payload = request.get_json()
    print(payload, '< --- this is playload')
    try:
        user = models.User.get(models.User.email== payload['email'])

        user_dict = model_to_dict(user)

        if(check_password_hash(user_dict['password'], payload['password'])):

            del user_dict['password']
            login_user(user)
            print(user, ' this is user')
            return jsonify(data=user_dict, status={"code": 200, "message": "Success"})
        else:
            return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})


@user.route('/register', methods=["POST"])
def register():

  payload = request.get_json()

  print(payload)
  # print(payload.get('email'))

  try:

    models.User.get(models.User.email == payload.get('email'))

    return jsonify(data={}, status={"code": 401, "message": "A user with that name exists"})

  except models.DoesNotExist:


    payload['password'] = generate_password_hash(payload['password']).decode('utf8')

    user = models.User.create(**payload)

    login_user(user)

    print("user")
    print(user)

    user_dict = model_to_dict(user)

    del user_dict['password']

    print("user_dict")
    print(user_dict)

    return jsonify(data=user_dict, status={"code": 201, "message": "Success"})


# User account details
@user.route('/<id>/account', methods=["GET"])
def get_one_user(id):

    user = models.User.get_by_id(id) # peewee query
    return jsonify(data=model_to_dict(user), status={"code": 200, "message": "Success"})


#profile page
@user.route('/<id>', methods=["GET"])
def get_user_profile(id):
    try:
        name = models.User.get_by_id(id).full_name

        orders = [model_to_dict(order) for order in models.Order.select().where(models.Order.user_id==id).order_by(models.Order.created_at.desc())]

        products = [model_to_dict(product) for product in models.Product.select().where(models.Product.user_id==id).order_by(models.Product.industry)]

        return jsonify(all_orders=orders, user_name=name, all_products=products, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": " There was an error getting the resource"})


# Update user
@user.route('/<id>/account', methods=["PUT"])
def update_one_user(id):

    payload = request.get_json()

    query = models.User.update(**payload).where(models.User.id==id)

    query.execute() # run the query, must do for update and delete
    # execute as per the docs returns the row updated

    updated_user = models.User.get_by_id(id)

    return jsonify(data=model_to_dict(updated_user), status={"code": 200, "message": "resource updated successfully"})















