import streamlit as st
import time

# Konfigurasi Halaman Web
st.set_page_config(page_title="Nhira Studio AI", page_icon="✨", layout="centered")

# CSS Kustom untuk Tampilan Estetik & Bersih
st.markdown("""
<style>
.stApp {
    background-color: #FAF6F0;
    background-image: linear-gradient(rgba(250, 246, 240, 0.90), rgba(250, 246, 240, 0.90)), 
                      url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
.main-title { font-size: 2.2rem; font-weight: bold; color: #1E3F20; text-align: center; margin-bottom: 0px; }
.sub-title { font-size: 1.0rem; color: #8C6D53; text-align: center; margin-bottom: 20px; }
.greeting-box { 
    background-color: #FFF2EE; 
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
    background-color: #FFFFFF;
    padding: 25px;
    border-radius: 15px;
    border: 1.5px solid #F5D6CB;
    margin-bottom: 30px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}
</style>
""", unsafe_allow_html=True)

# Header Utama
st.markdown('<p class="main-title">Nhira Studio AI ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">PRODUCT & FOOD PHOTO GENERATOR</p>', unsafe_allow_html=True)

# Sapaan Hangat & Islami
st.markdown("""
<div class="greeting-box">
Hai <i>Sisters</i> shalihah! Siapa bilang cari cuan harus selalu ninggalin rumah? Dari pojokan kamar sambil dasteran pun, kita tetap bisa jemput rezeki Allah. Semangat ya buat yang lagi ikhtiar hari ini! 🥺✨<br><br>
Eh tapi ingat, jangan keasyikan edit video sampai lupa jemuran di luar udah mateng terpanggang matahari ya, hehe. Selamat berkarya dan ikhtiar cari rezeki halal, semoga jadi tambahan rezeki yang barokah buat kita semua. Aamiin. 🥺✨
</div>
""", unsafe_allow_html=True)

# ==========================================
# A. FOTO PRODUK
# ==========================================
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### A. FOTO PRODUK <span style='font-size:0.8rem; color:#8C6D53;'>(Untuk Marketing, Promo, Konten Kreator)</span>", unsafe_allow_html=True)

col_p1, col_p2 = st.columns([1, 1])
with col_p1:
    st.markdown("##### 1. Unggah Foto Produk")
    prod_file = st.file_uploader("Format: PNG, JPG, atau WEBP", type=["jpg", "png", "jpeg", "webp"], key="prod")
    
    if prod_file is not None:
        st.success("✅ Foto produk berhasil diunggah!")
        st.image(prod_file, caption="Preview Foto Anda", width=200)
    
    st.markdown("##### Rasio Aspek (Opsional)")
    prod_ratio = st.radio("Pilih rasio produk:", ["Default", "1:1", "3:4", "9:16", "16:9"], horizontal=True, key="r_prod")
    
    st.markdown("##### Deskripsi Singkat Produk (Opsional)")
    prod_desc = st.text_input("Contoh: Botol serum vitamin C, kemasan 30ml", key="d_prod")

with col_p2:
    st.markdown("##### 2. Pilih Gaya Foto Produk <span style='font-size:0.75rem; color:#8C6D53;'>(Pilih maksimal 12)</span>", unsafe_allow_html=True)
    
    gp1, gp2, gp3, gp4 = st.columns(4)
    with gp1:
        p1 = st.checkbox("1. Minimalist", key="p1")
        p5 = st.checkbox("5. Floating", key="p5")
        p9 = st.checkbox("9. Clean White", key="p9")
    with gp2:
        p2 = st.checkbox("2. Luxury Marble", key="p2")
        p6 = st.checkbox("6. Beauty", key="p6")
        p10 = st.checkbox("10. Soft Pastel", key="p10")
    with gp3:
        p3 = st.checkbox("3. Premium", key="p3")
        p7 = st.checkbox("7. Glass Ref.", key="p7")
        p11 = st.checkbox("11. Lifestyle", key="p11")
    with gp4:
        p4 = st.checkbox("4. Catalog", key="p4")
        p8 = st.checkbox("8. Luxury Dark", key="p8")
        p12 = st.checkbox("12. Creative Adv", key="p12")

st.markdown("</div>", unsafe_allow_html=True)

# Tombol Eksekusi Produk
if st.button("✨ Hasilkan Foto Produk", use_container_width=True, key="btn_prod"):
    if prod_file is not None:
        with st.status("⏳ Memproses Foto Produk...", expanded=True) as status:
            time.sleep(1.5)
            status.update(label="🎉 Selesai!", state="complete", expanded=False)
        st.success("🎉 Foto produk berhasil diproses!")
    else:
        st.error("⚠️ Silakan unggah foto produk terlebih dahulu di Bagian A nomor 1!")


# ==========================================
# B. FOOD / KULINER
# ==========================================
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### B. FOOD / KULINER <span style='font-size:0.8rem; color:#8C6D53;'>(Untuk Promo, Konten Kreator, Bisnis Kuliner)</span>", unsafe_allow_html=True)

col_f1, col_f2 = st.columns([1, 1])
with col_f1:
    st.markdown("##### 1. Unggah Foto Makanan")
    food_file = st.file_uploader("Format: PNG, JPG, atau WEBP", type=["jpg", "png", "jpeg", "webp"], key="food")
    
    if food_file is not None:
        st.success("✅ Foto makanan berhasil diunggah!")
        st.image(food_file, caption="Preview Foto Makanan Anda", width=200)
        
    st.markdown("##### Rasio Aspek (Opsional)")
    food_ratio = st.radio("Pilih rasio makanan:", ["Default", "1:1", "3:4", "9:16", "16:9"], horizontal=True, key="r_food")
    
    st.markdown("##### Deskripsi Singkat Makanan (Opsional)")
    food_desc = st.text_input("Contoh: Nasi goreng spesial, level pedas 3", key="d_food")

with col_f2:
    st.markdown("##### 2. Pilih Gaya Foto Food Photography <span style='font-size:0.75rem; color:#8C6D53;'>(Pilih maksimal 12)</span>", unsafe_allow_html=True)
    
    gf1, gf2, gf3, gf4 = st.columns(4)
    with gf1:
        f1 = st.checkbox("1. Premium Cafe", key="f1")
        f5 = st.checkbox("5. Dark Moody", key="f5")
        f9 = st.checkbox("9. Steam Effect", key="f9")
    with gf2:
        f2 = st.checkbox("2. Flat Lay", key="f2")
        f6 = st.checkbox("6. Luxury Resto", key="f6")
        f10 = st.checkbox("10. Dessert Style", key="f10")
    with gf3:
        f3 = st.checkbox("3. Rustic Table", key="f3")
        f7 = st.checkbox("7. Korean Cafe", key="f7")
        f11 = st.checkbox("11. Street Food", key="f11")
    with gf4:
        f4 = st.checkbox("4. Natural Light", key="f4")
        f8 = st.checkbox("8. Japanese Min.", key="f8")
        f12 = st.checkbox("12. Menu Catalog", key="f12")

st.markdown("</div>", unsafe_allow_html=True)

# Tombol Eksekusi Food
if st.button("✨ Hasilkan Foto Food", use_container_width=True, key="btn_food"):
    if food_file is not None:
        with st.status("⏳ Memproses Foto Kuliner...", expanded=True) as status:
            time.sleep(1.5)
            status.update(label="🎉 Selesai!", state="complete", expanded=False)
        st.success("🎉 Foto kuliner berhasil diproses!")
    else:
        st.error("⚠️ Silakan unggah foto makanan terlebih dahulu di Bagian B nomor 1!")


# ==========================================
# C. HASIL VISUAL
# ==========================================
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("### C. HASIL VISUAL", unsafe_allow_html=True)
st.markdown("<p style='font-size:0.9rem; color:#8C6D53;'>Hasil & konsep visual siap digunakan.</p>", unsafe_allow_html=True)

st.info("🖼️ Hasil akan muncul di sini. Unggah gambar dan pilih gaya, lalu klik tombol 'Hasilkan' untuk memulai.")
st.markdown("</div>", unsafe_allow_html=True)


# Footer Motivasi Bawah
st.markdown("""
<div style="background-color: #FFF2EE; padding: 15px; border-radius: 10px; border: 1px solid #FFD1C7; text-align: center; color: #7A4F42; font-size: 0.85rem; margin-top: 30px;">
<b>KARYA KAMU, MASA DEPANMU.</b><br>
JADILAH EDITOR HEBAT, HIDUP LEBIH HEBAT. 🤍
</div>
""", unsafe_allow_html=True)
