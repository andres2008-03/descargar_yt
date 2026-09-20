import queue
import threading
from tkinter import *
import descargas
from GUI import Interfaz

# Cola para conectar el hilo de descarga con la interfaz principal
cola_progreso = queue.Queue()
app = None  # Instancia global de la interfaz


def monitorear_cola():
    """Monitorea la cola de mensajes en el hilo principal de Tkinter."""
    try:
        while True:
            mensaje, dato = cola_progreso.get_nowait()

            if mensaje == "PROGRESS":
                app.estado["value"] = dato

            elif mensaje == "FIN":
                app.estado["value"] = 100
                app.lbl_estado.pack(
                    pady=5
                )  # Muestra el mensaje de completado

            elif mensaje == "ERROR":
                app.estado["value"] = 0

            cola_progreso.task_done()
    except queue.Empty:
        pass
    finally:
        # Revisa la cola cada 100ms
        app.after(100, monitorear_cola)


def boton():
    """Función que se ejecuta al presionar el botón de descarga."""
    url_user = app.entry_url.get()
    res_user = app.opc_res.get()

    if not url_user:
        return

    # Oculta el mensaje anterior y reinicia la barra si se hace otra descarga
    app.lbl_estado.pack_forget()
    app.estado["value"] = 0

    # Inicia el hilo secundario para no congelar la GUI
    hilo = threading.Thread(
        target=descargas.descargar_video,
        args=(url_user, res_user, cola_progreso),
        daemon=True,
    )
    hilo.start()


def main():
    global app
    # Instancia la nueva clase de la GUI pasando el callback
    app = Interfaz(boton)

    # Inicia el monitoreo de la cola
    app.after(100, monitorear_cola)

    # Inicia el bucle principal
    app.mainloop()


if __name__ == "__main__":
    main()