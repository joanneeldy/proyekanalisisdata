import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Atur tampilan grafik
plt.rcParams["figure.figsize"] = (10, 6)

st.title("Dashboard Analisis Bike Sharing")

# Gunakan st.cache_data untuk menyimpan hasil load data
@st.cache_data
def load_data():
    df = pd.read_csv('Bike-sharing-dataset/clean_merged.csv')
    # Pastikan kolom tanggal sudah di-convert
    df['dateday'] = pd.to_datetime(df['dateday'])
    return df

df = load_data()

st.subheader("Data Preview")
st.write(df.head())

# --- Sidebar Filter ---
st.sidebar.header("Filter Data")

# Filter berdasarkan tanggal (rentang tanggal)
if 'dateday' in df.columns:
    min_date = df['dateday'].min().date()
    max_date = df['dateday'].max().date()
    date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date])
    
    # Jika rentang tanggal dipilih (mengembalikan list dengan dua tanggal)
    if isinstance(date_range, list) and len(date_range) == 2:
        start_date, end_date = date_range
        df_filtered = df[(df['dateday'].dt.date >= start_date) & (df['dateday'].dt.date <= end_date)]
    else:
        df_filtered = df.copy()
else:
    df_filtered = df.copy()

# Visualisasi 1: Tren Penyewaan per Hari
st.subheader("Tren Penyewaan Sepeda per Hari")
fig1, ax1 = plt.subplots()
sns.lineplot(data=df, x='dateday', y='daily_cnt', ax=ax1)
ax1.set_title("Total Penyewaan per Hari")
ax1.set_xlabel("Tanggal")
ax1.set_ylabel("Total Penyewaan")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Visualisasi 2: Rata-rata Penyewaan Berdasarkan Jam
st.subheader("Rata-rata Penyewaan Berdasarkan Jam")
if 'hour' in df.columns:
    avg_by_hour = df.groupby('hour')['hourly_count'].mean().reset_index()
    fig2, ax2 = plt.subplots()
    sns.barplot(data=avg_by_hour, x='hour', y='hourly_count', ax=ax2)
    ax2.set_title("Rata-rata Penyewaan per Jam")
    ax2.set_xlabel("Jam")
    ax2.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig2)
else:
    st.write("Kolom 'hr' tidak ditemukan di data.")

# Visualisasi 3: Distribusi Penyewaan Berdasarkan Musim
st.subheader("Distribusi Penyewaan Berdasarkan Musim")
if 'season' in df.columns:
    fig3, ax3 = plt.subplots()
    sns.boxplot(data=df, x='season', y='hourly_count', ax=ax3)
    ax3.set_title("Penyewaan per Jam Berdasarkan Musim")
    ax3.set_xlabel("Musim")
    ax3.set_ylabel("Penyewaan per Jam")
    st.pyplot(fig3)
else:
    st.write("Kolom 'season' tidak ditemukan di data.")
