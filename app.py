from flask import Flask, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required

from config import *
from signUp import *
from werkzeug.utils import secure_filename
import uuid as uuid

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/', methods = ['GET', 'POST'])
def homePage():
    form = PostForm()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            post = Posts(title=form.title.data, content=form.content.data)
            form.title.data = ''
            form.content.data = ''
            db.session.add(post)
            db.session.commit()
            flash("Post was submitted successfully. ")
        return render_template('homePage.html', user=current_user, form=form)
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user_object = User.query.filter_by(username=form.username.data).first()
        login_user(user_object)
        if current_user.is_authenticated:
            return redirect(url_for('profile'))
    return render_template('login.html', form=form, user=current_user)

@app.route('/signUp', methods=['GET', 'POST'])
def createAccount():
    form = signUp()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        profile_picture = form.profile_picture.data
        
        pic_filename = secure_filename(profile_picture.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        profile_picture.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
        pic_filename = pic_name

        user = User(username=username, password=password, profile_picture=pic_filename)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('signUp.html', form=form, user=current_user)

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    posts = Posts.query.order_by(Posts.date_posted)
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('profile.html', user=current_user, posts=posts)

@app.route('/logout', methods = ['GET'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("You have been logged out. ")
        return redirect(url_for('login'))
    flash("You are not logged in. ")
    return redirect(url_for('login'))

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    if current_user.is_authenticated:
        current_user.delete()
        db.session.commit()
        flash('Your account has been successfully deleted.')
        return redirect(url_for('login'))
    flash("You are not logged in. ")
    return redirect(url_for('login'))
        

if __name__ == "__main__":
    app.run(debug=True)