import yt_dlp
import sys
import os

# SENİN TAM LİSTEN (HİÇBİRİNİ SİLMEDİM)
CHANNELS = [
    # 1. AMERİKA & İNGİLTERE
    {"name": "ABC News Live (USA)", "url": "https://abcnews.go.com/Live", "filename": "abc_news_usa.m3u"},
    {"name": "CBS News (USA)", "url": "https://www.cbsnews.com/live/", "filename": "cbs_news_usa.m3u"},
    {"name": "Sky News UK", "url": "https://www.youtube.com/@SkyNews/live", "filename": "sky_news_uk.m3u"},
    {"name": "NASA TV Public", "url": "https://www.nasa.gov/multimedia/nasatv/index.html", "filename": "nasa_tv.m3u"},
    {"name": "Voice of America", "url": "https://www.youtube.com/@voanews/live", "filename": "voa_news.m3u"},

    # 2. AVRUPA KANALLARI
    {"name": "DW News (Germany)", "url": "https://www.youtube.com/@dwnews/live", "filename": "dw_news.m3u"},
    {"name": "France 24 English", "url": "https://www.youtube.com/@FRANCE24.English/live", "filename": "france24_en.m3u"},
    {"name": "Euronews Türkçe", "url": "https://www.youtube.com/@euronews.turkce/live", "filename": "euronews_tr.m3u"},
    {"name": "TVP World", "url": "https://www.youtube.com/@TVPWorld/live", "filename": "tvp_world.m3u"},

    # 3. TÜRK KANALLARI (EURO / AVRUPA)
    {"name": "Kanal 7 Avrupa", "url": "https://www.kanal7avrupa.com/canli-yayin", "filename": "kanal7_avrupa.m3u"},
    {"name": "TV8 Int (Avrupa)", "url": "https://www.tv8int.com/canli-yayin", "filename": "tv8_int.m3u"},
    
    # --- HABER KANALLARI ---
    {"name": "Sözcü TV", "url": "https://www.youtube.com/watch?v=ztmY_cCtUl0", "filename": "sozcu.m3u"},
    {"name": "Halk TV", "url": "https://www.youtube.com/channel/UC43Z0H99r2Y2uK68zTqF_7g/live", "filename": "halk_tv.m3u"},
    {"name": "Tele1", "url": "https://www.youtube.com/channel/UCHKX1Y43Q_5Xo6cW6zRkX8Q/live", "filename": "tele1.m3u"},
    {"name": "Habertürk", "url": "https://www.youtube.com/channel/UCj-X5G27b7_N26q44x0-b6g/live", "filename": "haberturk.m3u"},
    {"name": "NTV", "url": "https://www.youtube.com/channel/UCc1S8iqs2rS020-sH9x3C4w/live", "filename": "ntv.m3u"},
    {"name": "CNN Türk", "url": "https://www.youtube.com/channel/UC4d_d58n9M62Yy-6t7sJ-DA/live", "filename": "cnn_turk.m3u"},
    {"name": "TRT Haber", "url": "https://www.youtube.com/channel/UCx3240R_Xw6w5tXyQ4n_Y9w/live", "filename": "trt_haber.m3u"},
    {"name": "TV100", "url": "https://www.youtube.com/channel/UCndsdCS_o_pQwGscD-d8Zgw/live", "filename": "tv100.m3u"},

    # --- ULUSAL & EĞLENCE ---
    # Not: Listendeki 'UC-1-2-3-4-5-6-7' gibi sahte ID'leri gerçekleriyle değiştirmen gerekir.
    {"name": "Show TV", "url": "https://www.youtube.com/@ShowTV/live", "filename": "show_tv.m3u"},
    {"name": "Kanal 7", "url": "https://www.youtube.com/@Kanal7/live", "filename": "kanal7.m3u"},
    {"name": "NOW TV", "url": "https://www.youtube.com/@NOWHaber/live", "filename": "now.m3u"},

    # --- MÜZİK ---
    {"name": "PowerTürk", "url": "https://www.youtube.com/@PowerTurk/live", "filename": "powerturk.m3u"},
    {"name": "Kral Pop", "url": "https://www.youtube.com/@kralpop/live", "filename": "kral_pop.m3u"}
]

def get_stream_link(url):
    # IPTV Smarters için 'ios' istemcisi en stabil m3u8 linkini verir.
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'extractor_args': {
            'youtube': {
                'player_client': ['ios'],
            }
        }
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get('url')
    except Exception:
        return None

def update_separate_files():
    print(f"{len(CHANNELS)} kanal işleniyor...")
    
    for channel in CHANNELS:
        stream_url = get_stream_link(channel['url'])
        
        if stream_url:
            # IPTV Smarters Pro bazen '|' karakterini tanımaz, 
            # bu yüzden temiz linki veriyoruz.
            content = f"#EXTM3U\n#EXTINF:-1,{channel['name']}\n{stream_url}"
            
            with open(channel['filename'], 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {channel['name']}")
        else:
            print(f"❌ {channel['name']} (Link Alınamadı)")

if __name__ == "__main__":
    update_separate_files()
