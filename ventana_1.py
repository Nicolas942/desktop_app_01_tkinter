# importar la libreria tkinter con todas sus funciones 

from tkinter import *

#-------------------------
#Funciones de la app
#-------------------------




#-----------------------------
#Ventana principal de la app
#-----------------------------


# Se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto de tipo Tk()

ventana_principal = Tk()

#Titulo de la ventana
ventana_principal.title("Nicolas Alfonso Cabrera Suarez")

#tamaño de la ventana 
ventana_principal.geometry("800x500")

# Metodo principal que despliega la ventana en pantalla 

ventana_principal.mainloop()