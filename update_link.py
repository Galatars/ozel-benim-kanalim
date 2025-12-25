import yt_dlp
import sys

# Sözcü TV Canlı Yayın URL'si (Video ID yerine bunu kullanmak daha garantidir)
channel_url = "https://www.youtube.com/@SozcuTV/live"

def get_stream_link():
    ydl_opts = {
        'format': 'best',      # En iyi kaliteyi seç
        'quiet': True,         # Gereksiz çıktı verme
        'no_warnings': True,
        'extract_flat': False, # Derinlemesine tarama yap
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Link bilgilerini çek
            info = ydl.extract_info(channel_url, download=False)
            
            # Canlı yayın akış linkini (m3u8) al
            stream_url = info.get('url')
            
            if stream_url:
                print(f"Link bulundu: {stream_url[:50]}...")
                
                # M3U dosyasını oluştur
                content = f"#EXTM3U\n#EXTINF:-1,Sozcu TV\n{stream_url}"
                
                with open('sozcu.m3u', 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print("sozcu.m3u dosyası başarıyla güncellendi.")
            else:
                print("HATA: Akış linki bulunamadı.")
                sys.exit(1)

    except Exception as e:
        print(f"Kritik Hata: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    get_stream_link()
