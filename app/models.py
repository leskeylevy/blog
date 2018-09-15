from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # bio = db.Column(db.String(255))
    # profile_pic_path = db.Column(db.String())

    password_hash = db.Column(db.String(255))

    # photos = db.relationship('PhotoProfile', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__='blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True)
    post = db.Column(db.String(255), index=True)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls,title):
        blog = Blog.query.filter_by(title=title).all()

        return blog

    @classmethod
    def get_pitch_order(cls):
        blog=Blog.query.order_by('id').all()
        return blog

    def __repr__(self):
        return f'BLOG {self.title}'