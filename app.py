from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

db_path = os.path.join(os.path.dirname(__file__), 'database.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SECRET_KEY'] = 'thisisasecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

if __name__ == '__main__':
	app.run(debug=True)