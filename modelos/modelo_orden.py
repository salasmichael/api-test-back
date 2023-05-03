from db import conexion

def obtener_registros():
    con = conexion()
    registros = []
    with con.cursor() as cursor:
        cursor.execute("SELECT o.*,c.`nombre` FROM ordenes o INNER JOIN clientes c ON o.`clienteId` = c.id")
    registros = cursor.fetchall()
    con.close()

    return registros


def obtener_x_id(id):
    con = conexion()
    registros = []
    with con.cursor() as cursor:
        cursor.execute("SELECT * FROM ordenes WHERE ordenId=%s", id)
    registros = cursor.fetchone()
    con.close()
    return registros


def creacion_orden(orden, clienteId, fechaOrden, estado):
    con = conexion()
    with con.cursor() as cursor:
        cursor.execute("INSERT INTO ordenes(orden, clienteId, fechaOrden, estado) VALUES(%s, %s,%s,%s)", (orden, clienteId, fechaOrden, estado))
        last_id = cursor.lastrowid
    con.commit()
    con.close()
    return last_id


def modificar_orden(id, orden, clienteId, fechaOrden, estado):
    con = conexion()
    with con.cursor() as cursor:
        cursor.execute("UPDATE ordenes SET orden=%s, clienteId=%s, fechaOrden=%s, estado=%s WHERE ordenId=%s", (orden, clienteId, fechaOrden, estado, id))
    con.commit()
    con.close()

def cambiar_estado_orden(id, estado):
    con = conexion()
    with con.cursor() as cursor:
        cursor.execute("UPDATE ordenes SET estado=%s WHERE ordenId=%s", (estado, id))
    con.commit()
    con.close()

def obtenerDetalleOrden_x_id(id):
    con = conexion()
    registros = []
    with con.cursor() as cursor:
        cursor.execute("SELECT nombreItem,largo,ancho FROM ordenDetalle WHERE ordenId=%s", id)
    registros = cursor.fetchall()
    con.close()
    return registros


def creacion_orden_detalle(ordenId, nombreItem,largo, ancho):
    con = conexion()
    with con.cursor() as cursor:
        cursor.execute("INSERT INTO ordenDetalle(ordenId, nombreItem, largo, ancho) VALUES(%s, %s,%s,%s)", (ordenId, nombreItem, largo, ancho))
    con.commit()
    con.close()
