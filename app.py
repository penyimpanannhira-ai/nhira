
)
import streamlit as st
import time

st.set_page_config(page_title="Nhira Studio AI", layout="centered")

st.markdown("""
<style>
.stApp { background-color: #FFF8F0; }
h1, h2, h3, h4, h5, h6, p, label, .stCheckbox label { color: #4A4A4A; }
.main-container { background-color: #FFFFFF; padding: 2rem; border-radius: 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.05); margin-bottom: 2rem; }
.big-title { font-size: 2.2rem; font-weight: 800; color: #2D2D2D; text-align: center; margin-bottom: 0.5rem; }
.sub-title { font-size: 1.05rem; color: #666666; text-align: center; margin-bottom: 2rem; }
.tutorial-box { background-color: #FFFD0; border: 2px dashed #FFD166; border-radius: 15px; padding: 1.5rem; margin-bottom: 2rem; }
.box-header { font-size: 1.2rem; font-weight: 700; color: #D4A373; margin-bottom: 1rem; }
div.stButton > button { background-color: #FFB5A7; color: white; font-weight: 600; border-radius: 10px; border: none; }
div.stButton > button:hover { background-color: #F89690; color: white; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<p class="big-title">Aesthetic Food Photo Generator by Nhira Studio AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Ubah foto makanan-mu menjadi estetik! Maksimal 3 gaya foto dari 1 kali unggah.</p>', unsafe_allow_html=True)

st.markdown("""
<div class="tutorial-box">
    <p style="font-size: 1.2rem; font-weight: 700; color: #D4A373; margin-bottom: 0.8rem;">✨ Tutorial Singkat:</p>
    <ol style="font-size: 0.95rem; line-height: 1.6; color: #555555;">
        <li>Unggah foto produk makanan atau minuman.</li>
        <li>Pilih mode "Hasilkan 3 Konsep Visual Otomatis", atau pilih maksimal 3 konsep di mode custom.</li>
        <li>Tunggu proses selesai hingga hasil foto dan tombol aksi muncul.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="box-header">1. Unggah Foto Produk</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=['png', 'jpg', 'webp'])
aspect_ratio = st.radio("Rasio Aspek", ("Default", "1:1", "3:4", "9:16", "16:9"), label_visibility="collapsed")
product_description = st.text_input("Deskripsi", placeholder="Contoh: Jus Mangga", label_visibility="collapsed")

st.markdown('<p class="box-header" style="margin-top: 2rem;">2. Pilih Mode Generate</p>', unsafe_allow_html=True)
auto_generate = st.button("✨ Hasilkan 3 Konsep Visual Otomatis")

st.markdown('<p style="text-align: center; margin: 1rem 0; color: #888888;">>-- ATAU --<</p>', unsafe_allow_html=True)
st.markdown('<p class="box-header">Pilih Konsep Custom (Maksimal 3)</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
concept_names = ["Cerah", "Vintage Style", "Nature's Outdoor"]

checkbox_list = []
with col1:
    checkbox_list.append(st.checkbox(concept_names[0]))
with col2:
    checkbox_list.append(st.checkbox(concept_names[1]))
with col3:
    checkbox_list.append(st.checkbox(concept_names[2]))

selected_concepts = [name for checked, name in zip(checkbox_list, concept_names) if checked]
st.markdown(f'<p style="font-size: 0.9rem; color: #666;">Konsep terpilih: <b>{len(selected_concepts)} / 3</b></p>', unsafe_allow_html=True)

extra_props = st.text_input("Properti", placeholder="Contoh: daun mint", label_visibility="collapsed")
custom_generate = st.button("🎨 Hasilkan Konsep Custom")
st.markdown('<p class="box-header" style="margin-top: 2rem;">3. Hasil Visual</p>', unsafe_allow_html=True)

if auto_generate:
    if uploaded_file is not None:
        with st.spinner("Memproses 3 konsep visual otomatis..."):
            time.sleep(2)
        st.success("Berhasil!")
        c_res1, c_res2, c_res3 = st.columns(3)
        for i in range(3):
            target_col = c_res1 if i == 0 else (c_res2 if i == 1 else c_res3)
            with target_col:
                st.image(uploaded_file, caption=f"Konsep Otomatis {i+1}", use_container_width=True)
                st.text_input("Edit gambar", placeholder="Instruksi edit...", key=f"auto_edit_{i}")
                st.button("🔄 Ulang", key=f"auto_re_{i}")
                st.button("⬇️ Unduh", key=f"auto_dl_{i}")
                st.button("📝 Buat Caption", key=f"auto_cap_{i}")
                st.button("🎬 Buat Prompt Video", key=f"auto_vid_{i}")
                st.markdown("---")
    else:
        st.warning("⚠️ Silakan unggah foto produk terlebih dahulu.")
elif custom_generate:
    if uploaded_file is not None and len(selected_concepts) > 0:
        if len(selected_concepts) > 3:
            st.error("⚠️ Maksimal hanya bisa memilih 3 gaya foto!")
        else:
            with st.spinner(f"Memproses {len(selected_concepts)} konsep pilihan..."):
                time.sleep(2)
            st.success("Berhasil!")
            c_res1, c_res2, c_res3 = st.columns(3)
            for i, concept in enumerate(selected_concepts):
                target_col = c_res1 if i % 3 == 0 else (c_res2 if i % 3 == 1 else c_res3)
                with target_col:
                    st.image(uploaded_file, caption=concept, use_container_width=True)
                    st.text_input("Edit gambar", placeholder="Instruksi edit...", key=f"cust_edit_{i}")
                    st.button("🔄 Ulang", key=f"cust_re_{i}")
                    st.button("⬇️ Unduh", key=f"cust_dl_{i}")
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
Dibuat oleh : <b>Nhira Studio</b><br>
HARAM menyebarkan link ini tanpa izin 🚫
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
