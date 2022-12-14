from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import login_required
from flask_login import login_user, current_user, logout_user

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
    comments = Comments.query.all()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            post = Posts(title=form.title.data, content=form.content.data, author=current_user.id)
            form.title.data = ''
            form.content.data = ''
            db.session.add(post)
            db.session.commit()
            flash("Post was submitted successfully. ")
        return render_template('homePage.html', user=current_user, form=form, username=current_user, comments=comments)
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user_object = User.query.filter_by(username=form.username.data).first()
        login_user(user_object)
        user_object.follow(user_object)
        db.session.commit()
        return redirect(url_for('homePage'))
    return render_template('login.html', form=form, user=current_user)

@app.route('/signUp', methods=['GET', 'POST'])
def createAccount():
    form = signUp()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        profile_picture = form.profile_picture.data
        if profile_picture:
            pic_filename = secure_filename(profile_picture.filename)
            pic_name = str(uuid.uuid1()) + "_" + pic_filename
            profile_picture.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
            pic_filename = pic_name
            profile_picture = pic_filename
        user = User(username=username, password=password, profile_picture=profile_picture)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signUp.html', form=form, user=current_user)
    
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

@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@app.route('/search', methods = ['GET', 'POST'])
def search():
    form = SearchForm()
    username = User.query
    if current_user.is_authenticated:
        if form.validate_on_submit():
            username_searched = form.searched.data
            username = username.filter(User.username.like('%' + username_searched + '%'))
            username = username.order_by(User.id).all()
            return render_template('search.html', form=form, searched=username_searched, username=username)
    else:
        flash('Login to search')
        return redirect(url_for('login'))

@app.route("/profile/<username>")
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('No user with that username exists')
        return redirect(url_for('homePage'))
    posts = Posts.query.filter_by(author=user.id).all()
    return render_template('profile.html', user=user, posts=posts, username=username)

@app.route("/follow/<username>")
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User is not found.')
        return redirect(url_for('homePage'))
    if current_user.is_following(user):
        flash("You are already following that user. ")
        return redirect(url_for('homePage'))
    if not current_user.is_following(user):
        current_user.follow(user)
        db.session.commit()
        flash("You are now following: " + username)
        return redirect(url_for('profile',username=user.username))
    return redirect(url_for('homePage'))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User is not found.')
        return redirect(url_for('homePage'))
    if current_user.is_following(user):
        current_user.unfollow(user)
        db.session.commit()
        flash("You have now unfollowed: " + username)
        return redirect(url_for('homePage'))

@app.route("/comment/<posts_id>", methods=['POST'])
def comment(posts_id):
    form = CommentForm()
    content = form.comment.data
    post = Posts.query.filter_by(id=posts_id)
    if not post:
        flash("Cannot comment on that post. ")
    else:
        if form.validate_on_submit():
            comment = Comments(content=content, author=current_user.id, post_id=posts_id)
            db.session.add(comment)
            db.session.commit()
            flash('Comment has been added')
    return redirect(url_for('homePage'))

if __name__ == "__main__":
    app.run(debug=True)
