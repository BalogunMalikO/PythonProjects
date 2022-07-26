# import the necessary module
import pyqrcode
import png

# users are asked to input the link to be to be converted to QRCODE
link = input("Enter link: ")

# used to create the qrcode
qr_code = pyqrcode.create(link)

#this is to let you know the above code worked
print("Voiala! qrcode created." )

#this saves the qrcode in png format
qr_code.png("qrName.png", scale=5)
print("QRcode generated!")



