from app import app, db   #,ma
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

# defino las tablas
class Excursion(db.Model):   # la clase Producto hereda de db.Model de SQLAlquemy   
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(400))
    duracion=db.Column(db.String(100))
    descripcion=db.Column(db.String(400))
    dificultad=db.Column(db.String(100))
    imagen=db.Column(db.String(800))
    cupos=db.Column(db.Integer)
    precio=db.Column(db.Integer)
    def __init__(self,nombre,duracion,descripcion,dificultad,imagen,cupos,precio): #crea el  constructor de la clase
        self.nombre=nombre # no hace falta el idorque lo crea sola mysql por ser auto_incremento
        self.duracion=duracion
        self.descripcion=descripcion
        self.dificultad=dificultad
        self.imagen=imagen
        self.cupos=cupos
        self.precio=precio




    #  si hay que crear mas tablas , se hace aqui
# defino las tablas
"""class Usuario(db.Model):   # la clase Producto hereda de db.Model de SQLAlquemy   
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    contrasenia=db.Column(db.Integer)
    
    def __init__(self,nombre,contrasenia): #crea el  constructor de la clase
        self.nombre=nombre # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.contrasenia=contrasenia
        
"""


with app.app_context():
    db.create_all()  # aqui crea todas las tablas si es que no estan creadas
#  ************************************************************
