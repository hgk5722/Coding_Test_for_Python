# m의 크기가 100억 이상이 되면 시간 초과 판정이 나오기 때문에 공식을 이용한 풀이가 필요함

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]
#가장 큰 수(first)가 반복되는 횟수
count = (int(m / (k+1)) * k) + (m % (k+1))

result = 0
# 결과값에 first가 반복될 수 더함
result += count * first
# 결과값에 second가 반복될 수 더함
result += (m - count) * second
# first와 second가 모두 더해진 값 출력
print(result)
