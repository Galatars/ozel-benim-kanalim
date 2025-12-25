import requests
import yt_dlp
import sys
import time

# Sözcü TV Video ID
VIDEO_ID = "ztmY_cCtUl0"

def get_stream_link():
    print(f"Hedef: Sözcü TV ({VIDEO_ID})")
    print("-" * 30)

    # ---------------------------------------------------------
    # YÖNTEM 1: yt-dlp (Android VR Modu)
    # ---------------------------------------------------------
    print("[1/3] yt-dlp (Android VR Modu) deneniyor...")
    try:
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'extractor_args': {
                'youtube': {
                    'player_client': ['android_vr'],
                    'player_skip': ['web', 'tv'],
                }
            }
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            url = f"https://www.youtube.com/watch?v={VIDEO_ID}"
            info = ydl.extract_info(url, download=False)
            if 'url' in info:
                print(">>> BAŞARILI: yt-dlp linki kaptı!")
                save_m3u(info['url'])
                return
    except Exception as e:
        print(f"yt-dlp başarısız oldu: {str(e)[:50]}...")

    # ---------------------------------------------------------
    # YÖNTEM 2: API Ordusu (Piped & Invidious)
    # ---------------------------------------------------------
    print("\n[2/3] API Ordusu devreye giriyor...")
    
    instances = [
        # En Güçlüler
        f"https://pipedapi.kavin.rocks/streams/{VIDEO_ID}",
        f"https://yewtu.be/api/v1/videos/{VIDEO_ID}",
        f"https://vid.puffyan.us/api/v1/videos/{VIDEO_ID}",
        # Yedekler
        f"https://api.piped.io/streams/{VIDEO_ID}",
        f"https://pipedapi.smnz.de/streams/{VIDEO_ID}",
        f"https://inv.nadeko.net/api/v1/videos/{VIDEO_ID}",
        f"https://invidious.jing.rocks/api/v1/videos/{VIDEO_ID}",
        f"https://invidious.nerdvpn.de/api/v1/videos/{VIDEO_ID}",
        f"https://inv.tux.pizza/api/v1/videos/{VIDEO_ID}",
        f"https://invidious.fdn.fr/api/v1/videos/{VIDEO_ID}",
    ]

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

    for api_url in instances:
        try:
            domain = api_url.split("/")[2]
            print(f"Denenen sunucu: {domain} ...", end=" ")
            
            r = session.get(api_url, timeout=5)
            
            if r.status_code == 200:
                data = r.json()
                
                # Piped formatı
                if "hls" in data and data["hls"]:
                    print("TUTTU! (Piped)")
                    save_m3u(data["hls"])
                    return
                
                # Invidious formatı
                if "hlsUrl" in data and data["hlsUrl"]:
                    print("TUTTU! (Invidious)")
                    clean_url = data["hlsUrl"].replace("%3A", ":").replace("%2F", "/")
                    save_m3u(clean_url)
                    return
                print("Link yok.")
            else:
                print(f"Hata: {r.status_code}")
                
        except Exception:
            print("Erişilemedi.")
            continue

    print("\n!!! KRİTİK HATA: Hiçbir sunucudan yanıt alınamadı. !!!")
    sys.exit(1)

def save_m3u(stream_url):
    print(f"\nDosya kaydediliyor...")
    
    # HATA DÜZELTİLDİ: Tek tırnak kullanarak karışıklığı önledik
    m3u_content = f'''#EXTM3U
#EXTINF:-1 group-title="Haber" tvg-logo="https://yt3.googleusercontent.com/ytc/APkrFKamA6E3QWjE9YwQYx9w",SÖZCÜ TV Canlı Yayını ᴴᴰ
{stream_url}'''
    
    with open('sozcu.m3u', 'w', encoding='utf-8') as f:
        f.write(m3u_content)
    
    print(">>> sozcu.m3u BAŞARIYLA OLUŞTURULDU <<<")

if __name__ == "__main__":
    get_stream_link()
