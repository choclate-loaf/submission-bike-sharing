import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ========================
# CONFIG
# ========================
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# ========================
# LOAD DATA
# ========================
@st.cache_data
def load_data():
    df = pd.read_csv("data/main_data.csv")
    
    # Convert date
    df['dteday'] = pd.to_datetime(df['dteday'])
    
    # Extract time features
    df['year'] = df['dteday'].dt.year
    df['month'] = df['dteday'].dt.month
    df['day_name'] = df['dteday'].dt.day_name()
    
    # Handle hour column (optional)
    if 'hr' in df.columns:
        df['hour'] = df['hr']
    
    return df

df = load_data()

# ========================
# SIDEBAR FILTER
# ========================
st.sidebar.header("🔎 Filter Data")

year = st.sidebar.selectbox("Pilih Tahun", sorted(df['year'].unique()))

filtered_df = df[df['year'] == year]

# ========================
# TITLE
# ========================
st.title("📊 Dashboard Analisis Bike Sharing")
st.markdown("Analisis pola peminjaman sepeda berdasarkan waktu dan cuaca")

# ========================
# 1. METRIC
# ========================
col1, col2, col3 = st.columns(3)

col1.metric("Total Peminjaman", int(filtered_df['cnt'].sum()))
col2.metric("Rata-rata Harian", int(filtered_df['cnt'].mean()))
col3.metric("Maksimum Peminjaman", int(filtered_df['cnt'].max()))

# ========================
# 2. TREND BULANAN
# ========================
st.subheader("📈 Tren Peminjaman per Bulan")

monthly = filtered_df.groupby('month')['cnt'].sum()

fig1, ax1 = plt.subplots()
ax1.plot(monthly.index, monthly.values, marker='o')
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Jumlah Peminjaman")
ax1.set_title("Tren Peminjaman Bulanan")

st.pyplot(fig1)

# ========================
# 3. PENGARUH CUACA
# ========================
st.subheader("🌤️ Pengaruh Cuaca")

weather = filtered_df.groupby('weathersit')['cnt'].mean()

fig2, ax2 = plt.subplots()
sns.barplot(x=weather.index, y=weather.values, ax=ax2)
ax2.set_xlabel("Kondisi Cuaca")
ax2.set_ylabel("Rata-rata Peminjaman")
ax2.set_title("Pengaruh Cuaca terhadap Peminjaman")

st.pyplot(fig2)

# ========================
# 4. POLA JAM
# ========================
if 'hour' in filtered_df.columns:
    st.subheader("⏰ Pola Peminjaman per Jam")

    hourly = filtered_df.groupby('hour')['cnt'].mean()

    fig3, ax3 = plt.subplots()
    ax3.plot(hourly.index, hourly.values, marker='o')
    ax3.set_xlabel("Jam")
    ax3.set_ylabel("Rata-rata Peminjaman")
    ax3.set_title("Pola Penggunaan per Jam")

    st.pyplot(fig3)

# ========================
# 5. HARI DALAM SEMINGGU
# ========================
st.subheader("📅 Pola Berdasarkan Hari")

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

daily = filtered_df.groupby('day_name')['cnt'].mean().reindex(day_order)

fig4, ax4 = plt.subplots()
sns.barplot(x=daily.index, y=daily.values, ax=ax4)
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45)
ax4.set_title("Rata-rata Peminjaman per Hari")

st.pyplot(fig4)

# ========================
# INSIGHT
# ========================
st.subheader("📌 Insight")

st.markdown("""
- Peminjaman sepeda meningkat pada jam sibuk (pagi dan sore)
- Cuaca cerah meningkatkan jumlah peminjaman
- Pola penggunaan berbeda antara hari kerja dan akhir pekan
""")
