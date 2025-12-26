import yt_dlp
import sys

# GENİŞLETİLMİŞ KANAL LİSTESİ
# Her biri için ayrı bir .m3u dosyası oluşturulacak.
CHANNELS = [
    # --- ULUSAL & EĞLENCE ---
    {"name": "Show TV", "url": "https://www.youtube.com/@ShowTV/live", "filename": "show_tv.m3u"},
    {"name": "Kanal 7", "url": "https://www.youtube.com/@kanal7/live", "filename": "kanal7.m3u"},
    {"name": "Beyaz TV", "url": "https://www.youtube.com/@BeyazTV/live", "filename": "beyaz_tv.m3u"},
    {"name": "TV8 Buçuk", "url": "https://www.youtube.com/@tv8bucuk/live", "filename": "tv8_bucuk.m3u"},
    {"name": "Teve2", "url": "https://www.youtube.com/@teve2/live", "filename": "teve2.m3u"},
    {"name": "NOW TV", "url": "https://www.youtube.com/@NOWturkiye/live", "filename": "now.m3u"},
    {"name": "360 TV", "url": "https://www.youtube.com/@tv360comtr/live", "filename": "360_tv.m3u"},
    
    # --- HABER (TÜRKİYE) ---
    {"name": "Sözcü TV", "url": "https://www.youtube.com/@SozcuTV/live", "filename": "sozcu.m3u"},
    {"name": "Halk TV", "url": "https://www.youtube.com/@halktv/live", "filename": "halk_tv.m3u"},
    {"name": "Tele1", "url": "https://www.youtube.com/@tele1comtr/live", "filename": "tele1.m3u"},
    {"name": "Habertürk", "url": "https://www.youtube.com/@HaberturkTV/live", "filename": "haberturk.m3u"},
    {"name": "NTV", "url": "https://www.youtube.com/@ntv/live", "filename": "ntv.m3u"},
    {"name": "CNN Türk", "url": "https://www.youtube.com/@cnnturk/live", "filename": "cnn_turk.m3u"},
    {"name": "TRT Haber", "url": "https://www.youtube.com/@trthaber/live", "filename": "trt_haber.m3u"},
    {"name": "TGRT Haber", "url": "https://www.youtube.com/@tgrthaber/live", "filename": "tgrt_haber.m3u"},
    {"name": "KRT TV", "url": "https://www.youtube.com/@krtkulturtv/live", "filename": "krt_tv.m3u"},
    
    # --- EKONOMİ ---
    {"name": "CNBC-e", "url": "https://www.youtube.com/@cnbce/live", "filename": "cnbce.m3u"},
    {"name": "Bloomberg HT", "url": "https://www.youtube.com/@BloombergHT/live", "filename": "bloomberg_ht.m3u"},
    
    # --- ÇOCUK & ÇİZGİ FİLM ---
    {"name": "Cartoon Network TR", "url": "https://www.youtube.com/@CartoonNetworkTurkiye/live", "filename": "cartoon_network.m3u"},
    {"name": "SpaceToon", "url": "https://www.youtube.com/@spacetoon/live", "filename": "spacetoon.m3u"},
    {"name": "Minika ÇOCUK", "url": "https://www.youtube.com/@minika/live", "filename": "minika.m3u"},
    {"name": "Nickelodeon TR", "url": "https://www.youtube.com/@NickelodeonTurkiye/live", "filename": "nickelodeon_tr.m3u"},
    {"name": "Nick Jr. TR", "url": "https://www.youtube.com/@NickJrTurkiye/live", "filename": "nick_jr_tr.m3u"},
    {"name": "SpongeBob (7/24 Yayın)", "url": "https://www.youtube.com/@SpongeBobOfficial/live", "filename": "spongebob_live.m3u"},
    
    # --- MÜZİK ---
    {"name": "Kral Pop", "url": "https://www.youtube.com/@kralpop/live", "filename": "kral_pop.m3u"},
    {"name": "PowerTürk", "url": "https://www.youtube.com/@PowerTurkTV/live", "filename": "powerturk.m3u"},
    {"name": "Dream Türk", "url": "https://www.youtube.com/@DreamTurk/live", "filename": "dream_turk.m3u"},
    {"name": "Lofi Girl (Ders/Relax)", "url": "https://www.youtube.com/@LofiGirl/live", "filename": "lofi_girl.m3u"},
    {"name": "Number1 TV (Yabancı Hit)", "url": "https://www.youtube.com/@number1tv/live", "filename": "number1_tv.m3u"},
    {"name": "Number1 Türk", "url": "https://www.youtube.com/@number1turktv/live", "filename": "number1_turk.m3u"},
    {"name": "Power TV (Global Pop)", "url": "https://www.youtube.com/@PowerTVWorld/live", "filename": "power_tv.m3u"},
    {"name": "MTV Lebanon", "url": "https://www.youtube.com/@mtvlebanon/live", "filename": "mtv_lebanon.m3u"},
    {"name": "NetD Müzik (Mix)", "url": "https://www.youtube.com/@netdmuzik/live", "filename": "netd_mix.m3u"},
    
    # --- YABANCI & DÜNYA (Ücretsiz) ---
    {"name": "NASA TV", "url": "https://www.youtube.com/@NASA/live", "filename": "nasa_tv.m3u"},
    {"name": "Al Jazeera English", "url": "https://www.youtube.com/@aljazeeraenglish/live", "filename": "al_jazeera_en.m3u"},
    {"name": "France 24 English", "url": "https://www.youtube.com/@FRANCE24.English/live", "filename": "france24_en.m3u"},
    {"name": "DW News (Almanya)", "url": "https://www.youtube.com/@dwnews/live", "filename": "dw_news.m3u"},
    {"name": "Euronews Türkçe", "url": "https://www.youtube.com/@euronews.turkce/live", "filename": "euronews_tr.m3u"},
    
    # --- AZERBAYCAN ---
    {"name": "İctimai TV", "url": "https://www.youtube.com/@ictimaitv/live", "filename": "ictimai_tv.m3u"},
    {"name": "ARB TV", "url": "https://www.youtube.com/@arbtv/live", "filename": "arb_tv.m3u"}
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
            # Sadece linki al, indirme yapma
            info = ydl.extract_info(url, download=False)
            if 'url' in info:
                return info['url']
    except Exception:
        return None
    return None

def update_separate_files():
    print(f"Toplam {len(CHANNELS)} kanal taranıyor...")
    print("-" * 40)
    
    for channel in CHANNELS:
        print(f"İşleniyor: {channel['name']}...", end=" ")
        
        stream_url = get_stream_link(channel['url'])
        
        if stream_url:
            # Dosya içeriği
            content = f"#EXTM3U\n#EXTINF:-1,{channel['name']}\n{stream_url}"
            
            # Kanalın özel dosyasına yaz
            with open(channel['filename'], 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ OK ({channel['filename']})")
        else:
            print("❌ YAYIN YOK (Dosya oluşturulmadı)")

    print("-" * 40)
    print("Tüm işlemler tamamlandı.")

if __name__ == "__main__":
    update_separate_files()
