n, m = map(int, input().split()) 
# N개의 화페 단위 입력받기 
array = [] 
for i in range(n):
  array.append(int(input())) 

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [10001] * (m + 1) 

# 다이나믹 프로그래밍 진행(보텀업) 
d[0] = 0
for i in range(n): # 작은 화페부터 하나씩 진행 ( 순서대로 입력될 것이라고 생각 ) 
  for j in range(array[i], m + 1): 
    if d[j - array[i]] != 10001: # a(i-k) 값이 이전에 한번이라도 조정이 되었다면(초기값이 아니라면) 
      # min함수안에 d[j]를 넣는 이유 : 이전에 반복문을 돌린 금액(array[i])의 조합이 더 작은 수 일수 있어서
      d[j] = min(d[j], d[j - array[i]] + 1) 

if d[m] == 10001:
  print(-1)
else:
  print(d[m]) 

# a(i-k)인 이유 : k는 지금 세고 있는 화페의 단위 
# a(7- 5) = a(2)가 존재하면(10001이 아니면) a(2)에 k(지금은 5)를 추가해서 2 + 5가 되기 때문에
# 그래서 a(2)인 a(i-k)에 +1을 해주면서 최소의 횟수를 추가해준다. 