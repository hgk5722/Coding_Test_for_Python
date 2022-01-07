# data = list(map(int, input()))
# input()은 문자열로 받기 때문에 배열로 바로 사용 가능
data = input()
count_0 = 0 # 0의 그룹 수
count_1 = 0 # 1의 그룹 수
if data[0] == "1": # 첫인덱스로 그룹 수 추가
    count_1 += 1
else:
    count_0 += 1
for i in range(len(data)):
    if data[i-1] != data[i]: #배열값이 다를경우
        if data[i] == "1":
            count_1 += 1
        else:
            count_0 += 1
# 둘중 낮은 그룹 출력
print(min(count_0, count_1))

# 이어져 있는 문자열에서 옆 문자를 비교하는 신박한 방법이 있을줄 알았다.
# 그런건 없었고 이미 알던 array[i] != array[i+1]가 정답이었다.(외울것!!)
# input()은 문자열로 받으니 "1"로 입력해야 제대로된 값이 출력된다.
