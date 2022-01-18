from collections import deque
n, l, r = map(int, input().split()) 

graph = [ [0] * n for _ in range(n) ] 
for i in range(n):
    graph[i] = list(map(int, input().split())) 

dx = [ -1, 0, 1, 0 ]
dy = [ 0, 1, 0, -1 ]

result = 0

def process(x, y, index):
    # x, y의 위치와 연결된 나라(연합) 정보를 담는 리스트 
    united = []
    united.append((x, y))
    #  너비 우선 탐색(bfs)을 위한 큐 자료구조 정의 
    queue = deque()
    queue.append((x, y)) 
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(bfs) 
    while queue:
        x, y = queue.popleft() 
        # 현재 위치에서 4가지 방향을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    queue.append((nx, ny)) 
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny] 
                    count += 1 # 연합의 국가 수 증가 
                    united.append((nx, ny)) 
    for i, j in united:
        graph[i][j] = summary // count 
    return count 

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [ [-1] * n for _ in range(n) ] 
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1 
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
            break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)