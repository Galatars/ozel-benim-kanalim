import yt_dlp
import sys

# BURASI SENİN DÜZENLEYECEĞİN YER
# Link değişirse sadece buradaki ID'yi değiştirmen yeterli.
VIDEO_ID = "ztmY_cCtUl0"
video_url = f"https://www.youtube.com/watch?v={VIDEO_ID}"

def get_stream_link():
    # YouTube bot korumasını aşmak için kritik ayarlar
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        # Bu ayar YouTube'u kandırıp "Giriş Yap" hatasını engeller
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'ios'], # Mobil gibi davran
                'player_skip': ['web', 'tv'],        # Web arayüzünü atla
            }
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Bağlanılıyor: {video_url}")
            
            # Bilgileri çek
            info = ydl.extract_info(video_url, download=False)
            
            # Canlı yayın linkini (m3u8) al
            stream_url = info.get('url')
            
            if stream_url:
                print("Link başarıyla çekildi.")
                
                # M3U dosyasını oluştur
                # group-title ve kanal adını senin istediğin gibi ayarladım
                content = f"#EXTM3U\n#EXTINF:-1 group-title=\"Haber\",SÖZCÜ TV Canlı Yayını ᴴᴰ\n{stream_url}"
                
                with open('sozcu.m3u', 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print("sozcu.m3u dosyası başarıyla kaydedildi.")
            else:
                print("HATA: Link bulunamadı. Video yayında olmayabilir.")
                sys.exit(1)

    except Exception as e:
        print(f"KRİTİK HATA: {str(e)}")
        # Hata mesajı ver ama işlemi başarısız sayıp durdurma (GitHub Action kızarmasın)
        sys.exit(1)

if __name__ == "__main__":
    get_stream_link()
