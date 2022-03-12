import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None # if에서 리턴하지 못하고 여기까지 오면 None 반환 

n = int(sys.stdin.readline()) 
array = list(map(int, sys.stdin.readline().split())) 
array.sort() 

m = int(sys.stdin.readline()) 
x = list(map(int, sys.stdin.readline().split())) 

for i in x:
    result = binary_search(array, i, 0, n - 1) 
    if result == None:
        print('no', end= ' ') 
    else:
        print('yes', end= ' ') 

# N개의 정렬된 부품에서 M개를 찾을 때 O(MlogN) 약 200만
# 그래서 시간 복잡도는 O((M + N)logN) 