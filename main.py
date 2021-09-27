import face_detection
import send_request
import time
import cv2

device_id = 2
while True:
    print('press any to ring the bell')
    ring = input()
    face = None
    while face is None:
        time.sleep(0.5)
        face = face_detection.get_faces()
    send_request.send('http://192.168.188.68:8000/ring/',device_id,'picture.png')
