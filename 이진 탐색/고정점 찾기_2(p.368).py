n = int(input())
array = list(map(int, input().split()))

start = 0
end = n-1

def binary_search(array, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1

result = binary_search(array, start, end)
if result != 0:
    print(result)
else:
    print(-1)