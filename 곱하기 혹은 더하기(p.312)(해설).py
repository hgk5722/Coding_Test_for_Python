data = list(map(int, input()))

data.sort()
# 첫 리스트를 
result = data[0]

for i in range(1, len(data)):
    num = data[i] # 인덱스가 아닌 리스트의 값
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
print(result)

# 처음 문제를 봤을때 0이 나오는 경우만 예외처리해주면 된다고 생각했었다.
# 0, 1 모두 처리해 줘야함