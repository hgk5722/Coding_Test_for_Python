n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 맵 깔기
graph = [ [0] * m for _ in range(n) ] 
graph[x][y] = 1 # 시작 노드 방문처리 

dx = [ -1, 0, 1, 0 ] # 북, 남 
dy = [ 0, 1, 0, -1 ] # 동, 서 
count = 1 # 방문처리 했으니 1로 시작  
turn_time = 0 

# 맵 입력받아 채우기
for i in range(n):
    graph[i] = list(map(int, input().split())) 

def turn_left():
    d = [ 0, 1, 2, 3 ] # 북, 동, 남, 서
    global direction
    for i in range(4): # len(d)라 하지 않고 4라 해도 무방
        if direction == d[i]:
            direction = d[i-1]

while True:
    turn_left() # direction 변경 
    nx = x + dx[direction] 
    ny = y + dy[direction] 
    if graph[nx][ny] == 0: 
        graph[nx][ny] = 1 # 방문처리 
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue # 4번 회전할 수도 있기 때문에 continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if graph[nx][ny] == 0:
            x, y = nx, ny
        else: # 후진 실패시 반복문 탈출(종료) 
            break
        turn_time = 0 # 후진에 성공한 뒤 회전 수 초기화 
print(count)

# turn_left는 내가 구현