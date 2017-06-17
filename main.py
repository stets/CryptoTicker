from flask import Flask, render_template, request
import ticker
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email

app = Flask(__name__)


class LoginForm(Form):
    qty = StringField('username', validators=[InputRequired(), Email()])
    password = StringField('password', validators=[InputRequired()])


@app.route('/')
def root():
    price, symbol = ticker.getPrice() 
    return render_template('index.html', price=price, symbol=symbol)

@app.route('/test', methods=['GET', 'POST'])
def test():
    form = LoginForm()


if __name__ == '__main__':
    app.run()
