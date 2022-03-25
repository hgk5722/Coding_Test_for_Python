n = int(input()) 
student = []
for i in range(n):
    data = input().split() # 공백으로 분리되는 데이터를 하나의 변수에 저장
    student.append((data[0], int(data[1]))) # 하나의 변수에 2개의 데이터를 담았으니 튜플로 구분해서 저장.

student.sort(key = lambda x : x[1]) # 원하는 부분을 기준으로 정렬

for i in student:
    print(i[0], end=' ') # 공백을 사이에 두고 출력