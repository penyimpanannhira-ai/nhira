import streamlit as st
import time

# Konfigurasi Halaman Web
st.set_page_config(page_title="Nhira Studio AI - Kuliner", page_icon="🍽️", layout="centered")

# CSS Kustom: Background Gambar Pilihan Anda & Desain Bersih
st.markdown("""
<style>
.stApp {
    background-image: linear-gradient(rgba(250, 246, 240, 0.90), rgba(250, 246, 240, 0.90)), 
                      url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
.main-title { font-size: 2.2rem; font-weight: bold; color: #1E3F20; text-align: center; margin-bottom: 0px; }
.sub-title { font-size: 1.0rem; color: #8C6D53; text-align: center; margin-bottom: 20px; }
.greeting-box { 
    background-color: rgba(255, 242, 238, 0.95); 
    padding: 15px 20px; 
    border-radius: 12px; 
    border: 1.5px solid #FFD1C7; 
    color: #7A4F42; 
    font-size: 0.95rem; 
    text-align: center; 
    margin-bottom: 25px; 
    line-height: 1.5; 
}
.section-box {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 25px;
    border-radius: 15px;
    border: 1.5px solid #F5D6CB;
    margin-bottom: 30px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}
.style-card {
    background: #FFFFFF;
    border: 1px solid #E5D0C5;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 15px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Header Utama
st.markdown('<p class="main-title">Nhira Studio AI ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">FOOD / KULINER PHOTO GENERATOR</p>', unsafe_allow_html=True)

# Sapaan Hangat & Islami
st.markdown("""
<div class="greeting-box">
Hai <i>Sisters</i> shalihah! Bisnis kuliner makin moncer dengan foto estetik. Yuk, sulap foto makanan Anda jadi menggugah selera dalam satu klik. Semangat jemput rezeki halal hari ini! 🥺✨
</div>
""", unsafe_allow_html=True)

# ==========================================
# B. FOOD / KULINER
# ==========================================
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### B. FOOD / KULINER <span style='font-size:0.8rem; color:#8C6D53;'>(Untuk Konten Kreator & Bisnis Kuliner)</span>", unsafe_allow_html=True)

# 1. Unggah Foto Makanan
st.markdown("##### 1. Unggah Foto Makanan")
food_file = st.file_uploader("Format: PNG, JPG, atau WEBP", type=["jpg", "png", "jpeg", "webp"], key="food")

if food_file is not None:
    st.success("✅ Foto makanan berhasil diunggah!")
    st.image(food_file, caption="Preview Foto Makanan Anda", width=220)

st.write("---")

# Rasio Aspek
st.markdown("##### Rasio Aspek (Opsional)")
food_ratio = st.radio("Pilih rasio makanan:", ["Default", "1:1", "3:4", "9:16", "16:9"], horizontal=True, key="r_food")

st.write("---")

# Deskripsi Singkat
st.markdown("##### Deskripsi Singkat Makanan (Opsional)")
food_desc = st.text_input("Contoh: Nasi goreng spesial, level pedas 3", key="d_food")

st.write("---")

# 2. Pilih Gaya Foto Food Photography dengan Tombol Aksi Lengkap
st.markdown("##### 2. Pilih Gaya Foto Food Photography <span style='font-size:0.75rem; color:#8C6D53;'>(Pilih gaya & gunakan tombol aksi di bawahnya)</span>", unsafe_allow_html=True)

# Daftar 12 Gaya Kuliner
gaya_list = [
    "1. Premium Cafe", "2. Flat Lay", "3. Rustic Table", "4. Natural Light",
    "5. Dark Moody", "6. Luxury Resto", "7. Korean Cafe", "8. Japanese Min.",
    "9. Steam Effect", "10. Dessert Style", "11. Street Food", "12. Menu Catalog"
]

# Membuat grid 3 kolom untuk menampilkan gaya beserta tombol aksinya
cols = st.columns(3)
for idx, gaya in enumerate(gaya_list):
    col_target = cols[idx % 3]
    with col_target:
        st.markdown(f'<div class="style-card"><b>{gaya}</b>', unsafe_allow_html=True)
        st.checkbox("Pilih Gaya Ini", key=f"chk_f_{idx}")
        
        # Tombol-tombol aksi kecil di bawah foto/gaya
        b1, b2 = st.columns(2)
        with b1:
            if st.button("📥 Download", key=f"dl_f_{idx}", use_container_width=True):
                st.toast(f"Mengunduh hasil {gaya}...")
            if st.button("🎥 Prompt Video", key=f"pv_f_{idx}", use_container_width=True):
                st.toast(f"Membuat prompt video untuk {gaya}...")
        with b2:
            if st.button("🔄 Ulang", key=f"un_f_{idx}", use_container_width=True):
                st.toast(f"Mengulang proses {gaya}...")
            if st.button("💬 Caption", key=f"cp_f_{idx}", use_container_width=True):
                st.toast(f"Membuat caption untuk {gaya}...")
                
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Tombol Eksekusi Utama Food
if st.button("✨ Hasilkan Foto Food", use_container_width=True, key="btn_food"):
    if food_file is not None:
        with st.status("⏳ Memproses Foto Kuliner...", expanded=True) as status:
            time.sleep(1.5)
            status.update(label="🎉 Selesai!", state="complete", expanded=False)
        st.success("🎉 Foto kuliner berhasil diproses!")
    else:
        st.error("⚠️ Silakan unggah foto makanan terlebih dahulu di nomor 1!")

# Footer Motivasi Bawah
st.markdown("""
<div style="background-color: rgba(255, 242, 238, 0.95); padding: 15px; border-radius: 10px; border: 1px solid #FFD1C7; text-align: center; color: #7A4F42; font-size: 0.85rem; margin-top: 30px;">
<b>KARYA KAMU, MASA DEPANMU.</b><br>
JADILAH EDITOR HEBAT, HIDUP LEBIH HEBAT. 🤍
</div>
""", unsafe_allow_html=True)
