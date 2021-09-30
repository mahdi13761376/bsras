import requests
import base64

def send_ring(url, device_id, img_address ):
    with open (img_address , 'rb') as img:
        ba_64_img = base64.b64encode(img.read())
        data = {'device_id':device_id,
            'img':ba_64_img,
            }
        r = requests.post(url = url, data = data)
        res = r.text
        return res;
    
def send_change(url, device_id):
    data = {'device_id':device_id
        }
    r = requests.post(url = url, data = data)
    res = r.text
    return res;
