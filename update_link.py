import yt_dlp
import sys

# Sözcü TV'nin asla değişmeyen "Kanal ID"li canlı yayın linki
# Bu link her zaman o anki canlı yayına yönlendirir.
channel_url = "https://www.youtube.com/watch?v=ztmY_cCtUl0"

def get_stream_link():
    # yt-dlp ayarları
    ydl_opts = {
        'format': 'best',       # En iyi kaliteyi seç
        'quiet': True,          # Gereksiz yazıları gizle
        'no_warnings': True,
        'force_generic_extractor': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Bağlanılıyor: {channel_url}")
            
            # YouTube'dan canlı yayın bilgisini çek
            info = ydl.extract_info(channel_url, download=False)
            
            # Canlı yayın akış linkini (m3u8) al
            stream_url = info.get('url')
            
            if stream_url:
                print("Link başarıyla alındı.")
                
                # M3U dosyasını oluştur (İstediğin isimle)
                # group-title="Haber" ekledim, oynatıcılarda kategorili görünür.
                content = f"#EXTM3U\n#EXTINF:-1 group-title=\"Haber\",SÖZCÜ TV Canlı Yayını ᴴᴰ\n{stream_url}"
                
                with open('sozcu.m3u', 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print("sozcu.m3u dosyası güncellendi.")
            else:
                print("HATA: Link bulunamadı (Yayın kapalı olabilir).")
                sys.exit(1)

    except Exception as e:
        print(f"KRİTİK HATA: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    get_stream_link()
