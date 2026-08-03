
import streamlit as st
import time

st.set_page_config(page_title="Nhira Studio AI", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #FFF8F0; }
    h1, h2, h3, h4, h5, h6, p, label, .stCheckbox label { color: #4A4A4A; }
    .main-container { background-color: #FFFFFF; padding: 2rem; border-radius: 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.05); }
    .big-title { font-size: 2.2rem; font-weight: 800; color: #2D2D2D; text-align: center; margin-bottom: 0.5rem; }
    .sub-title { font-size: 1.05rem; color: #666666; text-align: center; margin-bottom: 2rem; }
    .tutorial-box { background-color: #FFFDF0; border: 2px dashed #FFD166; border-radius: 15px; padding: 1.5rem; margin-bottom: 1.5rem; }
    .box-header { font-size: 1.2rem; font-weight: 700; color: #2D2D2D; margin-bottom: 1rem; }
    div.stButton > button { background-color: #FFB5A7; color: white; font-weight: 600; border-radius: 10px; border: none; padding: 0.6rem 2rem; width: 100%; }
    div.stButton > button:hover { background-color: #F89690; color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<p class="big-title">Aesthetic Food Photo Generator by Nhira Studio AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Ubah foto makanan-mu menjadi estetik! Maksimal 8 gaya foto dari 1 kali unggah.</p>', unsafe_allow_html=True)

st.markdown("""
    <div class="tutorial-box">
        <p style="font-size: 1.2rem; font-weight: 700; color: #D4A373; margin-bottom: 0.8rem;">✨ Tutorial Singkat:</p>
        <ol style="font-size: 0.95rem; line-height: 1.6; color: #555555;">
            <li>Unggah foto produk makanan atau minuman.</li>
            <li>Pilih mode "Hasilkan 8 Konsep Visual Otomatis", atau pilih maksimal 8 konsep di mode custom.</li>
            <li>Tunggu proses selesai hingga hasil foto dan tombol aksi muncul.</li>
        </ol>
    </div>
""", unsafe_allow_html=True)

st.markdown('<p class="box-header">1. Unggah Foto Produk</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(" ", type=['png', 'jpg', 'webp'])
aspect_ratio = st.radio("Rasio Aspek", ("Default", "1:1", "3:4", "9:16", "16:9"), horizontal=True, label_visibility="collapsed")
product_description = st.text_input("Deskripsi", placeholder="Contoh: Jus Mangga", label_visibility="collapsed")

st.markdown('<p class="box-header" style="margin-top: 2rem;">2. Pilih Mode Generate</p>', unsafe_allow_html=True)
auto_generate = st.button("✨ Hasilkan 8 Konsep Visual Otomatis")

st.markdown('<p style="text-align: center; margin: 1rem 0; color: #888888;">— ATAU —</p>', unsafe_allow_html=True)
st.markdown('<p class="box-header">Pilih Konsep Custom (Maksimal 8)</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
concept_names = ["Cerah", "Vintage Style", "Nature's Outdoor", "Cultural Mode", "Aesthetic Cafe", "Pop Color", "Cinematic", "Hasil Panen", "Storytelling", "Flatlay", "Editorial Style", "Close up",
                 "Premium Style", "Natural Indoor", "Dark and Moody", "Dapur Estetik", "Pastel Studio", "Frame Mockup", "Shadows", "Melayang", "UGC", "Gaya Katalog", "Ingredients Story", "Clean Look"]

checkbox_list = []
with col1:
    for name in concept_names[:12]:
        checkbox_list.append(st.checkbox(name))
with col2:
    for name in concept_names[12:]:
        checkbox_list.append(st.checkbox(name))

selected_concepts = [name for checked, name in zip(checkbox_list, concept_names) if checked]
st.markdown(f"<p style='font-size: 0.9rem; color: #666;'>Konsep terpilih: <b>{len(selected_concepts)} / 8</b></p>", unsafe_allow_html=True)

extra_props = st.text_input("Properti", placeholder="Contoh: daun mint", label_visibility="collapsed")
custom_generate = st.button("🎨 Hasilkan Konsep Custom")

st.markdown('<p class="box-header" style="margin-top: 2rem;">3. Hasil Visual</p>', unsafe_allow_html=True)

if auto_generate:
    if uploaded_file is not None:
        with st.spinner("Memproses 8 konsep visual otomatis..."):
            time.sleep(2)
        st.success("Berhasil!")
        c_res1, c_res2 = st.columns(2)
        for i in range(8):
            with (c_res1 if i % 2 == 0 else c_res2):
                st.image(uploaded_file, caption=f"Konsep Otomatis {i+1}", use_container_width=True)
                st.text_input("Edit gambar", placeholder="Instruksi edit...", key=f"auto_edit_{i}")
                b1, b2 = st.columns(2)
                with b1: st.button("🔄 Ulang", key=f"auto_re_{i}")
                with b2: st.button("⬇️ Unduh", key=f"auto_dl_{i}")
                st.button("📝 Buat Caption", key=f"auto_cap_{i}")
                st.button("🎬 Buat Prompt Video", key=f"auto_vid_{i}")
                st.markdown("---")
    else:
        st.warning("⚠️ Silakan unggah foto produk terlebih dahulu.")
elif custom_generate:
    if uploaded_file is not None and len(selected_concepts) > 0:
        if len(selected_concepts) > 8:
            st.error("⚠️ Maksimal hanya bisa memilih 8 gaya foto!")
        else:
            with st.spinner(f"Memproses {len(selected_concepts)} konsep pilihan..."):
                time.sleep(2)
            st.success("Berhasil!")
            c_res1, c_res2 = st.columns(2)
            for i, concept in enumerate(selected_concepts):
                with (c_res1 if i % 2 == 0 else c_res2):
                    st.image(uploaded_file, caption=concept, use_container_width=True)
                    st.text_input("Edit gambar", placeholder="Instruksi edit...", key=f"cust_edit_{i}")
                    b1, b2 = st.columns(2)
                    with b1: st.button("🔄 Ulang", key=f"cust_re_{i}")
                    with b2: st.button("⬇️ Unduh", key=f"cust_dl_{i}")
                    st.button("📝 Buat Caption", key=f"cust_cap_{i}")
                    st.button("🎬 Buat Prompt Video", key=f"cust_vid_{i}")
                    st.markdown("---")
    elif uploaded_file is None:
        st.warning("⚠️ Silakan unggah foto produk terlebih dahulu.")
    else:
        st.warning("⚠️ Silakan pilih setidaknya satu konsep custom.")
else:
    st.info("Hasil akan muncul di sini setelah Anda mengunggah foto dan menekan tombol 'Hasilkan'.")

st.markdown("---")
st.markdown("""
    <p style="text-align: center; font-size: 0.85rem; color: #888888; line-height: 1.5;">
    Dibuat oleh : <b>Ghina Tresna</b><br>
    Generator ini bersifat Personal Use Only. Tidak boleh disebarkan/dijual ulang tanpa izin 🙏.<br>
    OPEN PUBLIC AFFILIATE LEWAT LYNK, Search : Aesthetic Food Photo Generator - GT03
    </p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)st.markdown("""
    <p style="text-align: center; font-size: 0.85rem; color: #888888; line-height: 1.5;">
    Dibuat oleh : <b>Ghina Tresna</b><br>
    Generator ini bersifat Personal Use Only. Tidak boleh disebarkan tanpa izin 🙏.<br>
    OPEN PUBLIC AFFILIATE LEWAT LYNK : Aesthetic Food Photo Generator - GT03
    </p>
""", unsafe_allow_html=True)st.markdown("""
    <p style="text-align: center; font-size: 0.85rem; color: #888888; line-height: 1.5;">
    Dibuat oleh : <b>Ghina Tresna</b><br>
    Generator ini bersifat Personal Use Only. Tidak boleh disebarkan tanpa izin 🙏.<br>
    OPEN PUBLIC AFFILIATE LEWAT LYNK : Aesthetic Food Photo Generator - GT03
    </p>
""", unsafe_allow_html=True)
