import yt_dlp
import sys
import time
import random

# Sözcü TV'nin sabit kanal canlı yayın linki (Asla değişmez)
channel_url = "https://www.youtube.com/watch?v=ztmY_cCtUl0"

def get_stream_link():
    # Bot korumasını aşmak için kritik ayarlar
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        # Bu ayar YouTube'a "Ben Android Uygulamasıyım" der.
        # Mobil uygulamalarda bot kontrolü daha azdır.
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'ios'],
                'player_skip': ['webpage', 'configs', 'js'], 
            }
        },
        # Ekstra güvenlik önlemleri
        'nocheckcertificate': True,
        'ignoreerrors': True,
        'logtostderr': False,
    }

    try:
        # Hızlı istekleri engellemek için rastgele kısa bir bekleme (opsiyonel)
        time.sleep(random.uniform(1, 3))
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Bağlanılıyor (Mobil İstemci Modu): {channel_url}")
            
            # Bilgileri çek
            info = ydl.extract_info(channel_url, download=False)
            
            # Eğer info None dönerse (hata varsa)
            if not info:
                print("HATA: Bilgi çekilemedi.")
                sys.exit(1)

            # Linki al
            stream_url = info.get('url')
            
            if stream_url:
                print("Link başarıyla alındı.")
                
                content = f"#EXTM3U\n#EXTINF:-1 group-title=\"Haber\",SÖZCÜ TV Canlı Yayını ᴴᴰ\n{stream_url}"
                
                with open('sozcu.m3u', 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print("sozcu.m3u dosyası güncellendi.")
            else:
                print("HATA: Canlı yayın linki bulunamadı.")
                sys.exit(1)

    except Exception as e:
        print(f"KRİTİK HATA AŞILAMADI: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    get_stream_link()
