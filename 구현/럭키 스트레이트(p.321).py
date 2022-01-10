data = input()

sum_left = 0
sum_right = 0

point = len(data)//2

for i in range(point-1 + 1):
    sum_left += int(data[i])

for i in range(point, point*2):
    sum_right += int(data[i])

if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")
