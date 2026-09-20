from tkinter import *
from tkinter import ttk
import sv_ttk


class Interfaz(Tk):

    def __init__(self, callback_boton):
        super().__init__()

        self.title("Descargador de YouTube")
        self.geometry("400x320")

        # Aplicar el tema Sun Valley
        sv_ttk.set_theme("light")

        # Configurar centrado en la ventana principal
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Marco contenedor
        marco = ttk.LabelFrame(
            self, text=" Descargar Video ", padding=(20, 15)
        )
        marco.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Etiqueta e Input URL
        self.lbl_url = ttk.Label(
            marco, text="Escribe la URL del video a descargar:"
        )
        self.lbl_url.pack(pady=5)

        self.entry_url = ttk.Entry(marco, width=32)
        self.entry_url.pack(pady=5)

        # Selector de Resoluciones
        resoluciones = (
            "Mejor disponible",
            "2160p",
            "1080p",
            "720p",
            "480p",
            "360p",
            "240p",
        )
        self.opc_res = ttk.Combobox(
            marco, values=resoluciones, state="readonly"
        )
        self.opc_res.current(0)
        self.opc_res.pack(pady=5)

        # Barra de progreso
        self.estado = ttk.Progressbar(marco, orient=HORIZONTAL, length=250)
        self.estado.pack(pady=8)

        # Mensaje de finalización (inicialmente oculto)
        self.lbl_estado = ttk.Label(marco, text="Descarga completa")

        # Botón de descarga
        self.btn_descargar = ttk.Button(
            marco, text="Descargar Video/Audio", command=callback_boton
        )
        self.btn_descargar.pack(pady=8)