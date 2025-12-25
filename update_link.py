import requests
import sys

# Sözcü TV Video ID (İstediğin zaman değiştirebilirsin)
VIDEO_ID = "ztmY_cCtUl0"

def get_stream_link():
    print(f"Hedef Video ID: {VIDEO_ID}")
    
    # 1. YÖNTEM: Piped API (En sağlam yöntem)
    # Bu API'ler YouTube engellerini kendi sunucularında aşar.
    piped_instances = [
        "https://pipedapi.kavin.rocks",
        "https://api.piped.privacydev.net",
        "https://pipedapi.smnz.de",
        "https://api.piped.drg.li"
    ]

    print("--- Yöntem 1: Piped API deneniyor ---")
    for base_url in piped_instances:
        try:
            url = f"{base_url}/streams/{VIDEO_ID}"
            print(f"Sunucuya soruluyor: {base_url}...")
            
            # Timeout süresini kısa tutuyoruz ki hızlı geçsin
            r = requests.get(url, timeout=5)
            
            if r.status_code == 200:
                data = r.json()
                # HLS linkini (canlı yayın akışı) bulalım
                if "hls" in data and data["hls"]:
                    m3u8_url = data["hls"]
                    print(f"Link Piped üzerinden bulundu!")
                    save_m3u(m3u8_url)
                    return
        except Exception as e:
            print(f"Sunucu pas geçildi: {e}")
            continue

    # 2. YÖNTEM: Invidious API (Yedek)
    # Daha taze ve çalışan sunucu listesi
    invidious_instances = [
        "https://inv.bp.projectsegfau.lt",
        "https://invidious.fdn.fr",
        "https://inv.tux.pizza",
        "https://invidious.flokinet.to"
    ]

    print("\n--- Yöntem 2: Invidious API deneniyor ---")
    for base_url in invidious_instances:
        try:
            url = f"{base_url}/api/v1/videos/{VIDEO_ID}"
            print(f"Sunucuya soruluyor: {base_url}...")
            
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                data = r.json()
                if "hlsUrl" in data:
                    m3u8_url = data["hlsUrl"]
                    # Linki düzelt (bazen encoded gelir)
                    m3u8_url = m3u8_url.replace("%3A", ":").replace("%2F", "/")
                    print(f"Link Invidious üzerinden bulundu!")
                    save_m3u(m3u8_url)
                    return
        except Exception as e:
            print(f"Sunucu hatası: {e}")
            continue

    print("\nKRİTİK HATA: Tüm sunucular denendi ama link alınamadı.")
    sys.exit(1)

def save_m3u(stream_url):
    print(f"KAYDEDİLİYOR: {stream_url[:50]}...")
    
    # M3U dosya içeriği
    content = f"#EXTM3U\n#EXTINF:-1 group-title=\"Haber\" tvg-logo=\"https://yt3.googleusercontent.com/ytc/AIdro_kX4C_A43gq_LqWfQ_oQ_oQ=s0\",SÖZCÜ TV Canlı Yayını ᴴᴰ\n{stream_url}"
    
    with open('sozcu.m3u', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("sozcu.m3u dosyası başarıyla oluşturuldu.")

if __name__ == "__main__":
    get_stream_link()
