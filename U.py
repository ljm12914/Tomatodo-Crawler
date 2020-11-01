from pip._vendor import requests
import urllib
import PIL
import os
from PIL import Image
from io import BytesIO
import time
headers = {
    'User-Agent':'Dalvik/2.1.0(Linux;U;Android8.1.0;RedmiNote8ProMIUI/V11.0.3.0.OEGCNXM)',
    'Host':'poster.tomatotime.cn',
    'Connection':'Keep-Alive',
    'Accept-Encoding':'gzip'
    }
i = 1
while(i < 2000):
    print("Try download pic " + str(i))
    try:
        r = requests.get('http://poster.tomatotime.cn/test' + str(i) + '.JPG', headers=headers)
        image = Image.open(BytesIO(r.content))
    except PIL.UnidentifiedImageError:
        print("Try download pic " + str(i) + " failed.")
        time.sleep(0.5)
        i += 1
    else:
        print("Try download pic " + str(i) + " succeed")
        image.save('E:/tomatodo/' + str(i) + '.jpg')
        time.sleep(0.5)
        i += 1