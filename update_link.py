import yt_dlp
import requests
import sys
import time

# Sözcü TV Video ID (Değişirse burayı güncelle)
VIDEO_ID = "ztmY_cCtUl0"
VIDEO_URL = f"https://www.youtube.com/watch?v={VIDEO_ID}"

# Linki alacak fonksiyon
def get_stream_link():
    print(f"Hedef Video: {VIDEO_ID}")

    # YÖNTEM 1: yt-dlp (iOS İstemcisi ile - Bazen çalışır)
    print("--- Yöntem 1: yt-dlp (iOS Modu) deneniyor ---")
    try:
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'extractor_args': {
                'youtube': {
                    'player_client': ['ios', 'web_embedded'], # iOS bazen daha az takılır
                }
            }
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(VIDEO_URL, download=False)
            url = info.get('url')
            if url:
                save_m3u(url)
                return
    except Exception as e:
        print(f"Yöntem 1 Başarısız: {str(e)[:100]}...")

    # YÖNTEM 2: Invidious API (Yedek Güç - GitHub IP Engelini Aşar)
    print("--- Yöntem 2: Invidious API (Proxy) deneniyor ---")
    instances = [
        "https://inv.nadeko.net",
        "https://invidious.jing.rocks",
        "https://vid.puffyan.us",
        "https://invidious.nerdvpn.de"
    ]

    for instance in instances:
        try:
            api_url = f"{instance}/api/v1/videos/{VIDEO_ID}"
            print(f"Sunucu deneniyor: {instance}...")
            response = requests.get(api_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                # Canlı yayın linkini (hlsUrl) bul
                if 'hlsUrl' in data:
                    m3u8_url = data['hlsUrl']
                    # Linkin çalıştığından emin olmak için bazen decode gerekebilir
                    m3u8_url = m3u8_url.replace("%3A", ":").replace("%2F", "/")
                    save_m3u(m3u8_url)
                    return
        except Exception as e:
            print(f"Sunucu hatası: {e}")
            continue

    print("HATA: Hiçbir yöntemle link alınamadı.")
    sys.exit(1)

def save_m3u(stream_url):
    print(f"BAŞARILI! Link bulundu: {stream_url[:40]}...")
    content = f"#EXTM3U\n#EXTINF:-1 group-title=\"Haber\" tvg-logo=\"https://yt3.googleusercontent.com/ytc/AIdro_kX4C_A2f8hXgG_d7D_h9tX8qX8_x8_x8=s900-c-k-c0x00ffffff-no-rj\",SÖZCÜ TV Canlı Yayını ᴴᴰ\n{stream_url}"
    
    with open('sozcu.m3u', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Dosya kaydedildi.")

if __name__ == "__main__":
    get_stream_link()
