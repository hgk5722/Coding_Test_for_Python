import sys 
n = int(input()) 
students = []
for i in range(n):
    a, b, c, d = list(sys.stdin.readline().split())
    students.append([a, b, c, d])

""" [정렬 기준] 
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬 
4) 네 번째 원소가 같은 경우, 첫 번쨰 원소를 기준으로 오름차순 정렬
 """

# 튜플로 정렬
students.sort(key = lambda x : ( -int(x[1]), int(x[2]), -int(x[3]), x[0] )) # 그래야지 여러 조건 가능

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0]) 

""" 정렬을 하지 않고 students 리스트를 출력하면.

for student in students:
    print(student)

['Junkyu', '50', '60', '100']
['Sangkeun', '80', '60', '50']
['Sunyoung', '80', '70', '100']
['Soong', '50', '60', '90']
['Heabin', '50', '60', '100']
['Kangsoo', '60', '80', '100']
['Donghyuk', '80', '60', '100']
['Sei', '70', '70', '70']
['Wonseob', '70', '70', '90']
['Sanghyun', '70', '70', '80']
['nsj', '80', '80', '80']
['Taewhan', '50', '60', '90']

for i in range(n):
    students.append(input().split())
이렇게 입력을 받아도 리스트로 정렬이 알아서 됨. """



""" example )
a = [ [5, 1, 5], [3, 5, 5], [3, 1, 9], [3, 1, 1] ]

a.sort(key= lambda x : ( x[1], x[0], x[2]) )
print(a, end=" ")

결과
[[3, 1, 1], [3, 1, 9], [5, 1, 5], [3, 5, 5]] 

* 이중 리스트로 이루어진 리스트를 정렬하려면 튜플을 사용해야 함. """