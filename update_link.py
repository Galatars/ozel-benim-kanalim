import requests
import re
import sys
import time
import json

# Sözcü TV Video ID
VIDEO_ID = "ztmY_cCtUl0"

def get_stream_link():
    print(f"Hedef: Sözcü TV ({VIDEO_ID})")
    print("-" * 30)

    # ---------------------------------------------------------
    # YÖNTEM 1: Embed Sayfası (Manuel Kazıma) - EN GÜÇLÜ YÖNTEM
    # ---------------------------------------------------------
    print("[1/2] Embed yöntemi deneniyor...")
    
    embed_url = f"https://www.youtube.com/embed/{VIDEO_ID}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Referer": "https://www.youtube.com/",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        response = requests.get(embed_url, headers=headers, timeout=10)
        html_content = response.text

        # Regex ile hlsManifestUrl'yi arıyoruz
        match = re.search(r'"hlsManifestUrl":"(https:[^"]+)"', html_content)
        
        if match:
            # Link bulundu ama içinde \/ karakterleri var, temizleyelim
            raw_link = match.group(1)
            clean_link = raw_link.replace("\\/", "/")
            print(">>> BAŞARILI: Embed sayfasından link çekildi!")
            save_m3u(clean_link)
            return
        else:
            print("Embed sayfasında manifest bulunamadı. (IP engeli olabilir)")

    except Exception as e:
        print(f"Embed hatası: {e}")

    # ---------------------------------------------------------
    # YÖNTEM 2: Android Istemcisi (POST İsteği ile)
    # ---------------------------------------------------------
    print("\n[2/2] Android API Simülasyonu deneniyor...")
    
    # Bu yöntem yt-dlp'nin yaptığı işi manuel ve daha gizli yapar
    api_url = "https://www.youtube.com/youtubei/v1/player"
    
    payload = {
        "videoId": VIDEO_ID,
        "context": {
            "client": {
                "clientName": "ANDROID",
                "clientVersion": "17.31.35",
                "androidSdkVersion": 30,
                "userAgent": "com.google.android.youtube/17.31.35 (Linux; U; Android 11) gzip",
                "hl": "en",
                "timeZone": "UTC",
                "utcOffsetMinutes": 0
            }
        }
    }

    try:
        r = requests.post(api_url, json=payload, headers={"User-Agent": headers["User-Agent"]}, timeout=10)
        data = r.json()
        
        # JSON içinden hlsManifestUrl'yi bulmaya çalışalım
        if "streamingData" in data and "hlsManifestUrl" in data["streamingData"]:
            link = data["streamingData"]["hlsManifestUrl"]
            print(">>> BAŞARILI: Android API üzerinden link alındı!")
            save_m3u(link)
            return
        else:
            print("Android API yanıt verdi ama link içermiyor.")
            
    except Exception as e:
        print(f"Android API hatası: {e}")

    # Başarısız olursa
    print("\n!!! KRİTİK HATA: Tüm kapılar kapalı. GitHub IP'si tamamen engellenmiş. !!!")
    sys.exit(1)

def save_m3u(stream_url):
    print(f"\nDosya kaydediliyor...")
    
    # Python 3 tırnak bloğu hatasını önlemek için güvenli yazım
    line1 = "#EXTM3U"
    line2 = '#EXTINF:-1 group-title="Haber" tvg-logo="https://yt3.googleusercontent.com/ytc/APkrFKamA6E3QWjE9YwQYx9w",SÖZCÜ TV Canlı Yayını ᴴᴰ'
    
    content = f"{line1}\n{line2}\n{stream_url}"
    
    with open('sozcu.m3u', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(">>> sozcu.m3u BAŞARIYLA OLUŞTURULDU <<<")

if __name__ == "__main__":
    get_stream_link()
