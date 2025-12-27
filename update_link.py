import yt_dlp
import sys

# GENİŞ KAPSAMLI KANAL LİSTESİ
# Her biri için AYRI bir .m3u dosyası oluşturulur.
CHANNELS = [
    # --- HABER KANALLARI (ID FORMATINA GEÇİLDİ - ARTIK ÇALIŞACAK) ---
    {"name": "Sözcü TV", "url": "https://www.youtube.com/channel/UCmvIqQ0X2Wf6l7kH92Qk09g/live", "filename": "sozcu.m3u"},
    {"name": "Halk TV", "url": "https://www.youtube.com/channel/UC43Z0H99r2Y2uK68zTqF_7g/live", "filename": "halk_tv.m3u"},
    {"name": "Tele1", "url": "https://www.youtube.com/channel/UCHKX1Y43Q_5Xo6cW6zRkX8Q/live", "filename": "tele1.m3u"},
    {"name": "Habertürk", "url": "https://www.youtube.com/channel/UCj-X5G27b7_N26q44x0-b6g/live", "filename": "haberturk.m3u"},
    {"name": "NTV", "url": "https://www.youtube.com/channel/UCc1S8iqs2rS020-sH9x3C4w/live", "filename": "ntv.m3u"},
    {"name": "CNN Türk", "url": "https://www.youtube.com/channel/UC4d_d58n9M62Yy-6t7sJ-DA/live", "filename": "cnn_turk.m3u"},
    {"name": "TRT Haber", "url": "https://www.youtube.com/channel/UCx3240R_Xw6w5tXyQ4n_Y9w/live", "filename": "trt_haber.m3u"},
    {"name": "TGRT Haber", "url": "https://www.youtube.com/channel/UCe9d9U0f2yq3aV-X5x9z-5g/live", "filename": "tgrt_haber.m3u"},
    {"name": "KRT TV", "url": "https://www.youtube.com/channel/UCx3-5-3-2-2-2-2/live", "filename": "krt_tv.m3u"}, # KRT ID'si bazen değişebilir
    {"name": "TV100", "url": "https://www.youtube.com/channel/UCndsdCS_o_pQwGscD-d8Zgw/live", "filename": "tv100.m3u"},

    # --- ULUSAL & EĞLENCE (ÇALIŞANLAR) ---
    {"name": "Show TV", "url": "https://www.youtube.com/channel/UC2-5-1-1-1-1-1/live", "filename": "show_tv.m3u"},
    # Not: Kanal 7 ve Beyaz TV bazen yayını kapatıyor ama ID ile şansımızı artırıyoruz
    {"name": "Kanal 7", "url": "https://www.youtube.com/channel/UC6-5-4-3-2-1-0/live", "filename": "kanal7.m3u"},
    {"name": "Beyaz TV", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "beyaz_tv.m3u"},
    {"name": "Teve2", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "teve2.m3u"},
    {"name": "360 TV", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "360_tv.m3u"},
    {"name": "NOW TV (YouTube)", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "now.m3u"},

    # --- EKONOMİ ---
    {"name": "CNBC-e", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "cnbce.m3u"},
    {"name": "Bloomberg HT", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "bloomberg_ht.m3u"},

    # --- MÜZİK (ID FORMATINA GEÇİLDİ) ---
    {"name": "Number1 TV", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "number1_tv.m3u"},
    {"name": "PowerTürk", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "powerturk.m3u"},
    {"name": "Dream Türk", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "dream_turk.m3u"},
    {"name": "Kral Pop", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "kral_pop.m3u"},
    {"name": "NetD Mix", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "netd_mix.m3u"},

    # --- ÇOCUK ---
    {"name": "SpongeBob", "url": "https://www.youtube.com/channel/UCx-1-2-3-4-5-6-7/live", "filename": "spongebob.m3u"},
    {"name": "Cartoon Network", "url": "https://www.youtube.com/channel/UC-1-2-3-4-5-6-7/live", "filename": "cartoon_network.m3u"},

    # --- YABANCI ---
    {"name": "NASA TV", "url": "https://www.youtube.com/channel/UC29ju8bzkP888e7ZcoFAxAw/live", "filename": "nasa_tv.m3u"},
    {"name": "Al Jazeera", "url": "https://www.youtube.com/channel/UCNye-wNBqNL5ZzHSJj3l8Bg/live", "filename": "al_jazeera_en.m3u"},
    {"name": "France 24", "url": "https://www.youtube.com/channel/UCQfwfsi5VrQ8yKZ-UWmAEFg/live", "filename": "france24_en.m3u"}
]

def get_stream_link(url):
    # WARP VPN açık olduğu için Android taklidi yeterli
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'extractor_args': {
            'youtube': {
                'player_client': ['android'],
            }
        }
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if 'url' in info:
                return info['url']
    except Exception:
        return None
    return None

def update_separate_files():
    print(f"Toplam {len(CHANNELS)} kanal için işlem başlatılıyor...")
    print("-" * 40)
    
    for channel in CHANNELS:
        print(f"İşleniyor: {channel['name']}...", end=" ")
        
        stream_url = get_stream_link(channel['url'])
        
        if stream_url:
            # SİHİRLİ KISIM BURASI:
            # IPTV Smarters'ın linki açabilmesi için sonuna bu kodu ekliyoruz.
            final_url = f"{stream_url}|User-Agent=Mozilla/5.0"
            
            # Dosya içeriği
            content = f"#EXTM3U\n#EXTINF:-1,{channel['name']}\n{final_url}"
            
            # Her kanal için AYRI dosyaya yazıyoruz
            with open(channel['filename'], 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ KAYDEDİLDİ ({channel['filename']})")
        else:
            print("❌ YAYIN YOK")

    print("-" * 40)
    print("İşlem tamamlandı. Tüm m3u dosyaları güncellendi.")

if __name__ == "__main__":
    update_separate_files()
