import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad INTEGER,
        emial varchar(100)
    )
    ''')

usuarios = [
    ('203795254','Vicente', 22, 'vizio.auditore13@gmail.com'),
    ('11111111A','Mario', 51, 'mario@ejemplo.com'),
    ('22222222B','Mercedes', 38, 'mercedes@ejemplo.com'),
    ('33333333C','Juan', 19, 'juan@ejemplo.com')
]

cursor.executemany("INSERT INTO usuarios VALUES(null, ?,?,?,?)", usuarios)
conexion.commit()   
conexion.close()


