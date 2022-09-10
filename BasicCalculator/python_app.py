# 더하기, 빼기, 곱하기, 나누기 계산

# 더하기
def add(a, b):
    answer = int(a) + int(b)
    print("더하기: " + str(a) + " + " + str(b) + " = " + str(answer) + "\n")


# 빼기
def sub(a, b):
    answer = int(a) - int(b)
    print("빼기: " + str(a) + " - " + str(b) + " = " + str(answer) + "\n")


# 곱하기
def mul(a, b):
    answer = int(a) * int(b)
    print("곱하기: " + str(a) + " * " + str(b) + " = " + str(answer) + "\n")


# 나누기
def div(a, b):
    answer = int(a) / int(b)
    print("나누기: " + str(a) + " / " + str(b) + " = " + str(answer) + "\n")


# 5번을 눌러서 나가기 선택 전까지 계속 반복(quit()을 만날 때까지 계속 반복)
while True:
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 나가기")

    choice = input("input your choice : ")

    if choice == "1":
        print("더하기")
        a = int(input("첫 번째 수: "))
        b = int(input("두 번째 수: "))
        add(a, b)
    elif choice == "2":
        print("빼기")
        a = int(input("첫 번째 수: "))
        b = int(input("두 번째 수: "))
        sub(a, b)
    elif choice == "3":
        print("곱하기")
        a = int(input("첫 번째 수: "))
        b = int(input("두 번째 수: "))
        mul(a, b)
    elif choice == "4":
        print("나누기")
        a = int(input("첫 번째 수: "))
        b = int(input("두 번째 수: "))
        div(a, b)
    elif choice == "5":
        print("프로그램 종료")
        quit()
