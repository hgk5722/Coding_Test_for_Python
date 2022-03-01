# O(logN)으로 해결해야 하니 선형탐색은 안됨
def binary_search(array, start, end):
    if start > end:
        return None
    # 여기선 mid가 target 역할 
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid: # 모르겠으면 부품찾기에서 elif 부분이랑 똑같다(mid == target) 
        return binary_search(array, start, mid - 1) 
    # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else: # start = mid + 1
        return binary_search(array, mid + 1, end) 

n = int(input()) 
array = list(map(int, input().split())) 

index = binary_search(array, 0, n - 1) 

# 고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
# 아닌 경우 해당 인덱스 출력
else: 
    print(index) 

# start와 end를 무엇으로 설정할 것인가? -> 이 문제에선 인덱스 -> 구하고자 하는것이 인덱스 
# 위치값과 일치하는 인덱스를 찾는것이 목표 -> 인덱스를 mid라 표현 (target) 
# 위치값이 여기선 가운데값이다 array[mid] (mid) 
# 가운데값(array[mid])보다 mid(target)이 더 크면 start = mid + 1 