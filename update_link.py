import yt_dlp
import sys

# KANAL LISTESI
# Buraya istediğin kadar kanal ekleyebilirsin.
# Format: "Kanal Adı": "Youtube Kanal Linki"
CHANNELS = [
    {
        "name": "Sözcü TV",
        "url": "https://www.youtube.com/@SozcuTV/live",
        "group": "Haber"
    },
    {
        "name": "CNBC-e",
        "url": "https://www.youtube.com/@cnbce/live",
        "group": "Ekonomi"
    },
    {
        "name": "NOW TV (FOX)",
        "url": "https://www.youtube.com/@NOWturkiye/live",
        "group": "Ulusal"
    },
    {
        "name": "Habertürk",
        "url": "https://www.youtube.com/@HaberturkTV/live",
        "group": "Haber"
    },
    {
        "name": "Teve2", # Tele 2 dediğin için Teve2 ekledim
        "url": "https://www.youtube.com/@teve2/live",
        "group": "Eglence"
    },
    # Eğer TELE1 istiyorsan üstteki Teve2'yi silip bunu açabilirsin:
    # {"name": "Tele1", "url": "https://www.youtube.com/@tele1comtr/live", "group": "Haber"},
    
    {
        "name": "Cartoon Network",
        "url": "https://www.youtube.com/@CartoonNetworkTurkiye/live",
        "group": "Cocuk"
    },
    {
        "name": "SpaceToon",
        "url": "https://www.youtube.com/@spacetoon/live",
        "group": "Cocuk"
    }
]

def get_stream_link(channel_info):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'extractor_args': {
            'youtube': {
                'player_client': ['android'], # WARP olduğu için Android taklidi yeterli
            }
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Taranıyor: {channel_info['name']}...")
            info = ydl.extract_info(channel_info['url'], download=False)
            
            if 'url' in info:
                return info['url']
            else:
                return None

    except Exception as e:
        print(f"HATA ({channel_info['name']}): Yayın yok veya alınamadı.")
        return None

def update_channels():
    print("VPN (WARP) Aktif. Kanallar taranıyor...")
    
    m3u_content = "#EXTM3U\n"
    
    for channel in CHANNELS:
        stream_url = get_stream_link(channel)
        
        if stream_url:
            # M3U formatına uygun ekleme yap
            m3u_content += f'#EXTINF:-1 group-title="{channel["group"]}",{channel["name"]}\n'
            m3u_content += f'{stream_url}\n'
            print(f">>> EKLENDİ: {channel['name']}")
        else:
            print(f"--- ATLANDI: {channel['name']} (Canlı yayın yok)")

    # Dosyayı kaydet (kanallar.m3u olarak)
    with open('kanallar.m3u', 'w', encoding='utf-8') as f:
        f.write(m3u_content)
    
    print("\n>>> İŞLEM TAMAM: 'kanallar.m3u' dosyası oluşturuldu. <<<")

if __name__ == "__main__":
    update_channels()
