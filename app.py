import streamlit as st

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="Nhira Studio AI - Aesthetic Food Photo Generator", layout="centered")

# --- CSS Kustom untuk Styling ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .main-container {
        background-color: #faf7f2;
        padding: 2rem;
        border-radius: 15px;
        color: #333333;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .big-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1f1f1f;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4f4f4f;
        text-align: center;
        margin-bottom: 2rem;
    }
    .custom-box {
        border: 2px solid #f0a2b7;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        background-color: #ffffff;
    }
    .box-header {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1f1f1f;
        margin-bottom: 1rem;
    }
    .body-text {
        font-size: 1rem;
        line-height: 1.5;
        color: #4f4f4f;
    }
    div.stButton > button {
        background-color: #11995e;
        color: white;
        font-weight: 600;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 2rem;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #0e7a4c;
    }
    </style>
""", unsafe_allow_html=True)

# --- Tampilan Utama ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<p class="big-title">Aesthetic Food Photo Generator by Nhira Studio AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Ubah foto makanan-mu menjadi estetik dalam hitungan detik! Hanya dari 1 foto bisa menjadi 8 foto estetik.</p>', unsafe_allow_html=True)

# --- Tutorial Singkat ---
st.markdown('<div class="custom-box">', unsafe_allow_html=True)
st.markdown('<p class="box-header">Tutorial Singkat:</p>', unsafe_allow_html=True)
st.markdown("""
    <ol class="body-text">
        <li>Unggah foto produk makanan / minuman-mu.</li>
        <li>Pilih mode "Hasilkan 8 Konsep Visual Otomatis", atau</li>
        <li>Pilih sampai 8 konsep foto yang kamu inginkan di mode custom.</li>
        <li>Tunggu fotonya muncul di panel "Hasil Visual".</li>
    </ol>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 1. Unggah Foto Produk ---
st.markdown('<p class="box-header">1. Unggah Foto Produk</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(" ", type=['png', 'jpg', 'webp'])

st.markdown('<p class="body-text" style="margin-top: 1rem; margin-bottom: 0.5rem;">Rasio Aspek (Opsional, Beta Version)</p>', unsafe_allow_html=True)
aspect_ratio = st.radio(" ", ("Default", "1:1", "3:4", "9:16", "16:9"), horizontal=True, label_visibility="collapsed")

st.markdown('<p class="body-text" style="margin-top: 1rem; margin-bottom: 0.5rem;">Deskripsi Singkat Produk (Opsional)</p>', unsafe_allow_html=True)
product_description = st.text_input(" ", placeholder="Contoh: Jus Mangga, Salad Isi Sayuran", label_visibility="collapsed")

# --- 2. Pilih Mode Generate ---
st.markdown('<p class="box-header" style="margin-top: 2rem;">2. Pilih Mode Generate</p>', unsafe_allow_html=True)

if st.button("✨ Hasilkan 8 Konsep Visual Otomatis"):
    if uploaded_file is not None:
        st.success("Berhasil! Menyiapkan 8 konsep visual otomatis...")
    else:
        st.warning("⚠️ Silakan unggah foto produk terlebih dahulu.")

st.markdown('<p class="body-text" style="text-align: center; margin: 1rem 0;">ATAU</p>', unsafe_allow_html=True)
st.markdown('<p class="box-header">Pilih Konsep Custom (Maks. 8)</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    c1 = st.checkbox("Cerah")
    c2 = st.checkbox("Vintage Style")
    c3 = st.checkbox("Nature's Outdoor")
    c4 = st.checkbox("Cultural Mode")
    c5 = st.checkbox("Aesthetic Cafe")
    c6 = st.checkbox("Pop Color")
    c7 = st.checkbox("Cinematic")
    c8 = st.checkbox("Hasil Panen")
    c9 = st.checkbox("Storytelling")
    c10 = st.checkbox("Flatlay")
    c11 = st.checkbox("Editorial Style")
    c12 = st.checkbox("Close up")

with col2:
    c13 = st.checkbox("Premium Style")
    c14 = st.checkbox("Natural Indoor")
    c15 = st.checkbox("Dark and Moody")
    c16 = st.checkbox("Dapur Estetik")
    c17 = st.checkbox("Pastel Studio")
    c18 = st.checkbox("Frame Mockup")
    c19 = st.checkbox("Shadows")
    c20 = st.checkbox("Melayang")
    c21 = st.checkbox("UGC")
    c22 = st.checkbox("Gaya Katalog")
    c23 = st.checkbox("Ingredients Story")
    c24 = st.checkbox("Clean Look")

selected_count = sum([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, 
                      c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24])

st.markdown('<p class="body-text" style="margin-top: 1rem; margin-bottom: 0.5rem;">Properti Tambahan (Opsional)</p>', unsafe_allow_html=True)
extra_props = st.text_input(" ", placeholder="Contoh: daun mint, irisan lemon", label_visibility="collapsed")

if st.button(f"🎨 Hasilkan {selected_count} Konsep Custom"):
    if uploaded_file is not None and selected_count > 0:
        st.success(f"Berhasil! Memproses {selected_count} konsep pilihan...")
    elif uploaded_file is None:
        st.warning("⚠️ Silakan unggah foto produk terlebih dahulu.")
    else:
        st.warning("⚠️ Silakan pilih setidaknya satu konsep custom.")

# --- 3. Hasil Visual ---
st.markdown('<p class="box-header" style="margin-top: 2rem;">3. Hasil Visual</p>', unsafe_allow_html=True)
st.info("Hasil akan muncul di sini setelah Anda menekan tombol 'Hasilkan'.")

# --- Footer ---
st.markdown("---")
st.markdown("""
    <p class="body-text" style="text-align: center; font-size: 0.85rem; color: #888888;">
    Dibuat oleh : **Nhira Studio AI**<br>
    Generator ini bersifat Personal Use Only. Hanya untuk pemakaian pribadi. 
    Tidak boleh disebarkan tanpa izin, dijual ulang tanpa izin, atau disalin dalam bentuk apa pun 🙏.<br>
    OPEN PUBLIC AFFILIATE LEWAT LYNK, Search : Aesthetic Food Photo Generator - GT03
    </p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
