import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os



class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Programador  BK MYsql")
        nombrearch= "D:/usuarios/alumno/documentos/7mo3ra/PDISC_2022/Trabajo final/config.txt"
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
           
        self.agregar_menu()
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=80, height=20)
        self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)
        self.scrolledtext1.delete("1.0", tk.END) 
        self.scrolledtext1.insert("1.0", contenido)
        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar BK", command=self.guardar)
        opciones1.add_command(label="Recuperar BK", command=self.recuperar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Backups", menu=opciones1)  

    def salir(self):
        sys.exit()

    def guardar(self):
        nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("ini files","*.ini"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def recuperar(self):
        nombrearch=fd.askopenfilename(initialdir = "D:/usuarios/alumno/documentos/7mo3ra/PDISC_2022/Trabajo final/config.txt",title = "Seleccione archivo",filetypes = (("ini files","config.ini"),("todos los archivos","*.*")))
        if nombrearch!='config.ini':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)

aplicacion1=Aplicacion() 