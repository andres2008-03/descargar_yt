import yt_dlp

def limpiar_res(calidad):
    if calidad == "2160p":
        formato = "bestvideo[height<=2160]+bestaudio/best"
    elif calidad == "1080p":
        formato = "bestvideo[height<=1080]+bestaudio/best"
    elif calidad == "720p":
        formato = "bestvideo[height<=720]+bestaudio/best"
    elif calidad == "480p":
        formato = "bestvideo[height<=480]+bestaudio/best"
    elif calidad == "360p":
        formato = "bestvideo[height<=360]+bestaudio/best"
    else:
        formato = "best"
    return formato

def progress_hook(d, cola):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
        downloaded = d.get('downloaded_bytes', 0)
        percent = (downloaded / total * 100) if total > 0 else 0
        cola.put(("PROGRESS", percent))
def descargar_video(url,calidad,cola):
    try:
        ydl_opts = {
            "format" : limpiar_res(calidad),
            "outtmpl" : "%(title)s.%(ext)s",
            "merge_output_format": "mp4",
            "progress_hooks": [lambda d: progress_hook(d, cola)],
            "quiet" : True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            cola.put(("FIN", None))
    except Exception as e:
        cola.put(("ERROR", str(e)))
