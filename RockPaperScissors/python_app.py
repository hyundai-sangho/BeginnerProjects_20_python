import random

나가기 = False
사용자_점수 = 0
컴퓨터_점수 = 0

while 나가기 == False:
    옵션 = ["바위", "보", "가위"]
    사용자_선택 = input("가위, 바위, 보 선택 or 나가기: ")
    컴퓨터_선택 = random.choice(옵션)

    if 사용자_선택 == "나가기":
        print("게임 종료")
        나가기 = True

    elif 사용자_선택 == "바위":
        if 컴퓨터_선택 == "바위":
            print("당신의 선택은 바위")
            print("컴퓨터의 선택은 바위")
            print("무승부")
            print("")
        elif 컴퓨터_선택 == "보":
            print("당신의 선택은 바위")
            print("컴퓨터의 선택은 보")
            print("컴퓨터의 승리")
            print("")
            컴퓨터_점수 += 1
        elif 컴퓨터_선택 == "가위":
            print("당신의 선택은 바위")
            print("컴퓨터의 선택은 가위")
            print("당신의 승리")
            print("")
            사용자_점수 += 1

    elif 사용자_선택 == "보":
        if 컴퓨터_선택 == "바위":
            print("당신의 선택은 보")
            print("컴퓨터의 선택은 바위")
            print("당신의 승리")
            print("")
            사용자_점수 += 1
        elif 컴퓨터_선택 == "보":
            print("당신의 선택은 보")
            print("컴퓨터의 선택은 보")
            print("무승부")
            print("")
        elif 컴퓨터_선택 == "가위":
            print("당신의 선택은 보")
            print("컴퓨터의 선택은 가위")
            print("컴퓨터의 승리")
            print("")
            컴퓨터_점수 += 1

    elif 사용자_선택 == "가위":
        if 컴퓨터_선택 == "바위":
            print("당신의 선택은 가위")
            print("컴퓨터의 선택은 바위")
            print("컴퓨터의 승리")
            print("")
            컴퓨터_점수 += 1
        elif 컴퓨터_선택 == "보":
            print("당신의 선택은 가위")
            print("컴퓨터의 선택은 보")
            print("당신의 승리")
            print("")
            사용자_점수 += 1
        elif 컴퓨터_선택 == "가위":
            print("당신의 선택은 가위")
            print("컴퓨터의 선택은 가위")
            print("무승부")
            print("")

    else:
        print("잘못된 입력")
        print("")

print("-------------------")
print("최종 점수는")
print("컴퓨터: " + str(컴퓨터_점수))
print("당신: " + str(사용자_점수))
print("프로그램을 종료합니다.")
