# Stream CCTV dengan Deteksi Objek YOLOv8

Aplikasi web Flask untuk streaming CCTV dengan kemampuan deteksi objek menggunakan YOLOv8. Aplikasi ini dapat menampilkan video stream dari kamera RTSP dan melakukan deteksi objek secara real-time.

## Fitur
- Streaming video langsung dari kamera RTSP
- Deteksi objek real-time menggunakan YOLOv8
- Antarmuka web yang responsif
- Mudah dikonfigurasi

## Persyaratan Sistem
- Windows 10/11 dengan WSL2
- Docker Desktop
- Koneksi jaringan ke kamera RTSP

## Dependensi
- Flask 3.0.2
- OpenCV Python 4.8.1.78
- NumPy 1.24.3
- Ultralytics 8.1.28 (YOLOv8)
- PyTorch 2.0.1
- TorchVision 0.15.2

## Cara Instalasi dan Penggunaan

### 1. Persiapan WSL
1. Buka terminal PowerShell sebagai Administrator
2. Masuk ke WSL Ubuntu sebagai root:
```bash
wsl -d ubuntu --user root
```

### 2. Menggunakan Docker
1. Clone repositori ini
2. Buat dan jalankan container Docker:
```bash
docker run -it --network host --name python_dev -v ${PWD}:/app -w /app python:3.9 bash
```

### 3. Setup Container
1. Masuk ke container jika belum berada di dalamnya:
```bash
docker exec -it python_dev bash
```

2. Install dependensi Python:
```bash
pip install -r requirements.txt
```

3. Install dependensi sistem untuk OpenCV:
```bash
apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0
```

4. Jalankan aplikasi:
```bash
python app.py
```

5. Buka browser dan akses:
```
http://localhost:5000
```

## Konfigurasi

Konfigurasi URL RTSP dapat diubah di file `app.py`:

```python
rtsp_url = 'rtsp://admin:BGENWW@192.168.100.28:554/stream'
```

Ganti URL sesuai dengan konfigurasi kamera RTSP Anda.

## Troubleshooting

1. **Stream tidak muncul**
   - Periksa apakah URL RTSP benar
   - Pastikan kredensial (username/password) benar
   - Periksa koneksi jaringan ke kamera
   - Lihat log terminal untuk pesan error

2. **Port 5000 sudah digunakan**
   - Ubah port di `app.py` dengan menambahkan parameter port:
   ```python
   app.run(debug=True, port=5001)
   ```

3. **Masalah OpenCV di Docker**
   - Jika muncul error `libGL.so.1`, jalankan:
   ```bash
   apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0
   ```

4. **Masalah Performa**
   - Pastikan koneksi jaringan stabil
   - Kurangi resolusi video jika diperlukan
   - Periksa penggunaan CPU dan memori

## Keamanan

- Jangan menyimpan kredensial RTSP langsung dalam kode
- Gunakan variabel lingkungan atau file konfigurasi terpisah
- Batasi akses ke aplikasi web menggunakan autentikasi jika diperlukan
- Pastikan container Docker dikonfigurasi dengan aman

## Kontribusi

Kontribusi selalu diterima! Silakan buat pull request atau laporkan issue jika menemukan bug.

## Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail. 
