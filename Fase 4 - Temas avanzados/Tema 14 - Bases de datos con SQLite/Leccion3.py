import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()  

#cursor.execute("SELECT * FROM usuarios WHERE edad = 22")

#usuario = cursor.fetchall()
#for u in usuario:
#    print(u)

#cursor.execute("UPDATE usuarios SET nombre = 'Vicente Martinez' WHERE dni='203795254'")

cursor.execute("DELETE FROM usuarios WHERE dni='203795254'")

conexion.commit()
conexion.close()