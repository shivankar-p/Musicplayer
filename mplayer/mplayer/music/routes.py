from flask import render_template, url_for, flash, redirect, request, Blueprint

music = Blueprint('music', __name__)

@music.route("/browse")
def browse():
    return render_template('browse.html')



    
