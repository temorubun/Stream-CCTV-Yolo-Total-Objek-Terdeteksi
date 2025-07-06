from flask import Flask, render_template, Response, jsonify
import cv2
from ultralytics import YOLO
import numpy as np
import threading
import time
from collections import Counter

app = Flask(__name__)

# Inisialisasi model YOLO
model = YOLO('yolov8n.pt')

# Variable global untuk menyimpan data deteksi terbaru
latest_detections = {
    'objects': [],
    'counts': {},
    'total_objects': 0,
    'timestamp': None
}

def update_detection_data(results):
    global latest_detections
    objects_detected = []
    
    # Mengambil hasil deteksi dari model YOLO
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Mendapatkan nama kelas dan confidence
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            name = model.names[cls]
            
            objects_detected.append({
                'class': name,
                'confidence': round(conf * 100, 2)
            })
    
    # Menghitung jumlah setiap jenis objek
    object_counts = Counter(obj['class'] for obj in objects_detected)
    
    latest_detections['objects'] = objects_detected
    latest_detections['counts'] = dict(object_counts)
    latest_detections['total_objects'] = len(objects_detected)
    latest_detections['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S')

def generate_frames():
    # RTSP URL
    rtsp_url = 'rtsp://admin:BGENWW@192.168.100.28:554/stream'
    
    # Buka koneksi RTSP
    cap = cv2.VideoCapture(rtsp_url)
    
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Lakukan deteksi menggunakan YOLO
            results = model(frame)
            
            # Update data deteksi
            update_detection_data(results)
            
            # Gambar hasil deteksi
            annotated_frame = results[0].plot()
            
            # Encode frame untuk streaming
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detection_data')
def detection_data():
    return jsonify(latest_detections)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') 