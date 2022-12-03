from flask import Flask, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required

from config import *
from signUp import signUp, loginForm

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user_object = User.query.filter_by(username=form.username.data).first()
        login_user(user_object)
        if current_user.is_authenticated:
            return redirect(url_for('profile'))
        return "Not logged in :("

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
        return redirect(url_for('profile'))
    return render_template('signUp.html', form=form)

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return "Can only go here if logged in"

@app.route('/logout', methods = ['GET'])
def logout():
    logout_user()
    flash("You have been logged out. ")
    return redirect(url_for('login'))

@app.route('/delete', methods = ['GET', 'POST'])
@login_required
def delete():
    current_user.delete()
    db.session.commit()
    flash('Your account has been successfully deleted.')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)