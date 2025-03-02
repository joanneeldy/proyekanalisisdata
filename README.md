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


## 3. Proses Data Cleaning & Merging

### 3.1. Memuat Data dan Konversi Tanggal

Kita mulai dengan membaca file CSV dan mengkonversi kolom tanggal (`dteday`) ke tipe datetime.

```python
import pandas as pd

# Membaca data asli
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

# Konversi kolom tanggal menjadi datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
```

### 3.2. Merging Data

```
# Buat subset dari day_df
day_subset = day_df[['dteday', 'cnt']].copy()
day_subset.rename(columns={'cnt': 'daily_cnt'}, inplace=True)

# Merge data per jam (hour_df) dengan data harian (day_subset)
merged_df = pd.merge(hour_df, day_subset, on='dteday', how='left')

# Simpan hasil merge untuk referensi
merged_df.to_csv('data/merged_bike_sharing.csv', index=False)
```

### 3.3. Data Cleaning
- Merename Kolom: Menjadikan nama kolom lebih deskriptif.
- Hapus Kolom Redundan: Menghapus kolom instant (hanya penomoran) dan workingday (jika sudah tergantikan oleh weekday).
- Scaling Nilai: Mengembalikan nilai ternormalisasi ke skala aslinya.
- Konversi Kategorikal: Mengubah nilai numerik pada kolom seperti season, month, weather_category, weekday, dan year ke label yang lebih mudah dipahami.
- Menambahkan Kolom Kategori: Misalnya, category_days (weekend vs weekdays) dan humidity_category.

### 4. Exploratory Data Analysis (EDA)
Pertanyaan Bisnis yang Dijawab:

Bagaimana tren penyewaan sepeda berubah seiring waktu?
Visualisasi: Line plot tren harian berdasarkan kolom daily_cnt vs. dateday.

Bagaimana pengaruh faktor waktu (jam) terhadap penyewaan?
Visualisasi: Bar plot rata-rata penyewaan per jam (hourly_count) berdasarkan kolom hr.

Bagaimana pengaruh kondisi musim (season) terhadap penyewaan?
Visualisasi: Box plot penyewaan per jam berdasarkan season.

Bagaimana pengaruh kelembapan terhadap penyewaan?
Visualisasi: Bar plot rata-rata penyewaan berdasarkan kategori kelembapan (humidity_category).

Apakah terdapat perbedaan pola antara hari kerja dan weekend?
Visualisasi: Box plot perbandingan penyewaan antara weekdays dan weekend (dari kolom category_days).

# Insight Utama yang Ditemukan:

Tren Penyewaan per Hari:
Terdapat pola musiman; penyewaan cenderung naik pada musim tertentu (misalnya, musim panas) dan turun pada musim dingin.

Penyewaan per Jam:
Jam-jam sibuk (seperti pagi dan sore) menunjukkan rata-rata penyewaan tertinggi.

Pengaruh Musim:
Distribusi penyewaan bervariasi antara musim, yang dapat membantu dalam perencanaan operasional dan penambahan armada.

Pengaruh Kelembapan & Hari Kerja vs Weekend:
Kategori kelembapan dan perbedaan pola antara weekdays dan weekend menunjukkan kondisi cuaca dan hari apa yang optimal untuk penyewaan.

### 5. Dashboard Interaktif dengan Streamlit
Dashboard dibuat untuk menyajikan analisis secara interaktif dengan fitur filter berdasarkan rentang tanggal dan tahun.

### 6. Dependencies
Lihat file requirements.txt untuk daftar library.

### 7. Cara Menjalankan Proyek
Notebook: Buka dan jalankan notebook.ipynb untuk mereproduksi proses data cleaning, merging, dan EDA.
Dashboard: Jalankan perintah streamlit run dashboard/dashboard.py dari terminal untuk membuka dashboard interaktif.
Dataset: Pastikan file dataset asli dan file bersih berada di folder data.

https://joanneeldy-proyekdata.streamlit.app/

### 8. Kesimpulan
Proyek ini berhasil menggabungkan data harian dan per jam dari Bike Sharing untuk mengungkap pola-pola penting seperti tren penyewaan, pengaruh waktu, kondisi musim, kelembapan, dan perbedaan antara weekdays dan weekend. Insight ini dapat digunakan untuk membantu dalam pengambilan keputusan operasional serta perencanaan strategi.