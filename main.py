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
        time.sleep(1)
        face = face_detection.get_faces()
    print('face detected')
    res = send_request.send_ring('http://192.168.188.68:8000/ring/',device_id,'picture.png')
    print (res)
    if res =='"open"':
        print('door is opened')
    else:
       time.sleep(30)
       res = send_request.send_change('http://192.168.188.68:8000/check/',device_id)
       print (res)
