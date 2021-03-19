from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from mplayer import db, login_manager
from flask import current_app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)               #db structure
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expires_sec=900):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id) #querying db for user

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class sng_in_pl(db.Model):
    __tablename__ = 'sng_in_pl'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    playlist = db.Column(db.String(20), nullable=False)
    song = db.Column(db.String(20), unique=True, nullable=False)

