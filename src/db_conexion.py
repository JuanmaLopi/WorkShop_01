import psycopg2

def establecer_conexion():
    dbname='WorkShop_01'
    user='postgres'
    password='root'
    host='localhost'
    port='3000'

    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    print("Conexion exitosa a la base de datos")
    cursor = conn.cursor()

    return conn, cursor

establecer_conexion()