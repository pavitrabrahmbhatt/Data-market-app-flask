from peewee import *
from flask_login import UserMixin
import datetime

DATABASE = SqliteDatabase('datamarket.sqlite')

# User Model
class User(UserMixin, Model): 
    full_name = CharField()
    email = CharField(unique=True)
    password = CharField()
    organization_name = CharField()
    job_title = CharField()

    class Meta:
        database = DATABASE

# Data set model
class Product(Model):
    name = CharField()
    price = IntegerField()
    user_id = ForeignKeyField(User, backref='products', null=False)
    created_at = DateTimeField(default=datetime.datetime.now)
    industry = CharField()
    description = TextField()
    territory = CharField()
    status = BooleanField(default=True)
    source = TextField()

    class Meta:
        database = DATABASE

#Order Model

class Order(Model): 
    user_id = ForeignKeyField(User, backref='orders', null=False)
    product_id = ForeignKeyField(Product, backref='products', null=False, unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class CreditCard(Model):
    name = CharField()
    number = IntegerField()
    ccv = IntegerField()
    expiration_date = DateTimeField()

    class Meta:
        database = DATABASE

class UserCard(Model):
    user_id = ForeignKeyField(User, backref='users', null=False)
    credit_card_id = ForeignKeyField(CreditCard, backref='credit_cards', null=False)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Product, Order, CreditCard, UserCard], safe=True)
    print("TABLES Created")
    DATABASE.close()