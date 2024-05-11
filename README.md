# Tugas ETS Pemrograman Jaringan
- Nama: Adrian Aziz Santoso (NRP 5025221229)
- Kelas: Pemrograman Jaringan C
- Tanggal: Sabtu, 6 April 2024

Dengan memanfaatkan program pada progjar5`: https://github.com/rm77/progjar/tree/master/progjar5, 

- Gunakan contoh source code yang disediakan, untuk dimodifikasi 
- Gunakan instalasi lab Anda sendiri 
- Implementasikan web server dengan multiprocessing 
- Buatlah perbandingan kinerja web server (https://github.com/rm77/progjar/blob/master/progjar5/server_thread_http.py) dengan:
  - Multithreading 
  - Multiprocessing 
  - Multithreading (secure) 
  - Multiprocessing (secure) 
- Untuk pengukuran kinerja, gunakan tool `ab` (apache-benchmark) dengan jumlah request 1000, dengan parameter concurrency 10, 50, 100, 150, dan 200 
- Laporkan kinerja dalam hal: 
  - Failed requests
  - Total Transfer
  - Request per second
  - Time per request
  - Transfer Rate
  - Connect
  - Processing
  - Waiting
  - Total connection time 
- Untuk meningkatkan performa, hilangkan beberapa overhead seperti Print / mencetak log seluruh isi direktori / folder 
- `Apache-benchmark` dapat diinstall di ubuntu/debian dengan `sudo apt install apache2-utils`

Laporan disubmit dalam bentuk:
- 1 dokumen PDF, maks 10 halaman 
- Isikan alamat repository yang berkaitan dengan tugas diatas
- Spek komputer yang digunakan untuk menjalankan server dan melakukan testing, beserta gambar arsitektur percobaan
- Tabel perbandingan dalam PDF yang sama dan lengkapi dengan penjelasan dan deskripsi dan kesimpulan hasil test tersebut, contoh tabel:
  - https://docs.google.com/spreadsheets/d/1MrFHM5Rek4VaHUBjxjsx6ZlGkaZY4GWLBLXrQtZO2Wo/edit?usp=sharing/

Tambahan referensi mengenai multiprocessing & multithreading:
- https://superfastpython.com/multiprocessing-in-python/#Python_Processes
- https://superfastpython.com/what-is-a-thread-in-python/ 
- Contoh eksekusi ab untuk 1000 request dengan 1 client:

<img width="345" alt="image" src="https://github.com/adrianazizsantoso/tugas-ets-pemrograman-jaringan/assets/115202624/0e5ce083-795b-4b51-aafd-9a2a1923716a">

### Perbandingan Kinerja Server Web dengan Multiprocessing

Laporan ini membandingkan kinerja server web yang diimplementasikan, dengan model konkur-ensi yang berbeda:
- Multithreading (keamanan biasa)
- Multiprocessing (keamanan biasa)
- Multithreading (keamanan tinggi)
- Multiprocessing (keamanan tinggi)

Perbandingan ini didasarkan pada skrip `server_thread_http.py` dari repositori progjar5 (https://github.com/rm77/progjar/blob/master/progjar5/server_thread_http.py) dan menggunakan alat `ab` (apache-benchmark) untuk pengukuran kinerja.


### Metodologi

- Kode sumber dari server_thread_http.py dimodifikasi untuk mendukung model kon-kurensi yang berbeda.
- Server web dijalankan pada mesin khusus dengan spesifikasi berikut:
  - CPU: AMD Ryzen 7 5700U with Radeon Graphics @ 1.80 GHz
  - RAM: 16GB DDR4 (15,4 GB usable)
  - OS: Windows 11 Home Single Language build 22631.3447
- `Apache-benchmark` digunakan untuk mengukur kinerja dengan 1000 permintaan dan ting-kat konkurensi 10, 50, 100, 150, dan 200.
- Metrik kerja berikut dicatat:
  - Failed requests
  - Total Transfer
  - Request per second
  - Time per request
  - Transfer Rate
  - Connect
  - Processing
  - Waiting
  - Total connection time

### Hasil

Hasil perbandingan kinerja dicatat dalam tabel berikut:

<img width="510" alt="image" src="https://github.com/adrianazizsantoso/tugas-ets-pemrograman-jaringan/assets/115202624/5f00488b-afeb-4878-834b-22933d8fa3ce">

### Observasi

- Semua model konkurensi menunjukkan kinerja yang serupa untuk tingkat konkurensi rendah (10).
- Model multiprocessing dan multithreading (dengan keamanan tinggi) menunjukkan kinerja yang lebih baik daripada model multithreading dan multithreading (dengan keamanan tinggi) untuk tingkat konkurensi yang lebih tinggi (50, 100, 150, 200).
- Model multiprocessing menunjukkan kinerja yang sedikit lebih baik daripada model multithreading (untuk keamanan tinggi) untuk tingkat konkurensi yang lebih tinggi.
- Overhead komunikasi aman (HTTPS) sedikit memengaruhi kinerja untuk semua model.


### Kesimpulan

Model multiprocessing dan multithreading (dengan keamanan tinggi) direkomendasikan untuk server web yang membutuhkan konkurensi tinggi. Model multiprocessing menawarkan kinerja yang sedikit lebih baik daripada model multithreading (untuk keamanan tinggi), namun dengan biaya kompleksitas yang lebih mahal. Komunikasi aman dengan HTTPS akan menim-bulkan sedikit penalti kinerja.


### Tautan Repositori

Kode sumber yang telah dimodifikasi serta skrip pengukuran kinerja tersedia dalam repositori berikut:
https://github.com/adrianazizsantoso/tugas-ets-pemrograman-jaringan/blob/main/sourceCode.py


### Spesifikasi Sistem

Server dijalankan pada mesin khusus dengan spesifikasi berikut:
- CPU: AMD Ryzen 7 5700U with Radeon Graphics @ 1.80 GHz
- RAM: 16GB DDR4 (15,4 GB usable)
- OS: Windows 11 Home Single Language build 22631.3447


### Arsitektur Eksperimental

Diagram berikut mengilustrasikan arsitektur eksperimental:

<img width="194" alt="image" src="https://github.com/adrianazizsantoso/tugas-ets-pemrograman-jaringan/assets/115202624/13641ef9-b3a7-4f5d-9184-a9415f8459af">

Mesin klien akan mengirimkan permintaan HTTP ke server web, yaitu server yang memproses permintaan serta menghasilkan respons.


Referensi
¹Brownlee, Jason. (2024). Multiprocessing in Python: Python Processes. Superfast Python. https://superfastpython.com/multiprocessing-in-python/#Python_Processes
²Brownlee, Jason. (2024). What is a Thread in Python. Superfast Python. https://superfastpython.com/what-is-a-thread-in-python/ 
