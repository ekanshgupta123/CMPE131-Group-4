from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def homePage():
    user = {'username' : 'Ekansh'}
    return render_template('homePage.html', title = 'Blog', username = user['username'])

@app.route('/login')
def login():
    # form = LoginForm()
    return render_template('login.html', title = 'Sign In')

if __name__ == "__main__":
    app.run(debug=True)