# pip install PyDictionary
from PyDictionary import PyDictionary

# dictionary = PyDictionary("eyes", "indentation", "head")
# print(dictionary.printMeanings())
# print(dictionary.getMeanings())

사전 = PyDictionary()

print(사전.meaning("eyes"))

while True:
    검색단어 = input("검색할 영단어 입력: ")
    if 검색단어 == "":
        break
    if 검색단어 == "나가기":
        break

    print(사전.meaning(검색단어))

print("프로그램을 종료합니다.")

# def main():
#     단어_사전 = {
#         "안녕": "인사의 방법",
#         "눈": "보는 기관",
#         "지구": "우주의 행성",
#     }

#     while True:
#         검색단어 = input("검색할 단어 입력: ")
#         if 검색단어 == "":
#             break
#         if 검색단어 == "나가기":
#             break
#         if 검색단어 in 단어_사전:
#             print(검색단어, ":", 단어_사전[검색단어])
#         else:
#             print("단어 사전에는 검색한 단어가 없습니다.")

#     print("프로그램을 종료합니다.")


# # main()
