from flask import render_template, url_for, flash, redirect, request
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
import os
from whoosh.analysis import StemmingAnalyzer
import flask_whooshalchemy

# set the location for the whoosh index
whoosh = os.path.join('static')
app.config['WHOOSH_BASE'] = whoosh
# set the global analyzer, defaults to StemmingAnalyzer.
app.config['WHOOSH_ANALYZER'] = StemmingAnalyzer()

PEOPLE_FOLDER = os.path.join('static', 'people_photo')

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
posts = [
    {
        'author': '1',
        'title': 'Clothes',
        'content': 'Here you will get Designers clothing.',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': '2',
        'title': 'Shoes',
        'content': 'All type of Shoes are available here.',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': '3',
        'title': 'Watches',
        'content': 'Here you will get Brand new Watches.',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': '4',
        'title': 'Laptops',
        'content': 'A wide range of Laptops are available.',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': '5',
        'title': 'Smart Phones',
        'content': 'High Rated Smart phones are available.',
        'date_posted': 'April 20, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'flask.jpg')
    return render_template('home.html', posts=posts, user_image = full_filename)
def search():
    query = request.form['search']
   #posts = posts.query.whoosh_search(request.form['search']).all()
    #return render_template('layout.html', posts=posts)
    print(query)

@app.route("/about")
def about():
    return render_template('about.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
