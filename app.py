from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersneaky'

class derivativeForm(FlaskForm):
    global example
    function = StringField("f(x)=",render_kw={"placeholder": " x**2"})
    submit = SubmitField('Calculate')

@app.route("/",methods=['GET','POST'])
def home():
    function = "x**2"
    derivative = diff(x**2,x)
    integral = integrate(x**2,x)

    form = derivativeForm()

    if form.validate_on_submit():
        function = form.function.data
        form.function.data = ''
        try:
            derivative = diff(function,x)
            integral = integrate(function,x)
        except:
            derivative = 'Error - Cannot Read Input'
            integral = 'Error - Cannot Read Input'

    return(render_template('home.html',form=form,function=function,derivative=derivative,integral=integral))

@app.route("/about")
def about():
    return(render_template('about.html'))

if __name__=="__main__":
    app.run(debug=True)