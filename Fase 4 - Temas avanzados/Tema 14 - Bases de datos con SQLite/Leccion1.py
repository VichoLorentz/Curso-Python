
import sqlite3



conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor() 

#cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

#cursor.execute("INSERT INTO usuarios VALUES('Vicente',27,'vizio.auditore13@gmail.com')")
#cursor.execute("SELECT * FROM usuarios")
#usuario = cursor.fetchone()
#print(usuario[0])

#Insertar de forma masiva
"""usuarios = [
    ('Mario', 51, 'mario@ejemplo.com'),
    ('Mercedes', 38, 'mercedes@ejemplo.com'),
    ('Juan', 19, 'juan@ejemplo.com')
]

cursor.executemany("INSERT INTO usuarios VALUES(?,?,?)", usuarios)"""

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

conexion.commit()
conexion.close()