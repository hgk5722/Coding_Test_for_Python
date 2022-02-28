from bisect import bisect_left, bisect_right 

def count_by_range(array, x): # 매개변수값 하나로 조정 
    left_index = bisect_left(array, x) 
    right_index = bisect_right(array, x) 
    return right_index - left_index

n, x = map(int, input().split()) 
array = list(map(int, input().split())) 

# 어차피 x가 수열에서 몇개인지를 구하는 문제니까 letf_value, right_value 하나로 조정 
result = count_by_range(array, x) 
if result == 0:
    print(-1)
else:
    print(result) 
