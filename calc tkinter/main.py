import threading
from tkinter import *
import GUI
import descargas


def boton():
    url_user = GUI.entry_url.get()
    res_user = GUI.opc_res.get()

    # Validación básica para no lanzar descargas con la URL vacía
    if not url_user:
        return

    # Crear e iniciar el hilo secundario
    hilo = threading.Thread(
        target=descargas.descargar_video,
        args=(url_user, res_user),
        daemon=True,
    )
    hilo.start()


def main():
    app = GUI.crear_gui(boton)
    app.mainloop()


if __name__ == "__main__":
    main()