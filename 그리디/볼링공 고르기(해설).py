n, m = map(int, input().split())
data = list(map(int, input().split()))
# 1~10까지의 무게를 가진 볼링공 담는 리스트
array = [0] * 11
for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
result = 0

for i in range(1, m+1):
    n -= array[i] # 특정 무게를 가진 볼링공의 개수 전체에서 빼서 전체개수 갱신
    result += array[i] * n # 갱신된 전체 개수는 array[i] 무게를 가진 볼링공을 고를때 남은 경우의 수 
print(result)

