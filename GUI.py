from tkinter import *
from tkinter import ttk
import time
Ventana = None
entry_url = None
lbl_estado = None
btn_descargar = None
lbl_url = None
resoluciones = None
opc_res = None
estado = None
def crear_gui(boton):
    global Ventana, entry_url, lbl_estado,btn_descargar, lbl_url,opc_res,resoluciones,estado 
    Ventana = Tk()
    Ventana.title("Descargador de youtube")

    lbl_url = Label(Ventana,text="Escribe la url del video a descargar")
    lbl_url.pack(pady=5)
    #Seccion para introducir el url a descargar
    entry_url = Entry(Ventana,width=30)
    entry_url.pack(pady=5)

    #seccion encargada de mostrar la lista de opciones del video
    resoluciones = ("Mejor disponible","2160p","1080p",
                    "720p","480p","360p","240p")
    opc_res = ttk.Combobox(Ventana,values=resoluciones,state="readonly")
    opc_res.pack(pady=5)

    estado = ttk.Progressbar(Ventana,orient=HORIZONTAL,length=250)
    estado.pack(pady=8)


    btn_descargar = Button(Ventana,text="Descargar Video/Audio",command=boton)
    btn_descargar.pack(pady=8)
    return Ventana