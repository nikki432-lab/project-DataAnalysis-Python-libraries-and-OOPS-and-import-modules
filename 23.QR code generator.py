import qrcode

image = qrcode.make("https://github.com/nikki432-lab/Pyhton-MenuDriven-Programms-and-OOP-challenges")

image.save("Nikgithub_qr.png")

print("QR Code Generated Successfully")