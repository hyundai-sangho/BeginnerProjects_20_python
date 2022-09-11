import string
import random

문자모음 = list(string.ascii_letters + string.digits + "!@#$^&*()")


def 비밀번호_생성기():
    비밀번호_길이 = int(input("비밀번호 길이를 입력: "))

    random.shuffle(문자모음)

    비밀번호 = []

    for x in range(비밀번호_길이):
        비밀번호.append(random.choice(문자모음))
        print(비밀번호)

    random.shuffle(비밀번호)
    print(비밀번호)

    비밀번호 = "".join(비밀번호)

    print("비밀번호는: " + 비밀번호)


옵션 = input("비밀번호 만들기를 원해? (네/아뇨) ")

if 옵션 == "네":
    비밀번호_생성기()
elif 옵션 == "아뇨":
    print("프로그램을 종료합니다.")
    quit()
else:
    print("잘못된 입력입니다. '네' or '아뇨'를 선택해 주세요.")
    quit()
