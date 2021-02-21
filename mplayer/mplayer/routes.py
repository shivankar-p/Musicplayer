import secrets
import os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from mplayer.forms import (RegistrationForm, LoginForm, UpdateAccountForm, 
                           RequestResetPasswordForm, ResetPasswordForm)
from mplayer.models import User
from mplayer import app, db, bcrypt, mail
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


count = 0

posts =[]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.create_all()
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You\'ll be able to log in now.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Register', form=form)   

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()   #queries through db for email
        if(user and bcrypt.check_password_hash(user.password, form.password.data)):    #pwd validation
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))   #ternary conditional
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():    
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)  
    _, f_ext = os.path.splitext(form_picture.filename)  #storing extension and leaving file name
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)  #function to save pic
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn   

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    global count   
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file) 
    if(count == 1):
        flash('Your account has been updated', 'success')
        count = 0
    return render_template('account.html', title='Account', image_file=image_file)

@app.route("/updateaccount", methods=['GET', 'POST'])
@login_required
def updateaccount(): 
    global count
    count = 1   
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif(request.method == 'GET'):
        form.username.data = current_user.username
        form.email.data = current_user.email    
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('updateaccount.html', title='Update Account info',
                           image_file=image_file, form=form)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@musico.com',
                  recipients=[user.email])             
    msg.body = f'''Hey {user.username},
To reset your password, click on the following link:
{url_for('reset_token', token=token, _external=True)}  
This link is only valid for 15 minutes.
If you did not make this request for password reset, please ignore this email.

Thanks,
Musico team
'''
    mail.send(msg)

@app.route("/reset_password", methods=['GET', 'POST'])
def request_reset():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if(current_user.is_authenticated):
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if(user is None):
        flash('That is an invalid or expired url', 'warning')
        return redirect(url_for('request_reset'))
    form = ResetPasswordForm()
    if(form.validate_on_submit()):
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #editing pwd
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You\'ll be able to log in now.', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

  
  