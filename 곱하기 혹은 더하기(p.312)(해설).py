data = list(map(int, input()))

data.sort()
# 첫 리스트를 결과값으로 설정!!
result = data[0]

for i in range(1, len(data)):
    num = data[i] # 인덱스가 아닌 리스트의 값
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
print(result)

# 처음 생각 : 0만 예외처리, count()이용해서 0의 개수 파악하고 
# zero변수 선언 후 data[zero]부터 리스트 끝까지 곱하면 된다고 생각함