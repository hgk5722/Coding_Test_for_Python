n = int(input()) 
data = list(map(int, input().split())) 
add, sub, mul, div = map(int, input().split()) 

min_value = (1e9) # 최소값 최댓값 10억, -10억으로 설정 
max_value = (-1e9) 

def dfs(i, now):
  global min_value, max_value, add, sub, mul, div 
  # 재귀호출과 돌아올때의 i값과 add, sub, mul, div의 반환으로 인해 가능한 모든 연산이 한번씩 실행됨
  # 모든 연산자를 한번씩 다 사용하면 최대, 최소값 갱신하러 들름.
  if i == n:
    # 모든 연산 중에 최소값과 최대값을 구할 수 있음.
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    if add > 0:
      add -= 1
      dfs(i + 1, now + data[i]) # i + 1하고 now값 갱신해서 재귀호출 
      add += 1 # i값과 add값 다시 돌아옴 
    if sub > 0:
      sub -= 1
      dfs(i + 1, now - data[i]) 
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i + 1, now * data[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i + 1, now / data[i])
      div += 1

# 처음 노드 스택에 넣고 방문 처리 
dfs(1, data[0])

# 최종 결과 출력 
print(max_value)
print(min_value) 
