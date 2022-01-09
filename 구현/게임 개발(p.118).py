n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 맵 깔기
wall = [ [0] * m for _ in range(n) ]

wall[x][y] = 1


dx = [ -1, 0, 1, 0 ] # 북, 남
dy = [ 0, 1, 0, -1 ] # 동, 서
count = 1
turn_time = 0

# 맵 입력받아 채우기
for i in range(n):
    wall[i] = list(map(int, input().split()))

def turn_left():
    d = [ 0, 1, 2, 3 ] # 북, 동, 남, 서
    global direction
    for i in range(len(d)):
        if direction == d[i]:
            direction = d[i-1]

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if wall[nx][ny] == 0:
        wall[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if wall[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)

# turn_left는 내가 구현