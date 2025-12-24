import yt_dlp

# YouTube Canlı Yayın URL'si
video_url = 'https://www.youtube.com/watch?v=ztmY_cCtUl0'

# Linki çekmek için ayarlar
ydl_opts = {
    'quiet': True,
    'no_warnings': True,
    'format': 'best'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        info = ydl.extract_info(video_url, download=False)
        m3u8_url = info['url']
        
        # M3U dosyası içeriği
        m3u_content = f"#EXTM3U\n#EXTINF:-1,Sozcu TV\n{m3u8_url}"
        
        with open('sozcu.m3u', 'w') as f:
            f.write(m3u_content)
        print("Link başarıyla güncellendi.")
    except Exception as e:
        print(f"Hata oluştu: {e}")
