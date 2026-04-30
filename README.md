# Proyek Analisis Data Bike Sharing

* Setup virtual environment

Agar tidak terjadi konflik antar library, buat terlebih dahulu virtual environment sebelum menjalankan dashboard.

1. Menggunakan Conda (disarankan)

conda create --name main-ds python=3.9

conda activate main-ds

pip install -r requirements.txt



2\. Alternatif menggunakan Pipenv

mkdir proyek\_analisis\_data

cd proyek\_analisis\_data

pipenv install

pipenv shell

pip install -r requirements.txt



3\. Cara jalankan dashboard

streamlit run dashboard/dashboard.py



## Informasi Singkat

Dashboard ini dibuat untuk menganalisis faktor yang memengaruhi jumlah peminjaman sepeda berdasarkan kondisi cuaca, temperatur, serta pola penggunaan pada hari kerja dan akhir pekan.

## Insight Singkat

* Peminjaman tertinggi terjadi saat cuaca cerah dan temperatur hangat
* Penggunaan sepeda lebih tinggi pada akhir pekan dibanding hari kerja

