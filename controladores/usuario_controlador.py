from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request

from app import app, db,ma

from modelos.usuario_modelo import  *

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','clave','nivel')


usuario_schema=UsuarioSchema()  # El objeto producto_schema es para traer un producto
usuarios_schema=UsuarioSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto




# crea los endpoint o rutas (json)
@app.route('/usuarios',methods=['GET'])
def get_Usuarios():
    all_usuarios=Usuario.query.all() # el metodo query.all() lo hereda de db.Model
    result=usuarios_schema.dump(all_usuarios)  #el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)     # retorna un JSON de todos los registros de la tabla




@app.route('/usuarios/<id>',methods=['GET'])
def get_usuario(id):
    usuario=Usuario.query.get(id)
    return usuario_schema.jsonify(usuario)   # retorna el JSON de un producto recibido como parametro


@app.route('/usuarios/<id>',methods=['DELETE'])
def delete_usuario(id):
    usuario=Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()                     # confirma el delete
    return usuario_schema.jsonify(usuario) # me devuelve un json con el registro eliminado


@app.route('/usuarios', methods=['POST']) # crea ruta o endpoint
def create_usuario():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    clave=request.json['clave']
    nivel=request.json['nivel']
   
    new_usuario=Usuario(nombre,clave,nivel)
    db.session.add(new_usuario)
    db.session.commit() # confirma el alta
    return usuario_schema.jsonify(new_usuario)


@app.route('/usuarios/<id>', methods=['PUT'])
def update_usuario(id):
    usuario=Usuario.query.get(id)
    #excursion=request.json['id']
    usuario.nombre=request.json['nombre']
    usuario.clave=request.json['clave']
    usuario.nivel=request.json['nivel']
    
    db.session.commit()    # confirma el cambio
    return usuario_schema.jsonify(usuario)    # y retorna un json con el producto
 


