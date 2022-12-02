from flask import Flask, render_template
from loginForm import loginForm

from config import *
from signUp import signUp

@app.route('/')
def homePage():
    return render_template('homePage.html')

@app.route('/login')
def login():
    form = loginForm()
    return render_template('login.html', form=form)

@app.route('/signUp', methods=['GET', 'POST'])
def createAccount():
    form = signUp()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into database! "
    return render_template('signUp.html', form=form)
if __name__ == "__main__":
    app.run(debug=True)