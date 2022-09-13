import pyqrcode
import png
link = "https://www.linkedin.com/in/mahima-kumari-31a3991b0/"
qr_code = pyqrcode.create(link)
qr_code.png("LinkedIn.png", scale=6)
