from app import db

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mail = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Campo para identificar si el usuario es administrador

    def __init__(self, mail, password, is_admin=False):
        self.mail = mail
        self.password = password
        self.is_admin = is_admin

