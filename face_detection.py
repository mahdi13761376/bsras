import io
import picamera
import cv2
import numpy
import time
from picamera.array import PiRGBArray

stream = io.BytesIO()

def get_faces():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 720)
        camera.capture(stream, format='png')
        rawcapture = PiRGBArray(camera)
        time.sleep(0.1)
        camera.capture(rawcapture, format="bgr")
        image1 = rawcapture.array
        cv2.imwrite('picture.png', image1)
        
        
    image = cv2.imread('picture.png')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    if len(faces):
        return image1
    return None

