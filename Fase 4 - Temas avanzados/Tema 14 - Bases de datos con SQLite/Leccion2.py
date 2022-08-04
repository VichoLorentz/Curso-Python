import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute('''
create table usuarios (
    dni VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    email VARCHAR(100)
    )
    ''')

usuarios = [
    ('203795254','Vicente', 22, 'vizio.auditore13@gmail.com'),
    ('11111111A','Mario', 51, 'mario@ejemplo.com'),
    ('22222222B','Mercedes', 38, 'mercedes@ejemplo.com'),
    ('33333333C','Juan', 19, 'juan@ejemplo.com')
]

cursor.executemany("INSERT INTO usuarios VALUES(?,?,?,?)", usuarios)


conexion.commit()   
conexion.close()    