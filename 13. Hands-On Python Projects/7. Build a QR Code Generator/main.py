

'''
Ues a Python library like qrcode and convert url to qr code

qrcode library also depends on Pillow (the modern version of PIL — Python Imaging Library) to generate images.

install Pillow: pip install pillow
'''
import qrcode

url = input("Enter your url: ")
filename = input("Filename you want to save it as: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)