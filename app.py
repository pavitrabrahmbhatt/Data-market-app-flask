from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager, login_required
import models

from api.api import api
from api.order import order
from api.user import user


DEBUG = True
PORT = 8000

login_manager = LoginManager()

app = Flask(__name__, static_url_path="", static_folder="static")

app.secret_key = 'RLAKJDRANDOM STRING' # app.use(session({secret_key: 'sd...blah blah blah'}))

login_manager.init_app(app)



@login_manager.user_loader
def load_user(userid):
  try:
    return models.User.get(models.User.id == userid)
  except models.DoesNotExist:
    return None





CORS(api, origins=['http://localhost:3000'], supports_credentials=True)
CORS(user, origins=['http://localhost:3000'], supports_credentials=True)
CORS(order, origins=['http://localhost:3000'], supports_credentials=True)



app.register_blueprint(api)
app.register_blueprint(user)
app.register_blueprint(order)

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


# @app.route('/test')
# @login_required
# def test_login_required():
#   return 'you shouldn\'t be able to see this unless you\'re logged in'

# The default URL ends in / 
@app.route('/')
def index():
    return 'SERVER IS WORKING'

# Run the app when the program starts
if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT, host='0.0.0.0')