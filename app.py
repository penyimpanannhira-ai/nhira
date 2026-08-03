import streamlit as st

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="Nhira Studio AI - Aesthetic Food Photo Generator", layout="centered")

# --- CSS Kustom untuk Background & Styling Pastel ---
st.markdown("""
    <style>
    /* Mengubah background utama aplikasi menjadi krem pastel yang hangat */
    .stApp {
        background-color: #FFF8F0; 
    }
    
    /* Mengubah warna teks secara umum agar elegan */
    h1, h2, h3, h4, h5, h6, p, label, .stCheckbox label {
        color: #4A4A4A; 
    }
    
    /* Container utama aplikasi */
    .main-container {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
    }
    
    /* Judul Besar */
    .big-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #2D2D2D;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    /* Sub-judul */
    .sub-title {
        font-size: 1.05rem;
        color: #666666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* KOTAK TUTORIAL ESTETIK (Warna Kuning Pastel Lembut / Butter) */
    .tutorial-box {
        background-color: #FFFDF0; /* Kuning pastel sangat lembut */
        border: 2px dashed #FFD166; /* Border putus-putus kuning/gold estetik */
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 10px rgba(255, 209, 102, 0.15);
    }
    
    .tutorial-header {
        font-size: 1.2rem;
        font-weight: 700;
        color: #D4A373; /* Warna teks cokelat madu yang manis */
        margin-bottom: 0.8rem;
    }
    
    .tutorial-content {
        font-size: 0.95rem;
        line-height: 1.6;
        color: #555555;
    }

    /* Header Bagian Lain */
    .box-header {
        font-size: 1.2rem;
        font-weight: 700;
        color: #2D2D2D;
        margin-bottom: 1rem;
    }
    
    /* Tombol Utama (Pink Pastel Menarik) */
    div.stButton > button {
        background-color: #FFB5A7; /* Pink pastel lembut */
        color: white;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 2rem;
        width: 100%;
        box-shadow: 0 4px 10px rgba(255, 181, 167, 0.4);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #F89690;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- Tampilan Utama Container ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="big-title">Aesthetic Food Photo Generator by Nhira Studio AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Ubah foto makanan-mu menjadi estetik dalam hitungan detik! Hanya dari 1 foto bisa menjadi 8 foto estetik.</p>', unsafe_allow_html=True)

# --- Kotak Tutorial Estetik (Berbeda dari Background, Tetap Senada) ---
st.markdown("""
    <div class="tutorial-box">
        <p class="tutorial-header">✨ Tutorial Singkat Penggunaan:</p>
        <ol class="tutorial-content">
            <li>Unggah foto produk makanan atau minuman andalanmu.</li>
            <li>Pilih mode <b>"Hasilkan 8 Konsep Visual Otomatis"</b>, atau</li>
            <li>Pilih hingga 8 konsep foto sesuai keinginanmu di mode custom.</li>
            <li>Tunggu beberapa saat hingga hasil foto muncul di panel <b>"Hasil Visual"</b>.</li>
        </ol>
    </div>
""", unsafe_allow_html=True)

# --- 1. Unggah Foto Produk ---
st.markdown('<p class="box-header">1. Unggah Foto Produk</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(" ", type=['png', 'jpg', 'webp'])

st.markdown('<p class="body-text" style="margin-top: 1rem; margin-bottom: 0.5rem; color: #4A4A4A;">Rasio Aspek (Opsional, Beta Version)</p>', unsafe_allow_html=True)
aspect_ratio = st.radio(" ", ("Default", "1:1", "3:4", "9:16", "16:9"), horizontal=True, label_visibility="collapsed")

st.markdown('<p class="body-text" style="margin-top: 1rem; margin-bottom: 0.5rem; color: #4A4A4A;">Deskripsi Singkat Produk (Opsional)</p>', unsafe_allow_html=True)
product_description = st.text_input(" ", placeholder="Contoh: Jus Mangga, Salad Isi Sayuran", label_visibility="collapsed")

# --- 2. Pilih Mode Generate ---
st.markdown('<p class="box-header" style="margin-top: 2rem;">2. Pilih Mode Generate</p>', unsafe_allow_html=True)

if st.button("✨ Hasilkan 8 Konsep Visual Otomatis"):
    if uploaded_file is not None:
        st.success("Berhasil! Menyiapkan 8 konsep visual otomatis...")
    else:
        st.warning("⚠️ Silakan unggah foto produk terlebih dahulu.")

st.markdown('<p style="text-align: center; margin: 1rem 0; color: #888888;">— ATAU —</p>', unsafe_allow_html=True)
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

st.markdown('<p class="body-text" style="margin-top: 1rem; margin-bottom: 0.5rem; color: #4A4A4A;">Properti Tambahan (Opsional)</p>', unsafe_allow_html=True)
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
    <p style="text-align: center; font-size: 0.85rem; color: #888888; line-height: 1.5;">
    Dibuat oleh : <b>Nhira Studio AI</b><br>
    Generator ini bersifat Personal Use Only. Hanya untuk pemakaian pribadi. 
    Tidak boleh disebarkan tanpa izin, dijual ulang tanpa izin, atau disalin dalam bentuk apa pun 🙏.<br>
    OPEN PUBLIC AFFILIATE LEWAT LYNK, Search : Aesthetic Food Photo Generator - GT03
    </p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Tutup main-container
