from flask import Flask, request, jsonify
from modelos import modelo_cliente, modelo_orden

app = Flask(__name__)

###############################
# Enpoints Clientes 
##############################

# Enpoint Creacion de clientes
@app.route("/cliente", methods=["POST"])
def agregar_cliente():
    nombre       = request.json['nombre']
    direccion    = request.json['direccion']
    telefono     = request.json['telefono']
    nacionalidad = request.json['nacionalidad']
    correo       = request.json['correo']

    cliente_id =  modelo_cliente.creacion_cliente(nombre, direccion, telefono, nacionalidad, correo)

    if(cliente_id):
        Cliente_dict = { "mensaje"  :  "Cliente creado con exito!" }
    else:
        Cliente_dict = { "error"  :  "Error al crear cliente!" }

    return jsonify(Cliente_dict)


# Enpoint Muestra todos los clientes
@app.route("/clientes", methods=["GET"])
def cargar_clientes():
    resultados = []
    result = modelo_cliente.obtener_registros()
    
    claves = ['id', 'nombre','direccion','telefono','nacionalidad','correo']
    for objetos in result:
        list2dic = dict(zip(claves, objetos))
        resultados.append(list2dic)


    return jsonify({"data":resultados})


# Enpoint Muestra Detalle de los clientes por ID
@app.route("/cliente/<id>", methods=["GET"])
def cargar_cliente_x_id(id):
    result = modelo_cliente.obtener_x_id(id)
    claves = ['id', 'nombre','direccion','telefono','nacionalidad','correo']
    lista2dic = dict(zip(claves, result))

    return lista2dic



# Enpoint Modifica cliente por ID
@app.route("/cliente/<id>", methods=["PUT"])
def actualizar_cliente(id):
    nombre       = request.json['nombre']
    direccion    = request.json['direccion']
    telefono     = request.json['telefono']
    nacionalidad = request.json['nacionalidad']
    correo       = request.json['correo']

    modelo_cliente.modificar_cliente(id, nombre, direccion, telefono, nacionalidad, correo)

    Cliente_dict = {
            "nombre"       : nombre,
            "direccion"    : direccion,
            "telefono"     : telefono,
            "nacionalidad" : nacionalidad,
            "correo"       : correo
        }

    return jsonify(Cliente_dict)



# Enpoint Elimina cliente
@app.route("/cliente/<id>", methods=["DELETE"])
def eliminar_cliente(id):
    modelo_cliente.eliminar_cliente(id)
    Cliente_dict = {'mensaje':'Cliente elimnado con exito!'}

    return jsonify(Cliente_dict)


###############################
# Enpoints para las ordenes 
##############################

# crear Ordenes 
@app.route("/orden", methods=["POST"])
def agregar_orden():
    orden        = request.json['orden']
    clienteId    = request.json['clienteId']
    fechaOrden   = request.json['fechaOrden']
    estado       = request.json['estado']
    items        = request.json['items']

    orden_id = modelo_orden.creacion_orden(orden, clienteId, fechaOrden, estado)

    if (orden_id):
        
        for item in items:
             modelo_orden.creacion_orden_detalle(orden_id, item["nombreItem"], item["largo"], item["ancho"])

        Orden_dict = { "mensaje"  :  "Orden guardada con exito!" }
    else:
        Orden_dict = { "error"  :  "Error al intentar guardar la orden" }

    return jsonify(Orden_dict)


# Listar ordenes 
@app.route("/ordenes", methods=["GET"])
def cargar_ordenes():
    resultados = []
    detalles   = []
    orden      = {}
    claves     = ['nombreItem', 'largo','ancho']
    
    result = modelo_orden.obtener_registros()
   
    
    for row in result:

        orden['orden'] = row[1]
        orden['cliente'] = row[5]
        orden['fechaOrden'] = row[3].strftime('%d/%m/%Y')
        orden['estado'] = row[4]
      
        resultadoDetalle = modelo_orden.obtenerDetalleOrden_x_id(row[0])

        if len(resultadoDetalle) > 0:
            detalles   = []
            for objetos in resultadoDetalle:
                list2dic = dict(zip(claves, objetos))
                detalles.append(list2dic)
            
        orden['items'] = detalles

        list2dic = dict(orden)
        resultados.append(list2dic)
        
    return jsonify({"data":resultados})



# Actualizar orden
@app.route("/orden/<id>", methods=["PUT"])
def actualizar_orden(id):
    orden        = request.json['orden']
    clienteId    = request.json['clienteId']
    fechaOrden   = request.json['fechaOrden']
    estado       = request.json['estado']

    modelo_orden.modificar_orden(id, orden, clienteId, fechaOrden, estado)

    Orden_dict = {
        "orden"  : orden,
        "clienteId"    : clienteId,
        "fechaOrden"   : fechaOrden,
        "estado"       : estado
    }

    return jsonify(Orden_dict)


# Cambiar estado de la orden
@app.route("/orden-estado/<id>", methods=["PUT"])
def actualizar_estado_orden(id):
   
    estado  = request.json['estado']

    modelo_orden.cambiar_estado_orden(id, estado)

    Orden_dict = {
        "mensaje"   : "Su orden paso a estado: " + estado
    }

    return jsonify(Orden_dict)



if __name__ == '__main__':
    with app.app_context():
        app.run(host="localhost", port="5000", debug=True)
