from flask import Flask, render_template
from form_classes import NamerForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
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

    return render_template('login.html',
                           name=name,
                           form=form)


if __name__ == '__main__':
    app.run()
