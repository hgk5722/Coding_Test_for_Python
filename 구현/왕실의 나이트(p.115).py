input_data = input()
# a1을 입력 받을때 1은 행이고 a는 열이다.
row = int(input_data[1])    # 1
col = int(ord(input_data[0])) - int(ord('a')) + 1   # a

steps = [ (-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, -1), (2, 1) ]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0] # 반복변수 step도 배열처럼 사용가능
    next_col = col + step[1]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

print(result)
