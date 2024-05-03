import pyqrcode
import png
from pyqrcode import QRCode

#put link here 
s = "https://www.linkedin.com/in/tushar-kumar-mishra-1974b124b/"

#Gentrate qr code 
url = pyqrcode.create(s)

#Create and save the svg file 
url.svg("myqr.svg",scale=8)

#Create and save the svg file 
url.png("myqr.png",scale=8)
