from flask import Flask, render_template, flash
from form_classes import NamerForm, UserForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# add database (kan dit niet in een aparte module?)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# initialise the SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # create a string
    def __repr__(self):
        return '<name %r' % self.name


# secret key
app.config['SECRET_KEY'] = "somepasswordthatonlyiknowhere"


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


# custom error pages
# invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# invalid server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


# FORM test one
@app.route('/login', methods=['GET', 'POST'])
def login():
    name = None
    form = NamerForm()
    # validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("login succes")

    return render_template('login.html',
                           name=name,
                           form=form)


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    # validate form
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data,
                         email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''

        flash("added user")

    our_users = Users.query.order_by(Users.date_added)

    return render_template('add_user.html',
                           name=name,
                           form=form,
                           our_users=our_users)


if __name__ == '__main__':
    app.run()
