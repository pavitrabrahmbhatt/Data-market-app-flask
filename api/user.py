import models

import os
import sys
import secrets


from flask import Blueprint, request, jsonify, url_for, send_file

from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict


user = Blueprint('users', 'user', url_prefix='/user')


@user.route('/register', methods=["POST"])
def register():

  # print(request, "REQUEST IS HERE")
  print(request.form, "REQUEST.form IS HERE")


  payload = request.get_json()

  print(payload)
  # print(payload.get('email'))

  try:

    models.User.get(models.User.email == payload.get('email'))

    return jsonify(data={}, status={"code": 401, "message": "A user with that name exists"})

  except models.DoesNotExist:

    payload['password'] = generate_password_hash(payload['password'])

    user = models.User.create(**payload)

    login_user(user)

    user_dict = model_to_dict(user)

    del user_dict['password']

    print(user_dict)

    return jsonify(data=user_dict, status={"code": 201, "message": "Success"})


# User profile page
@user.route('/<id>/account', methods=["GET"])
def get_one_user(id):

    user = models.User.get_by_id(id) # peewee query
    return jsonify(data=model_to_dict(user), status={"code": 200, "message": "Success"})

# Update user
@user.route('/<id>/account', methods=["PUT"])
def update_one_user(id):

    payload = request.get_json()

    query = models.User.update(**payload).where(models.User.id==id)

    query.execute() # run the query, must do for update and delete
    # execute as per the docs returns the row updated

    updated_user = models.User.get_by_id(id)

    return jsonify(data=model_to_dict(updated_user), status={"code": 200, "message": "resource updated successfully"})
