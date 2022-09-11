import urllib.request as urllib


def main(url):
    print("연결 확인 ")

    응답 = urllib.urlopen(url)

    print(응답)
    print(url, "연결 성공")
    print("응답 코드:", 응답.getcode())


print("웹 사이트 연결 확인 프로그램입니다.")
입력한_URL = input("웹 사이트의 URL 입력: ")

main(입력한_URL)
