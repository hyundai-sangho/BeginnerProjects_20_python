# str 변수에 들어있는 문자열의 특정 단어를 변환해주는 프로그램
# ex) hi 입력 후, 변환할 문자로 hello로 입력하면
# Hi, guys, I am sangho, and hello로 출력
def replace_word():

    str = "Hi guys, I am sangho, and hi"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))


replace_word()
