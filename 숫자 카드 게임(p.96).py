# 행과 열을 나타내는 n, m을 입력 받는다
n, m = map(int, input().split())
# 마지막 결과값을 출력할 result를 초기화
result = 0
# 한 줄씩 입력받아 확인
for i in range(n): # 행의 개수만큼 반복
    # 한 줄씩 입력 받아 작은 수 판별
    data = list(map(int, input().split()))
    mini = min(data) # 기본 내장 함수
    result = max(result, mini)

print(result)