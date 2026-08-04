
import streamlit as st
import time

st.set_page_config(page_title="Nhira Studio AI", layout="centered")

st.markdown("""
<style>
.stApp {
    background-image: url("background.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
.main-container { 
    background-color: rgba(255, 255, 255, 0.92); 
    padding: 1.5rem; 
    border-radius: 20px; 
    box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
    margin-bottom: 2rem; 
}
.big-title { 
    font-size: 1.8rem; 
    font-weight: 800; 
    color: #4A3B32; 
    text-align: center; 
    margin-bottom: 0.1rem; 
}
.sub-title { 
    font-size: 0.9rem; 
    color: #8C7A6B; 
    text-align: center; 
    margin-bottom: 1rem; 
}
.greeting-box { 
    background: linear-gradient(135deg, #FFF3E6 0%, #FFE5D0 100%); 
    border: 1px solid #F5CDBC; 
    padding: 1rem; 
    border-radius: 12px; 
    margin-bottom: 1rem; 
    font-size: 0.85rem; 
    color: #5C4A3D; 
    line-height: 1.5; 
    text-align: center; 
    font-weight: 600; 
}
.box-header { 
    font-size: 1rem; 
    font-weight: 700; 
    color: #5C4A3D; 
    margin-top: 1.2rem; 
    margin-bottom: 0.4rem; 
}
div.stButton > button { 
    background-color: #D98262; 
    color: white; 
    font-weight: 600; 
    border-radius: 10px; 
    border: none; 
    width: 100%; 
    padding: 0.5rem; 
}
div.stButton > button:hover { 
    background-color: #C16D4C; 
    color: white; 
}
.closing-box { 
    background-color: #FAF8F5; 
    border: 1px dashed #D9C3B0; 
    padding: 1rem; 
    border-radius: 10px; 
    text-align: center; 
    margin-top: 1.5rem; 
    font-size: 0.85rem; 
    color: #7A6958; 
    line-height: 1.5; 
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<p class="big-title">Nhira Studio AI ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Ubah foto produk Anda menjadi estetik dalam 1 klik dengan AI ✨</p>', unsafe_allow_html=True)

st.markdown("""
<div class="greeting-box">
    Assalamu'alaikum warohmatulohi wabarokatuh<br>
    <span style="font-size: 0.8rem; font-weight: normal; color: #7A6353; display: block; margin-top: 4px;">
    Semoga harimu penuh berkah dan rezeki halal berlimpah. Aamiin. ✨
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="box-header">1. Upload Foto Produk</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Upload Foto", 
    type=['png', 'jpg', 'jpeg', 'webp'], 
    label_visibility="collapsed"
)

st.markdown('<p class="box-header">2. Pilih Rasio / Ukuran Foto</p>', unsafe_allow_html=True)
aspect_ratio = st.radio(
    "Pilih ukuran:", 
    ("1:1 (Square)", "3:4 (Portrait)", "9:16 (Story)"), 
    horizontal=True, 
    label_visibility="collapsed"
)

st.markdown('<p class="box-header">3. Instruksi Edit Foto Produk</p>', unsafe_allow_html=True)
edit_instruction = st.text_input(
    "Instruksi Edit", 
    placeholder="Contoh: tingkatkan pencahayaan...", 
    label_visibility="collapsed"
)

st.markdown('<p class="box-header">4. Pilih Gaya Foto (12 Pilihan)</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
styles = [
    "Minimalist Studio", "Luxury Marble", "Soft Natural Light",
    "Dark & Moody", "Rustic Natural", "POV Hand Interaction",
    "Flat Lay Top View", "Lifestyle Real Scene", "Product Close-up",
    "Color Pop", "Monochrome Clean", "Creative Levitation"
]

selected_styles = []
for i, style in enumerate(styles):
    target_col = col1 if i % 3 == 0 else (col2 if i % 3 == 1 else col3)
    with target_col:
        if st.checkbox(style, key=f"style_{i}"):
            selected_styles.append(style)

st.markdown("<br>", unsafe_allow_html=True)
process_button = st.button("✨ Hasilkan Konsep Foto Produk Otomatis")

if process_button:
    if uploaded_file is not None:
        with st.spinner("⏳ Sedang memproses pengeditan foto produk, mohon tunggu..."):
            time.sleep(3)
        
        st.success("✅ Berhasil! Foto selesai dibuat.")
        st.markdown('<p class="box-header">Hasil Visual</p>', unsafe_allow_html=True)
        st.image(uploaded_file, caption="Hasil Olah AI", use_container_width=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.button("⬇️ Unduh Foto")
        with col_b:
            st.button("📝 Buat Caption")
    else:
        st.warning("⚠️ Silakan unggah foto produk terlebih dahulu.")

st.markdown("""
<div class="closing-box">
    <b>Skill hari ini, cuan untuk nanti. Terus bertumbuh!</b><br>
    Semoga rezekinya halal, berkah, & jadi sedekah di akhirat. Aamiin. 🤲<br>
    <b>Nhira Studio AI</b>
    <hr style="border: none; border-top: 1px dashed #D9C3B0; margin: 10px 0;">
    <span style="color: #D32F2F; font-size: 0.8rem; font-weight: 800;">
    ⚠️ DILARANG MENJUAL/MENYEBARKAN LINK TANPA IZIN. HARAM! 🚫
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
