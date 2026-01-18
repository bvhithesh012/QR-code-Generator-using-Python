import qrcode

url = input("Enter the URL: ").strip()
file_path = "("enter the file_path location")qrcode.png"

qr=qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)


print("QR code was Generated!, saved to file_path !")
