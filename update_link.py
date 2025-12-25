import yt_dlp
import sys

# Sözcü TV Kanal ID'li Canlı Yayın Linki
channel_url = "https://www.youtube.com/watch?v=ztmY_cCtUl0"

def get_stream_link():
    # YouTube bot korumasını aşmak için özel ayarlar
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        # KRİTİK AYAR: Kendimizi Android uygulaması gibi gösteriyoruz
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'ios'],
                'player_skip': ['web', 'tv']
            }
        },
        # Ekstra başlıklar ile gerçekçi tarayıcı taklidi
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Bağlanılıyor: {channel_url}")
            
            # Bilgileri çek
            info = ydl.extract_info(channel_url, download=False)
            
            # Canlı yayın linkini al
            stream_url = info.get('url')
            
            if stream_url:
                print("Link başarıyla alındı.")
                
                # M3U içeriğini oluştur
                content = f"#EXTM3U\n#EXTINF:-1 group-title=\"Haber\",SÖZCÜ TV Canlı Yayını ᴴᴰ\n{stream_url}"
                
                with open('sozcu.m3u', 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print("sozcu.m3u dosyası kaydedildi.")
            else:
                print("HATA: Link alınamadı.")
                sys.exit(1)

    except Exception as e:
        print(f"KRİTİK HATA: {str(e)}")
        # Hata olsa bile action'ı durdurma, bir sonraki denemeyi bekle
        sys.exit(1)

if __name__ == "__main__":
    get_stream_link()
