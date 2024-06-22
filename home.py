
import streamlit as st


st.title("Selamat Datang di Detektor Paru-Paru Kami")

# Subtitle
st.subheader("Mengutamakan Kesehatan Paru-Paru Anda")

# Introduction
st.write("""
Detektor Paru-Paru kami didesain untuk membantu Anda memantau kesehatan paru-paru dengan mudah dan efektif. 
Dengan teknologi canggih berbasis AI, alat kami dapat mendeteksi berbagai masalah kesehatan paru-paru secara cepat dan akurat.
""")

# Title of the homepage
st.title("Informasi Penyakit Paru-Paru")

# Section for Pneumonia
st.header("Pneumonia")
st.write("""
Pneumonia adalah infeksi yang menyebabkan peradangan pada kantung udara di satu atau kedua paru-paru. 
Kantung udara dapat terisi dengan cairan atau nanah, menyebabkan batuk berdahak atau nanah, demam, menggigil, dan kesulitan bernapas.
""")
st.subheader("Pencegahan")
st.write("""
- Vaksinasi
- Menjaga kebersihan tangan
- Menghindari merokok
- Menjaga sistem kekebalan tubuh
""")
st.image("image\pneumonia.jpeg", caption="Gambar paru-paru dengan pneumonia")

# Section for Tuberculosis
st.header("Tuberculosis (TBC)")
st.write("""
Tuberculosis adalah penyakit menular yang disebabkan oleh bakteri Mycobacterium tuberculosis. 
TBC biasanya menyerang paru-paru, tetapi juga dapat mempengaruhi bagian tubuh lainnya.
""")
st.subheader("Pencegahan")
st.write("""
- Vaksinasi BCG
- Menjaga kebersihan diri
- Menghindari kontak dengan penderita TBC aktif
- Menjaga sistem kekebalan tubuh
""")
st.image("image\ptubercullosis.jpeg", caption="Gambar paru-paru dengan tuberculosis")

# Section for Normal Lungs
st.header("Paru-Paru Normal")
st.write("""
Paru-paru normal adalah paru-paru yang sehat tanpa adanya infeksi atau penyakit. 
Paru-paru ini berfungsi dengan baik dalam pertukaran oksigen dan karbon dioksida.
""")
st.subheader("Pencegahan Penyakit Paru-Paru")
st.write("""
- Tidak merokok
- Menghindari polusi udara
- Berolahraga secara teratur
- Menjaga pola makan sehat
""")
st.image("image\sehat.jpeg", caption="Gambar paru-paru normal")

# Footer
st.write("Informasi ini disediakan untuk tujuan edukasi dan bukan sebagai pengganti nasihat medis profesional.")
