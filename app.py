from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
from flask_restful import Api
from db import db
import os
from controllers.heladeria_controller import Heladeria_Controller
from models.user import Users
from flask_login import LoginManager, login_user


load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_database = os.getenv('DB_DATABASE')
secret_key = os.urandom(24)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_database}"
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
api = Api(app)

login_manager = LoginManager()
login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
    user = Users.query.get(id)
    if user:
        return user
    return None

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)  
            return redirect(url_for('resultado', exito=True))
        else:
            return redirect(url_for('resultado', exito=False))
    return render_template("login.html")

@app.route('/resultado')
def resultado():
    exito_param = request.args.get('exito', 'false').lower()  # Convierte a minúsculas
    exito = exito_param == 'true'
    return render_template('resultado.html', exito=exito)



if __name__ == "__main__":
    app.run(debug=True)


