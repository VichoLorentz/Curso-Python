'''from tkinter import *

root = Tk()

frame = Frame(root, width=480, height=320)
frame.pack()

label = Label(frame, text="Hola mundo")
label.place(x=0, y=0)
root.mainloop()'''

from tkinter import *

# Configuración de la raíz
root = Tk()


'''# Variables dinámicas
texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text="¡Hola mundo!").pack(anchor="nw")
label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor="center")
Label(root, text="¡Última etiqueta!").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable=texto)
'''

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")
root.mainloop()

