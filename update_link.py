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
    
    # --- EKONOMİ ---
    {"name": "CNBC-e", "url": "https://www.youtube.com/@cnbce/live", "filename": "cnbce.m3u"},
    {"name": "Bloomberg HT", "url": "https://www.youtube.com/@BloombergHT/live", "filename": "bloomberg_ht.m3u"},
    
    # --- ÇOCUK & ÇİZGİ FİLM ---
    {"name": "Cartoon Network TR", "url": "https://www.youtube.com/@CartoonNetworkTurkiye/live", "filename": "cartoon_network.m3u"},
    {"name": "SpaceToon", "url": "https://www.youtube.com/@spacetoon/live", "filename": "spacetoon.m3u"},
    {"name": "Minika ÇOCUK", "url": "https://www.youtube.com/@minika/live", "filename": "minika.m3u"},
    
    # --- MÜZİK ---
    {"name": "Kral Pop", "url": "https://www.youtube.com/@kralpop/live", "filename": "kral_pop.m3u"},
    {"name": "PowerTürk", "url": "https://www.youtube.com/@PowerTurkTV/live", "filename": "powerturk.m3u"},
    {"name": "Dream Türk", "url": "https://www.youtube.com/@DreamTurk/live", "filename": "dream_turk.m3u"},
    {"name": "Lofi Girl (Ders/Relax)", "url": "https://www.youtube.com/@LofiGirl/live", "filename": "lofi_girl.m3u"},
    
    # --- YABANCI & DÜNYA (Ücretsiz) ---
    {"name": "NASA TV", "url": "https://www.youtube.com/@NASA/live", "filename": "nasa_tv.m3u"},
    {"name": "Al Jazeera English", "url": "https://www
