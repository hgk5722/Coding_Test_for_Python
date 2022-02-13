INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정 

# 노드의 개수 및 간선의 개수를 입력받기 
n = int(input()) 
m = int(input()) 
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화 
graph = [[INF] * (n + 1) for _ in range(n + 1) ] 

# 자기 자신에서 자기 자신으로 가는 비용은  0으로 초기화 
for a in range(1, n + 1): 
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0 

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화 
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정 
  a, b, c = map(int, input().split()) 
  # graph에 저장되는 것은 최단거리인 값이라는것을 기억!! 
  graph[a][b] = c 

# 점화식에 따라 플로이드 워셜 알고리즘을 수행 
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      # k번 노드를 거쳐 가는 경우니 행과 열에 k가 들어가는 경우를 배제 
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) 

# 수행된 결과를 출력 
for a in range(1, n + 1):
  for b in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력 
    if graph[a][b] == INF:
      print("INFINITY", end=" ") 
    else: 
      print(graph[a][b], end=" ") 
  print() 