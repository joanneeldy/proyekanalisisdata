# Proyek Analisis Bike Sharing

## 1. Pendahuluan

Proyek ini bertujuan untuk menganalisis data Bike Sharing dari Washington D.C. dengan menggabungkan data harian (`day.csv`) dan data per jam (`hour.csv`). Analisis ini mencakup proses data cleaning, merging, dan eksplorasi data (EDA) untuk menjawab beberapa pertanyaan bisnis, antara lain:
- **Bagaimana tren penyewaan sepeda berubah seiring waktu?**
- **Bagaimana pengaruh faktor waktu (jam) terhadap jumlah penyewaan?**
- **Bagaimana pengaruh kondisi musim (season) terhadap penyewaan?**
- **Bagaimana pengaruh kelembapan (humidity) terhadap penyewaan?**
- **Apakah terdapat perbedaan pola antara hari kerja (weekdays) dan akhir pekan (weekend)?**

## 2. Struktur Proyek

Submission Proyek Analisis Data
├── Bike-sharing-dataset
│   ├── day.csv
│   ├── hour.csv
│   ├── merged.csv
│   ├── clean_merged.csv
├── dashboard
│   └── dashboard.py
├── notebook.ipynb
├── README.md
└── requirements.txt


## 3. Setup Environment & Instalasi Library

### 3.1. Membuat Virtual Environment (Opsional)
Disarankan untuk membuat virtual environment agar dependency proyek tidak tercampur dengan paket lainnya.
Contoh menggunakan **venv**:
```bash
python -m venv venv
```
Aktifkan virtual environment:
- Windows:
  ```
  venv\Scripts\activate
  ```
- Mac/Linux:
  ```
  source venv/bin/activate
  ```

### 3.2. Instalasi Library
Pastikan kamu sudah menginstal semua library yang dibutuhkan dengan menjalankan perintah:
```
pip install -r requirements.txt
```
Untuk mengecek versi library yang digunakan, kamu bisa menggunakan:
```
pip freeze > requirements.txt
```

### 4. Proses Data Cleaning & Merging

Proyek ini meliputi beberapa tahap utama:
- Memuat Data: Membaca file day.csv dan hour.csv menggunakan pandas.
- Merging Data: Menggabungkan data per jam dan data harian agar didapatkan kolom daily_cnt yang menunjukkan total penyewaan harian.
- Data Cleaning:
    -> Menghapus kolom yang tidak relevan seperti instant dan workingday.
    -> Melakukan scaling pada kolom bernilai ternormalisasi (temp, atemp, humidity, windspeed) untuk mengembalikan ke skala aslinya.
    -> Mengkonversi kode numerik di kolom-kolom seperti season, month, weather_category, weekday, dan year menjadi label deskriptif.
    -> Menambahkan kolom kategori (misal: category_days dan humidity_category).
Lihat kode lengkap di dalam notebook.ipynb untuk detail setiap langkah.

Insight dari Tahap Ini:
Data yang telah dibersihkan dan digabungkan memudahkan analisis lebih mendalam karena:
- Semua data sudah konsisten dan siap digunakan.
- Informasi agregat harian dan per jam tersedia dalam satu tabel.
- Data numerik sudah dikembalikan ke skala aslinya sehingga lebih mudah diinterpretasikan.

### 5. Exploratory Data Analysis (EDA)
Pada tahap EDA, dilakukan analisis untuk menjawab pertanyaan bisnis utama:

Tren Penyewaan Sepeda:

Pertanyaan: Bagaimana tren penyewaan sepeda berubah seiring waktu?
Visualisasi: Line plot antara dateday dan daily_cnt.
Insight: Terlihat pola musiman, seperti peningkatan penyewaan pada musim panas dan penurunan pada musim dingin.

Pertanyaan: Bagaimana pengaruh faktor waktu (jam) terhadap penyewaan?
Visualisasi: Bar plot rata-rata penyewaan (hourly_count) per jam berdasarkan kolom hr.
Insight: Jam-jam tertentu (misalnya pagi dan sore) menunjukkan puncak penyewaan, menandakan jam sibuk.

Pertanyaan: Bagaimana pengaruh kondisi musim terhadap penyewaan?
Visualisasi: Box plot penyewaan per jam berdasarkan season.
Insight: Distribusi penyewaan berbeda secara signifikan antar musim.

Pertanyaan: Bagaimana pengaruh suhu terhadap penyewaan?
Visualisasi: Bar plot berdasarkan kategori suhu (temp).
Insight: Kondisi suhu ideal cenderung meningkatkan jumlah penyewaan.

Pertanyaan: Apakah terdapat perbedaan pola penyewaan antara weekdays dan weekend?
Visualisasi: Box plot perbandingan penyewaan berdasarkan category_days.
Insight: Terlihat perbedaan pola penyewaan antara hari kerja dan akhir pekan.

Lihat kode lengkap EDA di dalam notebook.ipynb.

### 6. Dashboard Interaktif dengan Streamlit

Dashboard interaktif memungkinkan pengguna untuk mengeksplorasi data dengan filter (misalnya, rentang tanggal dan tahun).

Fitur Utama Dashboard:
- Data Preview: Menampilkan contoh data bersih.
- Filter Interaktif: Sidebar untuk memilih rentang tanggal dan tahun.
- Visualisasi Dinamis: Grafik tren penyewaan, rata-rata penyewaan per jam, dan distribusi penyewaan berdasarkan musim yang diperbarui sesuai filter.
- Insight Langsung: Menampilkan total penyewaan berdasarkan data yang difilter.

Cara Menjalankan Dashboard Secara Lokal:
Pastikan virtual environment aktif (jika digunakan) dan semua library telah terinstal.
Buka terminal dan arahkan ke direktori proyek.
Jalankan perintah berikut:
```streamlit run dashboard/dashboard.py
```
Dashboard akan terbuka di browser secara otomatis.

### 7. Template Notebook

Pastikan notebook (notebook.ipynb) telah disesuaikan dengan template yang disediakan, yang mencakup:

Header: Judul proyek dan informasi singkat.
Tahap-tahap Analisis: Data Gathering, Data Cleaning & Merging, EDA, dan Insight.
Markdown Cells: Berisi penjelasan dan insight dari setiap tahap.
Komentar pada Kode: Untuk memudahkan pemahaman langkah-langkah analisis.

### 8. Referensi dan Panduan

Markdown Cheat Sheet – How to Write in Markdown with Examples
Dokumentasi library yang digunakan (pandas, matplotlib, seaborn, streamlit).

### 9. Kesimpulan

Proyek ini telah mengungkap insight penting dari data Bike Sharing, termasuk tren penyewaan berdasarkan waktu, pengaruh musim dan kelembapan, serta perbedaan antara hari kerja dan weekend. Insight ini dapat digunakan sebagai dasar untuk pengambilan keputusan operasional dan perencanaan strategi di sistem Bike Sharing.

### 10. Cara Menjalankan Proyek

Notebook: Buka dan jalankan notebook.ipynb untuk mereproduksi proses data cleaning, merging, dan EDA.
Dashboard: Jalankan perintah berikut di terminal:
```streamlit run dashboard/dashboard.py
```
Dataset: Pastikan file dataset asli dan file data bersih berada di folder data.
