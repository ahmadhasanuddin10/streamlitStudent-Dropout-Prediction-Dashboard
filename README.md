# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech


## Business Understanding
Latar Belakang Bisnis: Jaya Jaya Institut adalah institusi pendidikan yang berdiri sejak tahun 2000 dengan reputasi baik dalam mencetak lulusan. Namun, terdapat tantangan besar berupa tingginya angka dropout di kalangan siswa. Masalah ini berpotensi merusak reputasi institusi dan mengurangi tingkat keberhasilan akademik.


### Permasalahan Bisnis
Tingginya risiko siswa yang melakukan dropout, yang dapat berdampak pada revenue perusahaan.
Kurangnya pemahaman terhadap faktor-faktor yang memengaruhi dropout siswa.
Kebutuhan untuk memonitor dan menganalisis data siswa secara interaktif untuk pengambilan keputusan yang lebih cepat dan efektif.


### Cakupan Proyek
Data Preprocessing: Membersihkan dan mempersiapkan data siswa untuk analisis dan model machine learning.
Model Machine Learning: Mengembangkan sistem prediksi risiko dropout menggunakan algoritma machine learning.
Business Dashboard: Membuat dashboard untuk memvisualisasikan data siswa, faktor-faktor risiko, dan prediksi dropout.
Prototipe Sistem: Menyediakan antarmuka untuk mengunggah data baru dan mendapatkan prediksi risiko dropout.

### Persiapan

Sumber data: [https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv]

Setup environment:
```
numpy
pandas
matplotlib
seaborn
scikit-learn
joblib
streamlit
```

## Business Dashboard
Dashboard dibuat dengan menggunakan Google Looker Studio. Dashboard dapat diakses pada link berikut ini:
```
https://lookerstudio.google.com/reporting/fe9dcb0f-1122-4d57-a9e4-34d11927daf9
```
## Menjalankan Sistem Machine Learning
Cara Menjalankan Prototipe:

1. Local:
Jalankan perintah berikut:

```
streamlit run app.py
```
Akses prototipe di browser melalui http://localhost:8501.

2. Hosting: Jika di-deploy di Streamlit Cloud, pengguna hanya perlu mengakses tautan yang disediakan.


Akses prototipe di browser melalui :
```
https://appstudent-dropout-prediction-dashboard-zbacgnvnm3ekgc3nhv6hun.streamlit.app/
```

## Conclusion
Proyek ini berhasil mengembangkan model prediksi risiko dropout siswa dan dashboard interaktif. Model mampu memberikan wawasan tentang faktor-faktor utama yang memengaruhi dropout, sementara dashboard memungkinkan manajemen untuk menganalisis data secara cepat dan membuat keputusan berbasis data.
Dari hasil analisis data terkait risiko dropout pada perusahaan, berikut adalah beberapa poin penting:

Distribusi Risiko Dropout:

Sebagian besar individu diklasifikasikan sebagai dropout, mengindikasikan bahwa tantangan utama perusahaan adalah mempertahankan individu agar tetap terdaftar atau menyelesaikan program mereka.
Probabilitas dropout lebih tinggi pada individu dengan status aktual Dropout, tetapi terdapat overlap probabilitas antara Dropout dan Enrolled. Hal ini menunjukkan bahwa beberapa individu yang saat ini terdaftar (Enrolled) juga memiliki risiko dropout yang signifikan.
Hubungan Karakteristik Individu dan Risiko Dropout:

Dari analisis distribusi, individu dengan probabilitas dropout tinggi berasal dari berbagai kategori kursus dan status marital. Hal ini menunjukkan bahwa risiko dropout tidak hanya dipengaruhi satu variabel tunggal, tetapi merupakan kombinasi beberapa faktor.
Performa Program:

Tingginya jumlah individu yang diklasifikasikan sebagai Dropout dapat menjadi indikasi adanya masalah di dalam program kursus, seperti kurangnya dukungan, materi yang terlalu sulit, atau kurang relevannya program dengan kebutuhan peserta.
Probabilitas dan Intervensi:

Probabilitas dropout memberikan pandangan awal mengenai siapa saja yang memerlukan perhatian khusus. Namun, analisis menunjukkan perlunya lebih banyak informasi untuk mengidentifikasi pola-pola yang lebih spesifik dalam mencegah dropout.


### Rekomendasi Action Items
Meningkatkan Engagement Siswa:

Bangun sistem pengingat otomatis bagi siswa dengan performa rendah untuk menyelesaikan materi kursus.
Sediakan tutor atau mentor tambahan bagi siswa berisiko tinggi.
Peningkatan Monitoring Data:

Integrasikan sistem prediksi dropout ke platform utama perusahaan untuk pemantauan langsung.
Gunakan analitik lanjutan untuk mengidentifikasi tren dropout di masa depan.
Kampanye Edukasi:

Jalankan kampanye untuk meningkatkan kesadaran siswa tentang manfaat menyelesaikan kursus.
Sediakan insentif atau reward bagi siswa yang menyelesaikan kursus tanpa dropout.
