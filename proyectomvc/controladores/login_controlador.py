from flask import jsonify, request, redirect, url_for
from app import app, db
from Modelos.login_modelo import Login

@app.route('/login', methods=['POST'])
def login():
    mail = request.json['mail']
    password = request.json['password']
    
    user = Login.query.filter_by(mail=mail).first()
    
    if user and user.password == password:
        if user.is_admin:
            return jsonify({'message': 'Login successful', 'redirect': '/admin'})
        else:
            return jsonify({'message': 'Login successful', 'redirect': '/user-dashboard'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/register', methods=['POST'])
def register():
    mail = request.json['mail']
    password = request.json['password']
    
    new_user = Login(mail, password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'})

@app.route('/admin')
def admin():
    return render_template('excursiones.html')  # Página para administradores

@app.route('/user-dashboard')
def user_dashboard():
    return render_template('index.html')  # Página para usuarios normales

