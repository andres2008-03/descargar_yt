import threading
from tkinter import *
import GUI
import descargas
import queue

cola_progreso = queue.Queue()


def monitorear_cola():
    """Esta función corre EXCLUSIVAMENTE en el hilo principal de Tkinter."""
    try:
        while True:
            # Revisa la cola sin bloquear la interfaz
            mensaje, dato = cola_progreso.get_nowait()
            
           # 1. ACTUALIZAR LA BARRA CON EL PORCENTAJE
            if mensaje == "PROGRESS":
                GUI.estado["value"] = dato  # 'dato' es el flotante (ej. 45.2)

            elif mensaje == "FIN":
                GUI.estado["value"] = 100  # Llenar la barra al completar

            elif mensaje == "ERROR":
                GUI.estado["value"] = 0  # Reiniciar si falla

            cola_progreso.task_done()
    except queue.Empty:
        pass
    finally:
        # Programa la siguiente revisión cada 100 milisegundos en el hilo principal
        GUI.Ventana.after(100, monitorear_cola)


def boton():
    url_user = GUI.entry_url.get()
    res_user = GUI.opc_res.get()

    # Validación básica para no lanzar descargas con la URL vacía
    if not url_user:
        return

    # Crear e iniciar el hilo secundario
    hilo = threading.Thread(
        target=descargas.descargar_video,
        args=(url_user, res_user, cola_progreso),
        daemon=True,
    )
    hilo.start()


def main():
    app = GUI.crear_gui(boton)

    
    app.after(100,monitorear_cola())
    app.mainloop()

if __name__ == "__main__":
    main()