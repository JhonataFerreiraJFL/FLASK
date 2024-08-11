from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Interger, primary_key=True)
    username = db.Columns(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Intger, primary_key=True)
    content = db.Column(db.Text)
    id_user = db.Column(db.Integer, db.ForeingnKey('user.id'))

    user = db.relationship('User', forenign_keys=id_user)

    def __init__(self, content, id_user):
        self.content = content
        self.id_user = id_user

    def __repr__(self) -> str:
        return '<Post %r>' % self.id
    
class Follow(db.Model):
    __tablename__ = 'follow'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_key= user_id)
    follower = db.relationship('User', foreign_key= follower_id)
