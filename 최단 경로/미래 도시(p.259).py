INF = int(1e9) 

# 노드의 개수 및 간선의 개수를 입력받기 
n, m = map(int, input().split()) 
# 2차원 리스트(그래프 표현)을 만들고, 모든 값을무한으로 초기화 
graph = [ [INF] * (n + 1) for _ in range(n + 1) ] 

# 자기 자신에서 자시 자신으로 가는 비용은 0으로 초기화 
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0 

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화 
for _ in range(m):
  # A와 B가 서로에게 가는 비용은 1이라고 설정 
  a, b  = map(int, input().split()) 
  graph[a][b] = 1 
  graph[b][a] = 1 

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기 
x, k = map(int, input().split()) # 1 -> K -> X 순으로 이동 

# 점화식에 따라 플로이드 워셜 알고리즘을 수행 (이해 했으면 다음부턴 그냥 암기할 것!) 
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1): 
      # 거쳐가는 노드 k를 기준으로 직진이 빠른지 거쳐가는게 빠른지 판단하여 최단거리를 갱신.
      graph[a][b]  = min(graph[a][b], graph[a][k] + graph[k][b]) 
# 예시2에서 k = 4니까 k = 1 ~ 4까지 돌아가면서 행렬에 graph[a][b]가 a와 b의 상하좌우만 움직이는 이유는 
# 중간값 k를 넣어서 거쳐가는 거니까 자신의 주변부분을 지나가게 됨 
# 방문하지 않는 곳은 최단거리를 계산하지 않는다는 말과 같다.
# 그래서 노드k를 거쳐서 가는 모든 경우가 N^2이고 이것을 k번 반복하니 시간복잡도는 O(n^3)이 된다. 



# 수행된 결과를 출력 
# 모든 최단거리를 행렬에 구해놓고 원하는 구역만 거쳐가는것을 구함. 
distance = graph[1][k] + graph[k][x] 

# 도달할 수 없는 경우, -1을 출력 
if distance >= INF:
  print(-1) 
# 도달할 수 있다면, 최단 거리를 출력 
else: 
  print(distance) 