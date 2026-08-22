🧠 Local RAG Assistant with Microsoft Foundry & Streamlit
Bu proje; harici bir bulut API'sine (OpenAI, Anthropic vb.) bağımlı kalmadan, Microsoft Foundry Local ekosistemini kullanarak tamamen kendi yerel donanımınız üzerinde koşan, endüstri standardında Retrieval-Augmented Generation (RAG) tabanlı akıllı bir yapay zeka asistanıdır.

Proje; yerel vektör veritabanı yönetimi, akıllı arama bypass mekanizmaları, DuckDuckGo web arama yedeklemesi ve Google Gemini estetiğinden ilham alan modern bir Streamlit arayüzünü bir araya getirir.

🚀 Öne Çıkan Özellikler
🔒 %100 Lokal ve Güvenli: Verileriniz asla dışarıya çıkmaz. Microsoft Foundry Local SDK üzerinden Phi-3.5-mini (LLM) ve Qwen3-Embedding modelleri doğrudan yerelde çalışır.

⚡ Akıllı Sorgu Bypass Mekanizması: Kullanıcının "detaylandır", "özetle" veya "hangi doküman" gibi takip eden istekleri için doğrudan geçmiş sohbet ve bağlam üzerinden hızlı yanıt üretir, gereksiz vektör araması maliyetini önler.

🌐 Web Arama Yedeklemesi: Yerel veritabanında (SQLite + FAISS/Vektör) aranan bilgi bulunamadığında, entegre DuckDuckGo arama motoru üzerinden canlı web araması tetikleyerek yanıt üretebilir.

🎨 Modern Kullanıcı Arayüzü: Standart arayüzler yerine sağ/sol mesaj akışına sahip, sade ve şık bir Gemini deneyimi sunan Streamlit UI bileşenleri.

🛡️ Hata Toleranslı Mimarisi: Model yükleme (load) durumlarını otomatik kontrol eden ve eksik yüklemeleri anında yakalayıp çözen dayanıklı servis katmanları.

🛠️ Kullanılan Teknolojiler
Orkestrasyon & Arayüz: Python, Streamlit

LLM & Embedding: Microsoft Foundry Local SDK (Phi-3.5-mini, Qwen3-Embedding)

Veritabanı / Vektör Saklama: SQLite Vector Store

Arama Entegrasyonu: duckduckgo_search

📂 Proje Mimarisi
Plaintext
RAG/
│
├── config/
│   ├── model_config.py      # Model isimleri ve LLM ayarları
│   ├── prompt_templates.py  # Sistem ve kullanıcı prompt şablonları
│   └── settings.py          # Genel ayarlar
│
├── core/
│   ├── client.py            # Foundry istemci yöneticisi
│   ├── embedding_service.py # Vektörleştirme servisi (Auto-load korumalı)
│   └── llm_service.py       # Sohbet / Metin üretim servisi (Auto-load korumalı)
│
├── ingestion/               # Doküman yükleme ve parçalama (Chunking) modülleri
├── pipeline/
│   └── rag_engine.py        # Çekirdek RAG motoru (Bypass, Vektör arama, Web fallback)
├── storage/
│   └── vector_store.py      # SQLite vektör veritabanı yönetimi
├── ui/
│   ├── chat.py              # Sohbet arayüzü bileşeni
│   └── sidebar.py           # Yan panel ve dosya yönetim bileşeni
│
├── app.py                   # Ana Streamlit uygulama giriş noktası
└── README.md
⚙️ Kurulum ve Çalıştırma Adımları
Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Projeyi Klonlayın
Bash
git clone https://github.com/Emin-Erdem/local-rag-assist.git
cd local-rag-assist
2. Sanal Ortam Oluşturun ve Aktif Edin  
Bash
python -m venv .venv
# Windows için:
.venv\Scripts\activate
# macOS / Linux için:
source .venv/bin/activate
3. Gerekli Kütüphaneleri Yükleyin  
Bash
pip install -r requirements.txt
(Not: Microsoft Foundry Local SDK ve Streamlit bağımlılıklarının sisteminizde kurulu olduğundan emin olun.)

4. Uygulamayı Başlatın
Bash
streamlit run app.py
Uygulama otomatik olarak tarayıcınızda açılacaktır (http://localhost:8501). Sol panelden dokümanlarınızı yükleyerek yerel RAG asistanınızla sohbet etmeye başlayabilirsiniz!

👤 Geliştirici
Emin Erdem

Computer Engineering Student
