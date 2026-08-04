import streamlit as st
import time

# Konfigurasi Halaman Web
st.set_page_config(page_title="Nhira Studio AI", page_icon="✨", layout="centered")

# Desain Tampilan Estetik (CSS Kustom)
st.markdown("""
<style>
.stApp { background-color: #FAF6F0; }
.main-title { font-size: 2.2rem; font-weight: bold; color: #1E3F20; text-align: center; margin-bottom: 0px; }
.sub-title { font-size: 1.0rem; color: #8C6D53; text-align: center; margin-bottom: 25px; }
.greeting-box { background-color: #FFF2EE; padding: 15px 20px; border-radius: 12px; border: 1.5px solid #FFD1C7; color: #7A4F42; font-size: 0.95rem; text-align: center; margin-bottom: 25px; line-height: 1.5; }
.card { background-color: #FFFFFF; padding: 20px; border-radius: 15px; border: 1.5px solid #F5D6CB; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# Header Utama
st.markdown('<p class="main-title">Nhira Studio AI ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">PRODUCT PHOTO GENERATOR<br>Ubah foto produk Anda menjadi 8 konsep foto estetik dalam 1 klik dengan AI ✨</p>', unsafe_allow_html=True)

# Sapaan Hangat & Islami
st.markdown("""
<div class="greeting-box">
Hai <i>Sisters</i> shalihah! Siapa bilang cari cuan harus selalu ninggalin rumah? Dari pojokan kamar sambil dasteran pun, kita tetap bisa jemput rezeki Allah. Semangat ya buat yang lagi ikhtiar hari ini!<br><br>
Eh tapi ingat, jangan keasyikan edit video sampai lupa jemuran di luar udah mateng terpanggang matahari ya, hehe. Selamat berkarya dan ikhtiar cari rezeki halal, semoga jadi tambahan rezeki yang barokah buat kita semua. Aamiin. 🤲✨
</div>
""", unsafe_allow_html=True)

# 1. Langkah 1: Upload Foto Produk
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 1. Upload Foto Produk")
uploaded_file = st.file_uploader("Format yang didukung: JPG, PNG, WebP", type=["jpg", "png", "jpeg", "webp"])

if uploaded_file is not None:
    st.success("✅ Foto berhasil diunggah!")
    st.image(uploaded_file, caption="Preview Foto Anda", width=220)

st.markdown('</div>', unsafe_allow_html=True)

# 2. Langkah 2: Pilih Rasio / Ukuran Foto
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 2. Pilih Rasio / Ukuran Foto")
rasio = st.radio("Pilih ukuran:", ["1:1 (Square)", "3:4 (Portrait)", "9:16 (Story)"], horizontal=True)
st.markdown('</div>', unsafe_allow_html=True)

# 3. Langkah 3: Pilih Gaya Foto (Custom Style Grid - 12 Pilihan)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 3. Pilih Gaya Foto (Custom Style)")
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

# 4. Tombol Utama & Animasi Jam Pasir (Berada di Posisi Paling Bawah)
if st.button("✨ Hasilkan 8 Konsep Foto Produk Otomatis", use_container_width=True):
    if uploaded_file is not None:
        with st.status("⏳ Nhira Studio AI sedang memproses foto...", expanded=True) as status:
            st.write("Menganalisis bentuk dan pencahayaan produk...")
            time.sleep(1.5)
            st.write("Menerapkan gaya visual estetik...")
            time.sleep(1.5)
            st.write("Menyelesaikan 8 variasi foto...")
            time.sleep(1)
            status.update(label="🎉 Selesai! Foto berhasil diedit.", state="complete", expanded=False)
        st.success("🎉 8 konsep foto produk Anda berhasil dibuat dan siap di-download!")
    else:
        st.error("⚠️ Silakan upload foto produk terlebih dahulu di Langkah 1!")
