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

  payload = request.get_json()

  print(payload)
  # print(payload.get('email'))

  try:

    models.User.get(models.User.email == payload.get('email'))

    return jsonify(data={}, status={"code": 401, "message": "A user with that name exists"})

  except models.DoesNotExist:

    print("ok to create")

    payload['password'] = generate_password_hash(payload['password'])

    user = models.User.create(**payload)

    login_user(user)

    print("user")
    print(user)

    user_dict = model_to_dict(user)

    del user_dict['password']

    print("user_dict")
    print(user_dict)

    return jsonify(data=user_dict, status={"code": 201, "message": "Success"})
