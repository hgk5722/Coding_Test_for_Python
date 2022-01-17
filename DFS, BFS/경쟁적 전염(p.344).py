from collections import deque

n, k = map(int, input().split()) 
# 맵 초기화
graph = [ [0] * n for _ in range(n) ]
data = [] # 바이러스 정보를 입력할 리스트 
# 처음 단계 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j)) # 튜플로 입력 

data.sort()
queue = deque(data) 

target_s, target_x, target_y = map(int, input().split()) 

dx = [ -1, 0, 1, 0 ] 
dy = [ 0, 1, 0, -1 ] 

while queue:
    virus, s, x, y = queue.popleft() 
    if target_s == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # 아직 방문하지 않은 구역 
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s + 1, nx, ny)) 
print(graph[target_x - 1][target_y - 1]) 