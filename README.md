# Proyek Analisis Bike Sharing

## 1. Pendahuluan

Proyek ini bertujuan untuk menganalisis data Bike Sharing dari Washington D.C. dengan menggabungkan data harian dan data per jam. Analisis ini mencakup seluruh proses mulai dari data cleaning, merging, eksplorasi data (EDA) hingga analisis lanjutan (misalnya, clustering manual) untuk menjawab beberapa pertanyaan bisnis, seperti:

- **Bagaimana tren penyewaan sepeda berubah seiring waktu?**
- **Bagaimana pengaruh faktor waktu (jam) terhadap jumlah penyewaan?**
- **Bagaimana pengaruh kondisi musim dan suhu terhadap penyewaan?***
- **Apakah terdapat perbedaan pola antara hari kerja (weekdays) dan akhir pekan (weekend)?**


## 2. Dataset

- **Dataset**: Bike Sharing Dataset
- **Periode**: 2011 - 2012
- **Jumlah Baris**: 17.379
- **Jumlah Kolom**: 21
- **Kolom Penting**: dateday, season, month, hour, daily_cnt, hourly_count, temp, temp_category, category_days, dll.
- **Catatan**: Data telah melalui proses pembersihan dan transformasi, termasuk konversi nilai temp ke Celsius (dengan perkalian 41) dan pembentukan kategori suhu (temp_category).


## 3. Struktur Proyek

Submission Proyek Analisis Data:

├── Bike-sharing-dataset

│   ├── clean_merged.csv

│   ├── day.csv

│   ├── hour.csv

│   ├── merged.csv

│   └── Readme.txt

├── dashboard

│   └── dashboard.py

├── notebook.ipynb

├── preview_dashboard.png

├── README.md

└── requirements.txt

└── url.txt


## 4. Setup Environment & Instalasi Library

### 4.1. Membuat Virtual Environment (Opsional)
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

### 4.2. Instalasi Library
Pastikan kamu sudah menginstal semua library yang dibutuhkan dengan menjalankan perintah:
```
pip install -r requirements.txt
```

Pastikan file requirements.txt mencakup paket-paket seperti pandas, numpy, matplotlib, seaborn, dan streamlit.


## 5. Proses Data Cleaning & Merging

Proyek ini meliputi beberapa tahap:
- Memuat Data: Membaca file day.csv dan hour.csv menggunakan pandas.
- Merging Data: Menggabungkan data per jam dan data harian untuk menghasilkan kolom daily_cnt (total penyewaan harian).
- Data Cleaning:
  - Menghapus kolom yang tidak relevan (misalnya: instant, workingday).
  - Melakukan scaling pada kolom bernilai ternormalisasi (misalnya, temp, atemp, humidity, windspeed) untuk mengembalikan ke skala aslinya.
  - Mengonversi kode numerik di kolom seperti season, month, weather_category, weekday, dan year menjadi label deskriptif.
  - Menambahkan kolom kategori seperti category_days, humidity_category, dan temp_category (dengan interval suhu yang sesuai).

Lihat kode lengkap di dalam notebook.ipynb untuk detail setiap langkah.

Insight:

Data yang telah dibersihkan dan digabungkan memudahkan analisis lebih mendalam karena:
- Data konsisten dan siap digunakan.
- Informasi agregat harian dan per jam tersedia dalam satu tabel.
- Data numerik sudah dikembalikan ke skala aslinya sehingga lebih mudah diinterpretasikan.


## 6. Exploratory Data Analysis (EDA)
Pada tahap EDA, dilakukan analisis untuk menjawab pertanyaan bisnis utama:
**Pertanyaan Bisnis & Visualisasi Utama**

- Tren Penyewaan Sepeda:
  - Pertanyaan: Bagaimana tren penyewaan sepeda berubah seiring waktu?
  - Visualisasi: Line plot antara dateday dan daily_cnt.
  - Insight: Terlihat pola musiman dengan peningkatan di musim panas dan penurunan di musim dingin.

- Pengaruh Waktu (Jam):
  - Pertanyaan: Bagaimana pengaruh faktor waktu terhadap penyewaan?
  - Visualisasi: Bar plot rata-rata penyewaan (hourly_count) per jam.
  - Insight: Puncak penyewaan terjadi pada pagi dan sore hari (jam sibuk).

- Pengaruh Musim & Suhu:
  - Pertanyaan: Bagaimana pengaruh musim dan suhu terhadap penyewaan?
  - Visualisasi:
    - Bar plot rata-rata penyewaan per musim (season).
    - Bar plot rata-rata penyewaan berdasarkan kategori suhu (temp_category) yang telah dikonversi ke Celsius.
  - Insight: Penyewaan lebih tinggi di musim tertentu (misalnya, Fall) dan pada kategori suhu yang hangat/panas.

- Perbandingan Weekdays vs Weekend:
  - Pertanyaan: Apakah terdapat perbedaan pola antara hari kerja dan akhir pekan?
  - Visualisasi: Bar plot perbandingan daily_cnt berdasarkan category_days.
  - Insight: Meskipun pada dataset ini weekdays sedikit lebih tinggi, pola penggunaan antara hari kerja dan akhir pekan menunjukkan karakteristik yang berbeda.

Lihat kode lengkap EDA di dalam notebook.ipynb.


## 7. Dashboard Interaktif dengan Streamlit

https://joanneeldy-proyekdata.streamlit.app/

Dashboard interaktif dibuat untuk menyampaikan hasil analisis secara visual dan dinamis. Fitur utama dashboard:
- Data Preview: Menampilkan contoh data yang telah dibersihkan.
- Filter Interaktif: Sidebar untuk memilih rentang tanggal dan parameter lain jika diperlukan.
- Visualisasi Dinamis: Menampilkan grafik tren harian, rata-rata penyewaan per jam, distribusi penyewaan per musim, kategori suhu, dan perbandingan hari kerja vs weekend.
- Analisis Lanjutan: Misalnya, clustering manual (binned grouping) untuk mengelompokkan hari berdasarkan total penyewaan (daily_cnt).

Cara Menjalankan Dashboard Secara Lokal:
- Pastikan virtual environment aktif (jika digunakan) dan semua library telah terinstal.
- Buka terminal dan arahkan ke direktori proyek.
- Jalankan perintah berikut:
```
streamlit run dashboard/dashboard.py
```
Dashboard akan terbuka di browser secara otomatis.


## 8. Analisis Lanjutan (Advanced Analysis)

Selain EDA utama, proyek ini juga menerapkan teknik analisis lanjutan, antara lain:
- Clustering Manual (Binning):
  Mengelompokkan hari berdasarkan total penyewaan (daily_cnt) ke dalam kategori:
  - Low Usage, Medium Usage, High Usage
    (Analisis ini membantu mengidentifikasi hari-hari dengan performa rendah hingga tinggi.)

- Catatan:
  - RFM Analysis: Tidak diterapkan karena dataset tidak memiliki data transaksi per pelanggan.
  - Geospatial Analysis: Tidak diterapkan karena tidak ada informasi lokasi.


## 9. Template Notebook

Notebook (notebook.ipynb) telah disesuaikan dengan template yang disediakan, yang mencakup:
- Header: Judul proyek dan informasi singkat.
- Tahap-tahap Analisis: Data Gathering, Data Cleaning & Merging, EDA, dan Insight.
- Markdown Cells: Berisi penjelasan dan insight dari setiap tahap.
- Komentar pada Kode: Untuk memudahkan pemahaman langkah-langkah analisis.


## 10. Referensi dan Panduan
- Markdown Cheat Sheet – How to Write in Markdown with Examples
- Dokumentasi library yang digunakan (pandas, matplotlib, seaborn, streamlit).
- Contoh dan panduan visualisasi dari materi latihan sebelumnya.

## 11. Kesimpulan

Proyek ini berhasil mengungkap insight penting dari data Bike Sharing, antara lain:
- Tren penyewaan dipengaruhi oleh faktor waktu, musim, dan suhu.
- Penyewaan lebih tinggi pada jam sibuk dan di kategori suhu yang hangat/panas.
- Meskipun terdapat perbedaan antara hari kerja dan akhir pekan, data menunjukkan peran penting dari penggunaan sepeda dalam aktivitas komuter.
- Analisis lanjutan melalui clustering manual membantu mengidentifikasi hari-hari dengan performa rendah hingga tinggi, yang bisa dijadikan dasar strategi operasional.

Insight ini dapat digunakan untuk pengambilan keputusan strategis, seperti penyesuaian armada, promosi khusus, dan perencanaan layanan.


## 12. Cara Menjalankan Proyek

- Notebook: Buka dan jalankan notebook.ipynb untuk mereproduksi seluruh proses analisis data mulai dari data cleaning hingga advanced analysis.
- Dashboard: Jalankan perintah berikut di terminal:
```
streamlit run dashboard/dashboard.py
```
- Dataset: Pastikan file dataset asli dan file data bersih  (clean_merged.csv) berada di folder data.
