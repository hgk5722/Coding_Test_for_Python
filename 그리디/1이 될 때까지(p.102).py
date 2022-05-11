n, k = map(int, input().split()) 
result = 0 

while True:
  # k로 나눠 떨어지지 않는 n값을 조정해 주고 그 차이만큼을 횟수에 추가 
  # 예를 들어 18 4이면 그 차이인 2만큼은 1을 두번 빼줬다고 생각.
  target = (n//k) * k # n이 k보다 작으면 몫이 0이 나올테니 break문에 걸림 
  result +=  (n - target) # n이 k로 나눠 떨어지는 수로 맞췄다면 마지막 n은 항상 1이 된다. 
  # 그렇게 n = 1을 추가하고 
  n = target # 그리고 마지막 target은 0이 되어서 break 문에 걸리게 된다. 
  # 
  if n < k:
    break 
  # k로 나누기 
  result += 1
  n //= k 
  
result += (n - 1) # 추가했던 n을 빼주면 정답이 된다. 
print(result) 

""" 
17 4
target = 17 // 4 ) * 4 = 16
result += 17 -16 = 1

n = 16

result += 1 = 2
n //= k = 4

target = 4

result += 0 = 2

result += 1 = 3
4 //= 4 = n = 1

target = 0 * 4 = 0
result += (1-0) = 4
n = target = 0

if 0 < 4:
break

result += ( 0-1) = 3
print(result) = 3 """