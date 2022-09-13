# pip install Pillow
from PIL import Image


def 사진크기조정(size1, size2):
    사진 = Image.open("female.jpg")
    print(f"현재 사진 (가로, 세로) 크기: {사진.size}")
    resized_image = 사진.resize((size1, size2))
    resized_image.save("female-" + str(size1) + ".jpg")


size1 = int(input("가로 크기: "))
size2 = int(input("세로 크기: "))
사진크기조정(size1, size2)
