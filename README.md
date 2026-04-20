# Bike-Sharing-Dashboard1
# 🚲 Bike Sharing Data Analysis & Dashboard

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis pola penggunaan sepeda berdasarkan dataset Bike Sharing (2011–2012). Analisis difokuskan pada:

* Perbandingan penggunaan sepeda antara hari kerja dan hari libur
* Pola distribusi penyewaan berdasarkan jam

Selain itu, proyek ini dilengkapi dengan dashboard interaktif menggunakan Streamlit untuk visualisasi hasil analisis.

---

## Pertanyaan Analisis

1. Bagaimana perbandingan rata-rata penggunaan sepeda antara hari kerja dan hari libur?
2. Bagaimana pola distribusi penyewaan sepeda berdasarkan jam?

---

## Insight Utama

* Rata-rata penyewaan lebih tinggi pada **hari kerja (~4584)** dibandingkan **hari libur (~4330)**
* Terdapat pola **bimodal**:

  * Pagi (±08.00)
  * Sore (±17.00–18.00)
* Penyewaan sangat rendah pada dini hari (00.00–05.00)
* Sepeda dominan digunakan sebagai **transportasi (commuting)**

---

## Data Cleaning

* Konversi kolom `dteday` menjadi tipe datetime
* Penambahan kolom `weather_label` untuk interpretasi cuaca
* Tidak terdapat missing values dan duplikasi data
* Dataset siap digunakan untuk analisis lanjutan

---

## Exploratory Data Analysis (EDA)

Analisis yang dilakukan:

* Perbandingan weekday vs weekend
* Pola penyewaan per jam
* Kombinasi jam dan tipe hari
* Visualisasi heatmap

---

## Dashboard (Streamlit)

Dashboard digunakan untuk:

* Menampilkan pola penyewaan per jam
* Membandingkan hari kerja vs hari libur
* Visualisasi interaktif berbasis data

---

## Setup Environment

### 1. Clone Repository

```bash
git clone https://github.com/username/bike-sharing-dashboard.git
cd submission
```

### 2. (Opsional) Buat Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Menjalankan Dashboard

```bash
cd dashboard
streamlit run dashboard.py
```

---

## Struktur Folder

```
submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── data/
│   ├── hour.csv
│   └── day.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## Dependencies

```
streamlit
pandas
numpy
matplotlib
seaborn
```

---

## Rekomendasi Strategis

* Tambahkan sepeda pada jam sibuk (pagi & sore)
* Lakukan maintenance saat jam sepi
* Optimalkan distribusi:

  * Hari kerja → area perkantoran
  * Hari libur → area rekreasi

---

## Kesimpulan

Penggunaan sepeda sangat dipengaruhi oleh waktu dan jenis hari. Pola yang terbentuk menunjukkan bahwa sepeda berfungsi sebagai alat transportasi utama dengan lonjakan penggunaan pada jam sibuk.

---

## 👤 Author

* Nama: [Shofia ariska]
* Project: Bike Sharing Analysis & Dashboard
