n = int(input()) 
data = []
for i in range(n):
    data.append(int(input())) 

data.sort(reverse = True) # 역순으로 정렬
for i in data:
    print(i, end=' ') # 공백을 사이에 두고 출력하는 방법