import qrcode


def QR코드생성기(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    이미지 = qr.make_image(fill_color="black", back_color="white")
    이미지.save("QR_IMAGE.png")


url = input("QR 코드 생성할 URL 입력: ")
QR코드생성기(url)
