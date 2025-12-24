import requests
import re
import sys

# Sözcü TV Video ID
video_id = "ztmY_cCtUl0"
url = f"https://www.youtube.com/embed/{video_id}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}

try:
    response = requests.get(url, headers=headers)
    html = response.text
    
    # hlsManifestUrl'yi bulmak için regex kullanıyoruz
    match = re.search(r'"hlsManifestUrl":"(https:[^"]+)"', html)
    
    if match:
        m3u8_url = match.group(1).replace("\\/", "/")
        content = f"#EXTM3U\n#EXTINF:-1,Sozcu TV\n{m3u8_url}"
        
        with open('sozcu.m3u', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Basarili: Orijinal YouTube m3u8 linki bulundu.")
    else:
        print("HATA: m3u8 linki sayfa icinde bulunamadi. YouTube botu engellemis olabilir.")
        sys.exit(1)

except Exception as e:
    print(f"Sistemsel Hata: {e}")
    sys.exit(1)
