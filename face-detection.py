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
    buff = numpy.frombuffer(stream.getvalue(), dtype=numpy.uint8)
    image = cv2.imdecode(buff, 1)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    print ("Found "+str(len(faces))+" face(s)")

 
    if len(faces):
        return image1
    return None
print(get_faces())

