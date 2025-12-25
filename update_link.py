import yt_dlp
import sys

# Sözcü TV Video ID
VIDEO_ID = "ztmY_cCtUl0"
URL = f"https://www.youtube.com/watch?v={VIDEO_ID}"

def get_stream_link():
    print("VPN Aktif. YouTube'a bağlanılıyor...")
    
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        # VPN olduğu için sadece basit bir Android taklidi yeterli
        'extractor_args': {
            'youtube': {
                'player_client': ['android'],
            }
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(URL, download=False)
            
            if 'url' in info:
                stream_url = info['url']
                print(">>> BAŞARILI: Link alındı!")
                
                content = f"#EXTM3U\n#EXTINF:-1 group-title=\"Haber\" tvg-logo=\"https://yt3.googleusercontent.com/ytc/APkrFKamA6E3QWjE9YwQYx9w\",SÖZCÜ TV Canlı Yayını ᴴᴰ\n{stream_url}"
                
                with open('sozcu.m3u', 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                print("Link bulunamadı.")
                sys.exit(1)

    except Exception as e:
        print(f"Hata: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    get_stream_link()
