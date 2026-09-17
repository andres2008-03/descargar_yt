import yt_dlp
from GUI import resoluciones

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
def descargar_video(url,calidad):
    ydl_opts = {
        "format" : limpiar_res(calidad),
        "outtmpl" : "%(title)s.%(ext)s",
        "quiet" : True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])