# 현 나이트의 위치 입력받기
input_data = input()
# a1을 입력 받을때 1은 행이고 a는 열이다.
row = int(input_data[1])    # 1
col = int(ord(input_data[0])) - int(ord('a')) + 1   # a

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [ (-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, -1), (2, 1) ]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치
    next_row = row + step[0] # 반복변수 step도 배열처럼 사용가능
    next_col = col + step[1]
    # 나이트가 이동한 위치가 정원 내부에 있으면 카운트 1 증가
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

print(result)
