# Stream CCTV YOLO Detection dengan Penghitungan Objek

Aplikasi web untuk menampilkan stream CCTV dengan deteksi objek menggunakan YOLOv8. Aplikasi ini dapat mendeteksi dan menghitung objek secara real-time dengan menampilkan jumlah total dan detail setiap objek yang terdeteksi.

## Fitur

- 🎥 Streaming CCTV secara real-time
- 🔍 Deteksi objek menggunakan YOLOv8
- 📊 Menghitung jumlah objek yang terdeteksi secara real-time
- 📈 Menampilkan detail confidence level setiap objek
- ⚡ Update data otomatis setiap detik
- 📱 Tampilan responsif dan user-friendly

## Screenshot

### Tampilan dengan 4 Objek Terdeteksi
![Tampilan 4 Objek](docs/images/img%201.jpg)
*Deteksi 4 objek: bed (60.53%), 2 person (39.12%, 38.15%), dan kite (27.54%)*

### Tampilan dengan 3 Objek Terdeteksi
![Tampilan 3 Objek](docs/images/img%202.jpg)
*Deteksi 3 objek: bed (54.93%) dan 2 person (32.26%, 30.14%)*

### Tampilan dengan 2 Objek Terdeteksi
![Tampilan 2 Objek](docs/images/img%203.jpg)
*Deteksi 2 person dengan confidence level 79.09% dan 45.58%*

## Cara Penggunaan

### Menjalankan dengan Docker (Direkomendasikan)

1. Tarik image Python 3.9 dari Docker Hub:
   ```bash
   docker pull python:3.9
   ```

2. Cek image yang sudah terunduh:
   ```bash
   docker images
   ```

3. Jalankan container dengan pengaturan yang sesuai:
   ```bash
   docker run -it --network host --name app_rtsp_cctv_yolo -v ${PWD}:/app -w /app python:3.9 bash
   ```
   - `--network host` : Agar container dapat mengakses RTSP stream di jaringan lokal.
   - `-v ${PWD}:/app` : Mount folder project ke dalam container.
   - `-w /app` : Set direktori kerja di dalam container ke `/app`.

4. Install dependencies Python:
   ```bash
   pip install -r requirements.txt
   ```

5. Install library sistem yang dibutuhkan OpenCV:
   ```bash
   apt-get update
   apt-get install -y libgl1
   ```

6. Jalankan aplikasi:
   ```bash
   python app.py
   ```

7. Buka browser dan akses:
   ```
   http://localhost:5000
   ```

**Catatan:**
- Pastikan file `requirements.txt` sudah ada di folder project.
- Jika ingin keluar dari container, gunakan perintah `exit`.
- Untuk menjalankan ulang container yang sudah pernah dibuat:
  ```bash
  docker start -ai app_rtsp_cctv_yolo
  ```

### Menjalankan secara Lokal (Opsional)

1. Install dependencies yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```
2. Pastikan library sistem `libgl1` sudah terinstall:
   ```bash
   sudo apt-get update
   sudo apt-get install -y libgl1
   ```
3. Jalankan aplikasi:
   ```bash
   python app.py
   ```
4. Buka browser dan akses:
   ```
   http://localhost:5000
   ```

## Fitur Detail

### Panel Informasi
- Total objek terdeteksi
- Daftar jenis objek dan jumlahnya
- Waktu deteksi real-time
- Confidence level setiap objek

### Kemampuan Deteksi
- Multiple object detection
- Real-time object counting
- Confidence level tracking
- Automatic updates

## Konfigurasi RTSP

Untuk menggunakan CCTV Anda sendiri, ubah `rtsp_url` di file `app.py`:

```python
rtsp_url = 'rtsp://username:password@ip-address:port/stream'
```

## Teknologi yang Digunakan

- Python Flask untuk backend
- YOLOv8 untuk deteksi objek
- OpenCV untuk pemrosesan video
- jQuery untuk update data real-time
- HTML/CSS untuk tampilan frontend

## Struktur Proyek

```
├── app.py              # Aplikasi Flask dan logika utama
├── requirements.txt    # Daftar dependencies
├── templates/         
│   └── index.html     # Template HTML
├── docs/
│   └── images/        # Screenshot aplikasi
└── README.md          # Dokumentasi
```

## Kontribusi

Kontribusi selalu diterima! Silakan buat pull request atau laporkan issue jika menemukan bug.

## Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail. 
