# 📊 Proyek Analisis Data: Bike Sharing Dataset

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis pola penggunaan layanan bike sharing berdasarkan faktor waktu dan kondisi lingkungan. Dataset yang digunakan terdiri dari data harian (day.csv) dan data per jam (hour.csv).

Analisis dilakukan melalui tahapan:

- Data Wrangling (Assessing & Cleaning)
- Exploratory Data Analysis (EDA)
- Visualisasi data menggunakan Streamlit

Hasil analisis diharapkan dapat memberikan insight terkait pola penggunaan sepeda untuk mendukung pengambilan keputusan.

---

## 🎯 Pertanyaan Bisnis

1. Bagaimana tren jumlah peminjaman sepeda berdasarkan waktu (harian dan per jam)?
2. Bagaimana pengaruh kondisi cuaca terhadap jumlah peminjaman sepeda?
3. Pada jam berapa terjadi puncak penggunaan layanan bike sharing?

---

## 📂 Dataset

Dataset yang digunakan:

- day.csv → Data agregasi harian
- hour.csv → Data agregasi per jam

Fitur utama:

- dteday → tanggal
- season → musim
- weathersit → kondisi cuaca
- temp, atemp → suhu
- hum → kelembaban
- windspeed → kecepatan angin
- cnt → total peminjaman

---

## 🛠️ Tools & Library

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

---

## ⚙️ Setup Environment

### 1. Clone Repository

git clone <link-repository>
cd submission-bike-sharing

### 2. Membuat Virtual Environment

python -m venv venv

### 3. Aktivasi Virtual Environment

Windows (PowerShell):
.\venv\Scripts\Activate

Windows (CMD):
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

## 📦 Install Dependencies

pip install -r requirements.txt

---

## ▶️ Menjalankan Notebook

Buka file notebook.ipynb lalu jalankan seluruh cell untuk:

1. Assessing Data
2. Cleaning Data
3. EDA
4. Simpan data bersih:
   df.to_csv("data/clean_data.csv", index=False)

---

## 🚀 Menjalankan Dashboard Streamlit

streamlit run dashboard/dashboard.py

Akses melalui browser:
http://localhost:8501

---

## 📊 Insight Utama

- Peminjaman sepeda meningkat pada jam sibuk (pagi dan sore)
- Kondisi cuaca cerah meningkatkan jumlah peminjaman
- Terdapat perbedaan pola penggunaan antara hari kerja dan akhir pekan

---

## 📌 Catatan Penting

- Dashboard menggunakan data hasil cleaning (clean_data.csv)
- Pastikan proses cleaning selesai sebelum menjalankan dashboard
- Gunakan dataframe yang sama secara konsisten dalam seluruh analisis

---

## ✨ Author

Proyek ini dibuat untuk memenuhi submission Proyek Analisis Data.
