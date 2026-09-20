import queue
import threading
from tkinter import *
import descargas
from GUI import Interfaz

cola_progreso = queue.Queue()
app = None  # Instancia global de la interfaz


def monitorear_cola():
    """Esta función corre EXCLUSIVAMENTE en el hilo principal de Tkinter."""
    try:
        while True:
            mensaje, dato = cola_progreso.get_nowait()

            if mensaje == "PROGRESS":
                app.estado["value"] = dato

            elif mensaje == "FIN":
                app.estado["value"] = 100
                app.lbl_estado.pack(pady=5)  # Muestra el label al terminar

            elif mensaje == "ERROR":
                app.estado["value"] = 0

            cola_progreso.task_done()
    except queue.Empty:
        pass
    finally:
        app.after(100, monitorear_cola)


def boton():
    url_user = app.entry_url.get()
    res_user = app.opc_res.get()

    if not url_user:
        return

    # Ocultar el mensaje anterior y reiniciar la barra si se hace otra descarga
    app.lbl_estado.pack_forget()
    app.estado["value"] = 0

    hilo = threading.Thread(
        target=descargas.descargar_video,
        args=(url_user, res_user, cola_progreso),
        daemon=True,
    )
    hilo.start()


def main():
    global app
    app = Interfaz(boton)
    app.after(100, monitorear_cola)
    app.mainloop()


if __name__ == "__main__":
    main()