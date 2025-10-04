

# 📊 RetailKita Data Pipeline & Analytics

Proyek ini membangun **pipeline ETL sederhana** untuk mengolah data transaksi e-commerce dari file CSV menjadi tabel analitik di PostgreSQL, serta melakukan **analisis & visualisasi** untuk mendukung pengambilan keputusan berbasis data.

---

## 🚀 Cara Menjalankan ETL Script

Jalankan perintah berikut untuk melakukan proses **Extract, Transform, Load (ETL)**:

```bash
python main.py engine run
```

Script ini akan:

* Membaca data dari `resources/transactions.csv`, `resources/products.csv`, dan `resources/customers.csv`.
* Melakukan pembersihan & transformasi data (misalnya membuat kolom `total_price`, `is_new_customer`, `revenue_band`, dll).
* Menyimpan hasil analitik ke PostgreSQL dalam tabel: **`retail_kita_analytic`**.

---

## 📂 Struktur Folder

```
source/
│── main.py                  # Entry point ETL
│── service/                 # Modul koneksi PostgreSQL
│── resources/
│   ├── transactions.csv     # Data transaksi
│   ├── products.csv         # Data produk
│   ├── customers.csv        # Data pelanggan
│   └── query.sql            # Kumpulan query analitik
│── visualisasi.ipynb        # Notebook untuk analisis & visualisasi
```

---

## 📑 Query Analisis

Kumpulan query SQL untuk analisis dapat ditemukan di:

```
source/resources/query.sql
```

Beberapa analisis utama:

1. **Produk Terlaris** → 5 produk teratas berdasarkan total pendapatan.
2. **Pelanggan Paling Berharga** → 10 pelanggan dengan total belanja tertinggi.
3. **Tren Penjualan Bulanan** → total pendapatan per bulan.

---

## 📈 Visualisasi

Untuk visualisasi hasil analisis, buka notebook berikut:

```
source/visualisasi.ipynb
```

Contoh visualisasi yang tersedia:

* **Top 5 Produk Terlaris** (Bar Chart)
* **Top 10 Pelanggan Paling Berharga** (Bar Chart)
* **Tren Penjualan Bulanan** (Line Chart)

---

## 🔧 Teknologi yang Digunakan

* **Python (Pandas, Typer, Loguru)** → ETL
* **PostgreSQL** → Data Warehouse
* **Matplotlib / Seaborn** → Visualisasi
* **Jupyter Notebook** → Analisis & Eksplorasi

---

👉 Dengan struktur ini, tim manajemen dapat **mengambil insight dengan cepat** dari data transaksi tanpa harus repot mengolah data mentah.

---
