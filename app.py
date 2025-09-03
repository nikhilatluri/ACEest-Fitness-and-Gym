from flask import Flask
from flask_login import LoginManager
from controller import db, User
from api_v1 import api_v1

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'api_v1.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(api_v1)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
