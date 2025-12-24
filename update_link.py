import yt_dlp
import sys

# Sözcü TV Canlı Yayın URL'si
video_url = 'https://www.youtube.com/watch?v=ztmY_cCtUl0'

# YouTube'un engellemesini aşmak için eklenen ayarlar
ydl_opts = {
    'quiet': True,
    'no_warnings': True,
    'format': 'best',
    'noprogress': True,
    'extract_flat': False,
    # YouTube'un bot algılamasını zorlaştıran headerlar
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
    }
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        m3u8_url = info.get('url')
        
        if m3u8_url:
            content = f"#EXTM3U\n#EXTINF:-1,Sozcu TV\n{m3u8_url}"
            with open('sozcu.m3u', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Basarili: sozcu.m3u dosyasi guncellendi.")
        else:
            print("Hata: m3u8 linki ayiklanamadi.")
            sys.exit(1)
except Exception as e:
    print(f"Hata olustu: {e}")
    sys.exit(1)
