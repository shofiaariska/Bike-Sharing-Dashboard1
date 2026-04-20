
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('main_data.csv')

st.set_page_config(layout="wide")
st.title('🚲 Bike Sharing Dashboard')

# ===============================
# SIDEBAR FILTER
# ===============================
st.sidebar.header('Filter')

hour_range = st.sidebar.slider('Pilih Jam', 0, 23, (0, 23))
day_filter = st.sidebar.selectbox('Tipe Hari', ['Semua', 'Kerja', 'Libur'])

# Filter data
filtered_df = df[(df['hr'] >= hour_range[0]) & (df['hr'] <= hour_range[1])]

if day_filter == 'Kerja':
    filtered_df = filtered_df[filtered_df['workingday'] == 1]
elif day_filter == 'Libur':
    filtered_df = filtered_df[filtered_df['workingday'] == 0]

# Mapping label
filtered_df['day_type'] = filtered_df['workingday'].map({
    1: 'Kerja',
    0: 'Libur'
})

# ===============================
# METRICS
# ===============================
col1, col2, col3 = st.columns(3)

col1.metric("Total", int(filtered_df['cnt'].sum()))
col2.metric("Rata-rata", round(filtered_df['cnt'].mean(), 2))
col3.metric("Peak Hour", int(filtered_df.groupby('hr')['cnt'].mean().idxmax()))

# ===============================
# GRAFIK JAM
# ===============================
st.subheader('📈 Pola Penyewaan per Jam')

hour_data = filtered_df.groupby('hr')['cnt'].mean()

fig, ax = plt.subplots(figsize=(10,4))
hour_data.plot(marker='o', ax=ax)
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah')
ax.grid()
st.pyplot(fig)

# ===============================
# GRAFIK HARI
# ===============================
st.subheader('📊 Hari Kerja vs Libur')

day_data = filtered_df.groupby('day_type')['cnt'].mean()

fig2, ax2 = plt.subplots()
sns.barplot(x=day_data.index, y=day_data.values, ax=ax2)
st.pyplot(fig2)

# ===============================
# HEATMAP 
# ===============================
st.subheader ('🔥 Heatmap Jam vs Hari')

pivot = filtered_df.pivot_table(
    values='cnt',
    index='hr',
    columns='day_type',
    aggfunc='mean'
)

fig3, ax3 = plt.subplots(figsize=(6,8))
sns.heatmap(pivot, cmap='YlGnBu', annot=True, fmt='.0f', ax=ax3)
st.pyplot(fig3)
