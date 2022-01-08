# 왕실의 나이트 문제를 풀기전에 코드업에 있는 문제를 이해해야한다.
# 영문 소문자 입력받아 a부터 그 문자까지 출력하기
x = ord(input())    # ex) f를 입력받아 a~f 출력하기
y = ord('a')
while x != y:
    y = chr(y)
    print(y)
    y = ord(y) + 1
print(chr(x))       # 마지막 입력받은 알파벳 출력