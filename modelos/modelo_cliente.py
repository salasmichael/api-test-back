from db import conexion

def obtener_registros():
    con = conexion()
    registros = []
    with con.cursor() as cursor:
        cursor.execute("SELECT * FROM clientes")
    registros = cursor.fetchall()
    con.close()

    return registros


def obtener_x_id(id):
    con = conexion()
    registros = []
    with con.cursor() as cursor:
        cursor.execute("SELECT * FROM clientes WHERE id=%s", id)
    registros = cursor.fetchone()
    con.close()
    return registros


def creacion_cliente(nombre, direccion, telefono, nacionalidad, correo):
    con = conexion()
    with con.cursor() as cursor:
        cursor.execute("INSERT INTO clientes(nombre, direccion, telefono, nacionalidad, correo) VALUES(%s, %s,%s,%s,%s)", (nombre, direccion, telefono, nacionalidad, correo))
        last_id = cursor.lastrowid
    con.commit()
    con.close()
    return last_id

def modificar_cliente(id, nombre, direccion, telefono, nacionalidad, correo):
    con = conexion()
    with con.cursor() as cursor:
        cursor.execute("UPDATE clientes SET nombre=%s, direccion=%s, telefono=%s, nacionalidad=%s, correo=%s WHERE id=%s", (nombre, direccion, telefono, nacionalidad, correo, id))
    con.commit()
    con.close()

def eliminar_cliente(id):
    con = conexion()
    with con.cursor() as cursor:
        cursor.execute("DELETE FROM clientes WHERE id=%s", id)
    con.commit()
    con.close() 