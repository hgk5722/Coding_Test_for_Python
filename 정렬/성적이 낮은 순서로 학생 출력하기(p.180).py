n = int(input()) 
student = []
for i in range(n):
    data = input().split()
    student.append((data[0], int(data[1]))) 

student.sort(key = lambda x : x[1]) 

for i in student:
    print(i[0], end=' ') 