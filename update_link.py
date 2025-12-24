import requests
import sys

# Sözcü TV Video ID'si
video_id = "ztmY_cCtUl0"

# Bu servis YouTube linkini otomatik olarak m3u8 formatına çevirir
proxy_url = f"https://youtube-m3u8-nu.vercel.app/api/live?url=https://www.youtube.com/watch?v={video_id}"

try:
    # M3U dosyası içeriği (Proxy linkini içine yazıyoruz)
    content = f"#EXTM3U\n#EXTINF:-1,Sozcu TV\n{proxy_url}"
    
    with open('sozcu.m3u', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Proxy linki basariyla sozcu.m3u dosyasina yazildi.")
except Exception as e:
    print(f"Hata olustu: {e}")
    sys.exit(1)
