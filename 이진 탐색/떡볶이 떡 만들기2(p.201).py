# 함수로 만들어본 경우 
def binary_search(array):
    start  = 0
    end = max(array) 
    result = 0 
    while start <= end:
        total = 0
        mid = (start + end) // 2 
        for x in array:
            if x > mid:
                total += (x - mid) 
        if total < m:
            end = mid - 1
        else:
            start = mid + 1
            result = mid 
    return result 

n, m = map(int, input().split()) 
array = list(map(int, input().split())) 
print(binary_search(array)) 