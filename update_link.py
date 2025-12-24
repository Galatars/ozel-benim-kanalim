import yt_dlp
import os

# Sözcü TV güncel canlı yayın URL'si
video_url = 'https://www.youtube.com/watch?v=ztmY_cCtUl0'

ydl_opts = {
    'quiet': True,
    'no_warnings': True,
    'format': 'best',
    'nocheckcertificate': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        # Linki al
        info = ydl.extract_info(video_url, download=False)
        m3u8_url = info['url']
        
        # Dosyayı oluştur
        with open('sozcu.m3u', 'w', encoding='utf-8') as f:
            f.write(f"#EXTM3U\n#EXTINF:-1,Sozcu TV\n{m3u8_url}")
        
        print("Dosya basariyla olusturuldu.")
    except Exception as e:
        print(f"Hata: {e}")
        # Hata olsa bile bos dosya olusmasin diye islemi durdur
        exit(1)
