n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0
count = 0
while m != count:
    for _ in range(k):
        result += first
        count += 1
    
    result += second
    count += 1

print(result)

# 메세지 변경!
