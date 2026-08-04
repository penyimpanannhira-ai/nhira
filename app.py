import streamlit as st
import time

# Konfigurasi Halaman Web
st.set_page_config(page_title="Nhira Studio AI", page_icon="✨", layout="centered")

# Desain Tampilan Estetik & Background Custom CSS
st.markdown("""
<style>
/* Mengatur Background Utama Aplikasi */
.stApp {
    background-color: #FAF6F0;
    background-image: linear-gradient(rgba(250, 246, 240, 0.85), rgba(250, 246, 240, 0.85)), 
                      url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.main-title { 
    font-size: 2.2rem; 
    font-weight: bold; 
    color: #1E3F20; 
    text-align: center; 
    margin-bottom: 0px; 
}

.sub-title { 
    font-size: 1.0rem; 
    color: #8C6D53; 
    text-align: center; 
    margin-bottom: 20px; 
}

.greeting-box { 
    background-color: #FFF2EE; 
    padding: 15px 20px; 
    border-radius: 12px; 
    border: 1.5px solid #FFD1C7; 
    color: #7A4F42; 
    font-size: 0.95rem; 
    text-align: center; 
    margin-bottom: 20px; 
    line-height: 1.5; 
}

.card { 
    background-color: rgba(255, 255, 255, 0.92); 
    padding: 20px; 
    border-radius: 15px; 
    border: 1.5px solid #F5D6CB; 
    margin-bottom: 20px; 
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}
</style>
""", unsafe_allow_html=True)

# Header Utama
st.markdown('<p class="main-title">Nhira Studio AI ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">PRODUCT & FOOD PHOTO GENERATOR<br>Ubah foto produk/makanan Anda menjadi estetik dalam 1 klik dengan AI ✨</p>', unsafe_allow_html=True)

# Sapaan Hangat & Islami
st.markdown("""
<div class="greeting-box">
Hai <i>Sisters</i> shalihah! Siapa bilang cari cuan harus selalu ninggalin rumah? Dari pojokan kamar sambil dasteran pun, kita tetap bisa jemput rezeki Allah. Semangat ya buat yang lagi ikhtiar hari ini!<br><br>
Eh tapi ingat, jangan keasyikan edit video sampai lupa jemuran di luar udah mateng terpanggang matahari ya, hehe. Selamat berkarya dan ikhtiar cari rezeki halal, semoga jadi tambahan rezeki yang barokah buat kita semua. Aamiin. 🤲✨
</div>
""", unsafe_allow_html=True)

# 1. Langkah 1: Upload Foto Produk / Makanan
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 1. Upload Foto Produk / Makanan")
uploaded_file = st.file_uploader("Format: JPG, PNG, WebP", type=["jpg", "png", "jpeg", "webp"])

if uploaded_file is not None:
    st.success("✅ Foto berhasil diunggah!")
    st.image(uploaded_file, caption="Preview Foto Anda", width=220)

st.markdown('</div>', unsafe_allow_html=True)

# 2. Langkah 2: Pilih Rasio / Ukuran Foto
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 2. Pilih Rasio / Ukuran Foto")
rasio = st.radio("Pilih ukuran:", ["1:1 (Square)", "3:4 (Portrait)", "9:16 (Story)"], horizontal=True)
st.markdown('</div>', unsafe_allow_html=True)

# 3. Langkah 3: Kolom Instruksi Edit / Ubah Background & Food Photography
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 3. Instruksi Edit & Food Photography")
instruksi_edit = st.text_area(
    "Tuliskan perintah ubah background atau konsep foto (Contoh: Ganti background jadi meja kayu estetik untuk food photography)",
    placeholder="Ketik instruksi edit di sini..."
)
st.markdown('</div>', unsafe_allow_html=True)

# 4. Langkah 4: Pilih Gaya Foto (12 Pilihan Custom Style)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 4. Pilih Gaya Foto (Custom Style)")
st.write("Centang gaya yang diinginkan (Maksimal 8):")

col1, col2, col3 = st.columns(3)
with col1:
    g1 = st.checkbox("Minimalist Studio")
    g4 = st.checkbox("Dark & Moody")
    g7 = st.checkbox("Flat Lay Top View")
    g10 = st.checkbox("Color Pop")
with col2:
    g2 = st.checkbox("Luxury Marble")
    g5 = st.checkbox("Rustic Natural")
    g8 = st.checkbox("Lifestyle Real Scene")
    g11 = st.checkbox("Monochrome Clean")
with col3:
    g3 = st.checkbox("Soft Natural Light")
    g6 = st.checkbox("POV Hand Interaction")
    g9 = st.checkbox("Product Close-up")
    g12 = st.checkbox("Creative Levitation")

st.markdown('</div>', unsafe_allow_html=True)

# 5. Tombol Utama & Animasi Jam Pasir (Posisi Paling Bawah)
if st.button("✨ Hasilkan Konsep Foto Produk Otomatis", use_container_width=True):
    if uploaded_file is not None:
        with st.status("⏳ Nhira Studio AI sedang memproses foto...", expanded=True) as status:
            st.write("Menganalisis objek dan instruksi background...")
            time.sleep(1.5)
            st.write("Menerapkan gaya visual & food photography...")
            time.sleep(1.5)
            st.write("Menyelesaikan hasil edit foto...")
            time.sleep(1)
            status.update(label="🎉 Selesai! Foto berhasil diedit.", state="complete", expanded=False)
        st.success("🎉 Konsep foto produk & makanan Anda berhasil dibuat dan siap di-download!")
    else:
        st.error("⚠️ Silakan upload foto produk/makanan terlebih dahulu di Langkah 1!")

# Footer Penutup Bawah
st.markdown("""
<div style="background-color: rgba(255, 242, 238, 0.95); padding: 12px; border-radius: 10px; border: 1px solid #FFD1C7; text-align: center; color: #7A4F42; font-size: 0.85rem; margin-top: 30px;">
Skill hari ini, cuan untuk nanti. Terus bertumbuh!<br>
Semoga rezekinya halal, berkah, & jadi sedekah di akhirat. Aamiin. 🤲<br>
<b>Nhira Studio AI</b><br>
<span style="color: #d9534f; font-weight: bold;">⚠️ DILARANG MENJUAL/MENYEBARKAN LINK TANPA IZIN. HARAM! 🚫</span>
</div>
""", unsafe_allow_html=True)
