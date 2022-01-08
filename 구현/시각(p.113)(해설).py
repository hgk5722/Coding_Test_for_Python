h = int(input())

count = 0
# 시간의 단위는 24시간 60분 60초
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매시각에 문자열 '3'이 포함되어 있는지 확인
            if "3" in str(i) + str(j) + str(k):
                # 반복 변수들을 문자열로 변환
                count += 1
print(count)

# 나는 시간 관련 문제가 나오면 끝자리가 10이 아닌 60으로 끝나는거에 대해 힌트를 못찾곤한다.
# 파이썬에서는 in 함수를 사용할 수 있다는것을 기억