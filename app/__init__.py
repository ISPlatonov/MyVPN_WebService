import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
app = flask.Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.log_in'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

# open config.json into config dict
import json
with open('app/config.json', 'r') as file:
    config = json.load(file)

app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

# blueprint for auth routes in our app
from app.routes.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from app.routes.routes import routes as routes_blueprint
app.register_blueprint(routes_blueprint)


with app.app_context():
    db.create_all()
