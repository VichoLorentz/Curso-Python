from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

def test():
    #MessageBox.showinfo("Hola!", "Hola mundo")
    #MessageBox.showwarning("Alerta!", "Seccion solo para administradores")
    #MessageBox.showerror("Error!", "Ha ocurrido un error inesperado")
    #resultado = MessageBox.askquestion("Salir", "Esta seguro que quiere salir sin guardar?")
    #if resultado == "yes":
    #    root.destroy()
    #resultado = MessageBox.askokcancel("Salir", "Sobreescribir el fichero actual?")
    #resultado = MessageBox.askyesno("Salir", "Esta seguro que quiere salir sin guardar?")
    #if resultado == True:
    #    root.destroy()
    #resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar")
    #if resultado:
    #    root.destroy()
    #color = ColorChooser.askcolor(title="Elige un color")
    #print(color)
    """ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:", 
    filetypes=(("Fichero de texto","*.txt"),
    ("Fichero de texto avanzado","*.txt2"),
    ("Todos los ficheros","*.*")))
    print(ruta)"""
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="r+", defaultextension=".txt")
    print(fichero)
    if fichero is not None:
        fichero.write("Hola")
        fichero.close() 
Button(root, text="Haz click", command=test).pack()


root.mainloop() 