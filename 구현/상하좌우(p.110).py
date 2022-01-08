n = int(input())
data = list(input().split())

x, y = 1, 1

for i in data:
    if i == "R":
        if y + 1 > n:   # 마지막 열일때
            continue
        else:
            y += 1
    elif i == "L":
        if y - 1 == 0:  # 1열일때
            continue
        else:
            y -= 1
    elif i == "U":
        if x - 1 == 0:  # 1행일때
            continue
        else:
            x -= 1
    else:   # 마지막 행일때
        if x + 1 > n:
            continue
        else:
            x += 1

print(x, y)