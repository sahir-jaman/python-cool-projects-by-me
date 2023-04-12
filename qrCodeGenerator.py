import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
qr.add_data('https://www.youtube.com/@sahir-jaman')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("some_file.png")