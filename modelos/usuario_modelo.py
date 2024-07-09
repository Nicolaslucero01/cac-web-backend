from app import app, db   #,ma
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
# defino las tablas
class Usuario(db.Model):   # la clase Producto hereda de db.Model de SQLAlquemy   
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(255))
    clave=db.Column(db.String(255))
    nivel=db.Column(db.String(50))
    
    def __init__(self,nombre,clave): #crea el  constructor de la clase
        self.nombre=nombre # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.clave=clave
        self.nivel=nivel
        


with app.app_context():
    db.create_all()  # aqui crea todas las tablas si es que no estan creadas
#  ************************************************************

