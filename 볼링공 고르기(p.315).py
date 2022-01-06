n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
for i in range(n-1):
    #j = i + 1
    for j in range(i+1, n):
        if data[i] != data[j]:
            count += 1
print(count)
# 빠른 방법은 아니지만 2중 for문을 이용해서 구할 수 있다.
# 하지만 안쪽 for문의 반복변수 j를 i+1로 대응하게 해야하는데 방법을 모르겠다.
# 해결했다. j를 i+1로 대응하게 하는법 7행을 보면된다.