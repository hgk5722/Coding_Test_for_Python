# O(logN)으로 해결하라 했으니 순차탐색은 안되고 이진탐색으로 해결해야함
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value) 
    left_index = bisect_left(array, left_value) 
    return right_index - left_index 

n, x = map(int, input().split()) # n, x 입력
array = list(map(int, input().split())) 

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)  

#  값이 x인 원소가 존재하지 않는다면
if count == 0: 
    print(-1) 
# 값이 x인 원소가 존재한다면
else: 
    print(count) 
