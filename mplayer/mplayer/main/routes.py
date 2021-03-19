from flask import render_template, request, Blueprint, url_for
from flask_login import current_user

main = Blueprint('main', __name__)


posts =[]
@main.route("/")
@main.route("/home")
def home():
    if current_user.is_authenticated:
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
        return render_template('home.html', posts=posts, image_file=image_file)
    else:
        return render_template('home.html', posts=posts)  
 