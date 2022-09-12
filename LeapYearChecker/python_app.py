# 서력 기원 연수가 4로 나누어 떨어지는 해는 윤년으로 한다.
# (1988년, 1992년, 1996년, 2004년, 2008년, 2012년, 2016년, 2020년, 2024년, 2028년, 2032년, 2036년, 2040년, 2044년 ...)

# 서력 기원 연수가 4, 100으로 나누어 떨어지는 해는 평년으로 한다.
# (1700년, 1800년, 1900년, 2100년, 2200년, 2300년...)

# 서력 기원 연수가 4, 100, 400으로 나누어 떨어지는 해는 윤년으로 둔다.
# (1600년, 2000년, 2400년...)
def 윤년인가(년도):
    if 년도 % 4 == 0:
        if 년도 % 100 == 0:
            if 년도 % 400 == 0:
                print("윤년입니다.")
            else:
                print("평년입니다.")
        else:
            print("윤년입니다.")
    else:
        print("평년입니다.")


년도 = int(input("올해는 몇 년도인가요? "))
윤년인가(년도)