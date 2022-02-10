n = int(input()) 
array = list(map(int, input().split())) 
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환 
array.reverse()

dp = [1] * n 
# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)

# 최종 max(dp)가 가장 긴 증가하는 부분 수열 
# 열외시켜야 하는 병사의 최소 수를 출력 
print(n - max(dp)) 

# 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수
# 즉 내림차순으로 이어지는 최대 길이를 구하라.
# 다이나믹 프로그래밍 