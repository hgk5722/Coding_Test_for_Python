n, k = map(int, input().split())
count = 0
while True:
    # n이 k의 배수일때
    if n % k == 0:
        n //= k
        count += 1
    # 아니면 1씩 빼줌
    else:
        n -= 1
        count += 1
    # 도착
    if n == 1: 
        break

print(count)
