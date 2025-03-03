import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Atur tampilan grafik
plt.rcParams["figure.figsize"] = (10, 6)

st.title("Dashboard Analisis Bike Sharing")

@st.cache_data
def load_data():
    df = pd.read_csv('Bike-sharing-dataset/clean_merged.csv')
    df['dateday'] = pd.to_datetime(df['dateday'])
    # Pastikan kolom 'temp' sudah dalam satuan Celsius
    # Buat kategori suhu
    bins = [0, 10, 15, 20, 25, 30, 41]
    labels = ['Sangat Dingin', 'Dingin', 'Sejuk', 'Hangat', 'Panas', 'Sangat Panas']
    df['temp_category'] = pd.cut(df['temp'], bins=bins, labels=labels, include_lowest=True)
    return df

df = load_data()

st.subheader("Data Preview")
st.write(df.head())

# --- Sidebar Filter ---
st.sidebar.header("Filter Data")

# Filter berdasarkan rentang tanggal
if 'dateday' in df.columns:
    min_date = df['dateday'].min().date()
    max_date = df['dateday'].max().date()
    date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date])
    
    if isinstance(date_range, list) and len(date_range) == 2:
        start_date, end_date = date_range
        df_filtered = df[(df['dateday'].dt.date >= start_date) & (df['dateday'].dt.date <= end_date)]
    else:
        df_filtered = df.copy()
else:
    df_filtered = df.copy()

# -----------------------------
# 1. Tren Penyewaan Sepeda per Hari (Line Plot)
# -----------------------------
st.subheader("Tren Penyewaan Sepeda per Hari")

if 'dateday' in df_filtered.columns and 'daily_cnt' in df_filtered.columns:
    fig1, ax1 = plt.subplots(figsize=(12,6))
    sns.lineplot(data=df_filtered, x='dateday', y='daily_cnt', ax=ax1)
    ax1.set_title("Tren Penyewaan Sepeda per Hari")
    ax1.set_xlabel("Tanggal")
    ax1.set_ylabel("Total Penyewaan Harian")
    plt.xticks(rotation=45)
    st.pyplot(fig1)
else:
    st.write("Kolom 'dateday' atau 'daily_cnt' tidak ditemukan.")

# -----------------------------
# 2. Rata-rata Penyewaan per Musim (Bar Plot)
# -----------------------------
st.subheader("Rata-rata Penyewaan per Musim")

if 'season' in df_filtered.columns and 'hourly_count' in df_filtered.columns:
    season_avg = df_filtered.groupby('season')['hourly_count'].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(8,6))
    sns.barplot(data=season_avg, x='season', y='hourly_count', palette='coolwarm', ax=ax2)
    ax2.set_title("Rata-rata Penyewaan per Musim")
    ax2.set_xlabel("Musim")
    ax2.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig2)
else:
    st.write("Kolom 'season' atau 'hourly_count' tidak ditemukan.")

# -----------------------------
# 3. Rata-rata Penyewaan per Jam Berdasarkan Kategori Suhu (Bar Plot)
# -----------------------------
st.subheader("Rata-rata Penyewaan Sepeda per Jam Berdasarkan Kategori Suhu")

if 'temp_category' in df_filtered.columns and 'hourly_count' in df_filtered.columns:
    # Jika df_agg_temp sudah dibuat di Notebook, kita bisa langsung hitung di sini juga
    temp_agg = df_filtered.groupby('temp_category')['hourly_count'].mean().reset_index()
    fig3, ax3 = plt.subplots(figsize=(8,6))
    sns.barplot(data=temp_agg, x='temp_category', y='hourly_count', palette='magma', ax=ax3)
    ax3.set_title("Rata-rata Penyewaan Sepeda per Jam (Kategori Suhu)")
    ax3.set_xlabel("Kategori Suhu")
    ax3.set_ylabel("Rata-rata Penyewaan per Jam")
    st.pyplot(fig3)
else:
    st.write("Kolom 'temp_category' atau 'hourly_count' tidak ditemukan.")

# -----------------------------
# 4. Perbandingan Penyewaan: Hari Kerja vs Weekend (Bar Plot)
# -----------------------------
st.subheader("Perbandingan Penyewaan: Hari Kerja vs Weekend")

if 'category_days' in df_filtered.columns and 'daily_cnt' in df_filtered.columns:
    fig4, ax4 = plt.subplots(figsize=(8,6))
    sns.barplot(data=df_filtered, x='category_days', y='daily_cnt', palette='pastel', ax=ax4)
    ax4.set_title("Perbandingan Penyewaan: Hari Kerja vs Weekend")
    ax4.set_xlabel("Kategori Hari")
    ax4.set_ylabel("Total Penyewaan Harian")
    st.pyplot(fig4)
else:
    st.write("Kolom 'category_days' atau 'daily_cnt' tidak ditemukan.")

# -----------------------------
# (Opsional) 5. Rata-rata Penyewaan Berdasarkan Jam (Bar Plot)
# -----------------------------
st.subheader("Rata-rata Penyewaan Berdasarkan Jam")

if 'hour' in df_filtered.columns and 'hourly_count' in df_filtered.columns:
    avg_by_hour = df_filtered.groupby('hour')['hourly_count'].mean().reset_index()
    fig5, ax5 = plt.subplots(figsize=(8,6))
    sns.barplot(data=avg_by_hour, x='hour', y='hourly_count', palette='viridis', ax=ax5)
    ax5.set_title("Rata-rata Penyewaan per Jam")
    ax5.set_xlabel("Jam")
    ax5.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig5)
else:
    st.write("Kolom 'hour' atau 'hourly_count' tidak ditemukan.")


# --- Analisis Lanjutan: Clustering (Manual Grouping) ---
st.subheader("Analisis Lanjutan: Pengelompokan Hari Berdasarkan Penyewaan")

# Membuat kategori penggunaan (usage) dengan binning pada daily_cnt
bins_usage = [0, 3000, 5000, df['daily_cnt'].max()]
labels_usage = ['Low Usage', 'Medium Usage', 'High Usage']
df['usage_category'] = pd.cut(df['daily_cnt'], bins=bins_usage, labels=labels_usage, include_lowest=True)

# Tampilkan distribusi kategori penggunaan
st.write("Distribusi kategori penggunaan harian:")
st.write(df['usage_category'].value_counts())

# Visualisasi distribusi kategori penggunaan
fig_cluster, ax_cluster = plt.subplots(figsize=(8,6))
sns.countplot(data=df, x='usage_category', palette='Set2', ax=ax_cluster)
ax_cluster.set_title("Distribusi Kategori Penggunaan Harian")
ax_cluster.set_xlabel("Kategori Penggunaan")
ax_cluster.set_ylabel("Jumlah Hari")
st.pyplot(fig_cluster)

# --- Analisis Lanjutan ---
st.markdown("## Analisis Lanjutan")
st.markdown("""
1. **RFM Analysis:** Tidak dapat diterapkan karena tidak ada data transaksi per pelanggan.
2. **Geospatial Analysis:** Tidak dapat diterapkan karena tidak ada data lokasi.
3. **Clustering:** Mengelompokkan hari berdasarkan total penyewaan menggunakan teknik binning.
""")
