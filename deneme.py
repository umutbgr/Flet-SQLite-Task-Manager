import yt_dlp

def video_indir(url):
    ydl_opts = {
        # 'bestvideo+bestaudio' 4K için en iyi görüntü ve sesi seçer
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        # FFmpeg kullanarak birleştirme yapar
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = input("İndirmek istediğiniz video linkini girin: ")
video_indir(url)