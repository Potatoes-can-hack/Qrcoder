import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=9s")
img.save("Qrcode_youtube.png")