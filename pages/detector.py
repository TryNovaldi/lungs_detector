import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Title
st.title("Selamat Datang di Aplikasi Detektor Paru-Paru Kami")

# Introduction
st.write("""
Solusi modern untuk memantau kesehatan Anda. Aplikasi kami menggunakan algoritma AI canggih untuk mendeteksi berbagai penyakit dengan cepat, memberikan Anda informasi penting untuk menjaga kesehatan dengan lebih baik.
""")


# Load h5 model
model = keras.models.load_model('model.h5')

# Load Labels
with open('labels.txt', 'r') as f:
    labels = f.read().split('\n')

# Input Image
uploaded_file = st.file_uploader("Periksa paru-paru anda", type=('png','jpg','jpeg'))
if uploaded_file is not None:
    # Read and preprocess image
    image = tf.io.decode_image(uploaded_file.getvalue(), channels=3)
    image = tf.image.resize(image, [224, 224])
    image = tf.expand_dims(image, axis=0)
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
     
    st.image(uploaded_file, caption='Proses', use_column_width=True)

    # Predict
    prediction = model.predict(image)
    predicted_class = labels[np.argmax(prediction)]
    confidence = np.max(prediction) * 100
    
    st.write(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}%")
