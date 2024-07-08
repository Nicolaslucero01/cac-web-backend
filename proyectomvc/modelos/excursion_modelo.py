from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship


from app import app, db          #,ma


# defino las tablas
class Excursion(db.Model):   # la clase Excursion hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    descripcion=db.Column(db.String(400))
    duracion=db.Column(db.String(100))
    dificultad=db.Column(db.String(100))
    cupos=db.Column(db.Integer)
    precio=db.Column(db.Integer)
    imagen=db.Column(db.String(400))
    """ tipoexcursion = db.Column(db.Integer) """
    #tipoexcursion = db.relationship('tipoexcursion', backref='funciones')
    
    def __init__(self,nombre,descripcion,duracion,dificultad,cupos,precio,imagen):   #crea el  constructor de la clase
        self.nombre=nombre# no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.descripcion=descripcion
        self.duracion=duracion
        self.dificultad=dificultad
        self.cupos=cupos
        self.precio=precio
        self.imagen=imagen


with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
