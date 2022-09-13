# pip install matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 사용시 기본이 영문이라 한글이 깨짐
# 한글 사용시에는 font를 따로 지정해줘야 한글이 깨지지 않음.
font_path = "C:/Windows/Fonts/D2Coding-Ver1.3.2-20180524-all.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family=font)

left = [1, 2, 3, 4, 5]
height = [10, 11, 23, 36, 4]

tick_label = ["one", "two", "three", "four", "five"]

plt.bar(left, height, tick_label=tick_label, width=0.8, color=["blue", "orange"])


plt.xlabel("X축")
plt.ylabel("Y축")
plt.title("데모 그래프 - 바 차트")

plt.show()
