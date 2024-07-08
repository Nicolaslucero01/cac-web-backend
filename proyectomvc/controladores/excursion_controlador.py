from flask import jsonify, request
from app import app, db, ma
from modelos.excursion_modelo import Excursion  # Importa la clase Excursion con la primera letra en mayúscula

class ExcursionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'descripcion', 'duracion', 'dificultad', 'cupos', 'precio', 'imagen')

excursion_schema = ExcursionSchema()           # El objeto excursion_schema es para traer un excursion
excursiones_schema = ExcursionSchema(many=True) # El objeto excursiones_schema es para traer multiples registros de excursion

# crea los endpoint o rutas (json)
@app.route('/excursiones', methods=['GET'])
def get_excursiones():
    all_excursiones = Excursion.query.all()         # el metodo query.all() lo hereda de db.Model
    result = excursiones_schema.dump(all_excursiones)  # el metodo dump() lo hereda de ma.schema y trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla

@app.route('/excursiones/<id>', methods=['GET'])
def get_excursion(id):
    excursion = Excursion.query.get(id)
    return excursion_schema.jsonify(excursion)   # retorna el JSON de un excursion recibido como parametro

@app.route('/excursiones/<id>', methods=['DELETE'])
def delete_excursion(id):
    excursion = Excursion.query.get(id)
    db.session.delete(excursion)
    db.session.commit()
    return excursion_schema.jsonify(excursion)   # me devuelve un json con el registro eliminado

@app.route('/excursiones', methods=['POST']) # crea ruta o endpoint
def create_excursion():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    duracion = request.json['duracion']
    dificultad = request.json['dificultad']
    cupos = request.json['cupos']
    precio = request.json['precio']
    imagen = request.json['imagen']
    new_excursion = Excursion(nombre, descripcion, duracion, dificultad, cupos, precio, imagen)
    db.session.add(new_excursion)
    db.session.commit()
    return excursion_schema.jsonify(new_excursion)

@app.route('/excursiones/<id>', methods=['PUT'])
def update_excursion(id):
    excursion = Excursion.query.get(id)

    excursion.nombre = request.json['nombre']
    excursion.descripcion = request.json['descripcion']
    excursion.duracion = request.json['duracion']
    excursion.dificultad = request.json['dificultad']
    excursion.cupos = request.json['cupos']
    excursion.precio = request.json['precio']
    excursion.imagen = request.json['imagen']

    db.session.commit()
    return excursion_schema.jsonify(excursion)



@app.route('/')
def bienvenida():
    return "Bienvenidos al backend"   # retorna el JSON de un usuario recibido como parametro
