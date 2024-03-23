import qrcode
from PIL import Image 

print("Hello World!")

img = qrcode.make(input("Enter the information to store : "))
img.save("qr_code.png")

im = Image.open("qr_code.png")
im.show()
