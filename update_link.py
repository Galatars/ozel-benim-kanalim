import yt_dlp
import sys

# Sözcü TV Canlı Yayın ID'si
video_id = "ztmY_cCtUl0"
video_url = f'https://www.youtube.com/watch?v={video_id}'

# YouTube engeline takılmamak için en hafif formatı (m3u8) istiyoruz
ydl_opts = {
    'quiet': True,
    'no_warnings': True,
    'format': 'best[ext=mp4]/best', # En uyumlu format
    'force_generic_extractor': False,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # YouTube'dan m3u8 linkini çek
        info = ydl.extract_info(video_url, download=False)
        
        # Eğer canlı yayınsa manifest_url kullanılır
        m3u8_url = info.get('manifest_url') or info.get('url')
        
        if m3u8_url:
            # VLC ve IPTV için standart M3U formatı
            content = f"#EXTM3U\n#EXTINF:-1,Sozcu TV\n{m3u8_url}"
            with open('sozcu.m3u', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Basarili: Orijinal m3u8 linki kaydedildi.")
        else:
            print("Link bulunamadi.")
            sys.exit(1)
except Exception as e:
    print(f"Hata: {e}")
    sys.exit(1)
