# 원리금균등분할상환 방식의 계산기
# 참고 : https://www.kbinsure.co.kr/CG407000001.ec
def main():
    print("이것은 월별 지불 대출 계산기입니다\n")

    principal = float(input("대출 금액을 입력 : "))
    apr = float(input("연간 이자율을 입력 : "))
    years = int(input("대출 기간 연수 : "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    print("monthly_interest_rate : " + str(monthly_interest_rate))
    print("amount_of_months : " + str(-amount_of_months))
    print(
        "principal * monthly_interest_rate : " + str(principal * monthly_interest_rate)
    )
    print(
        "(1 - (1 + monthly_interest_rate) ** (-amount_of_months)) : "
        + str((1 - (1 + monthly_interest_rate) ** (-amount_of_months)))
    )
    monthly_payment = (
        principal
        * monthly_interest_rate
        / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    )

    print("이 대출에 대한 월별 지불은 : %.2f " % monthly_payment)


main()
