# 단순하게 푸는 답안 예시
n, k = map(int, input().split())
result = 0
# n이 k이상이면 반복
while n >= k:
    # n이 k로 나누어 떨어지지 않을때
    while n % k != 0:
        n -= 1
        result += 1
    # n이 k의 배수이면
    n //= k
    result += 1
# 마지막으로 남은 수가 n이 1보다 크고 k보다 작은 경우
while n > 1:
    n -= 1
    result += 1

print(result)