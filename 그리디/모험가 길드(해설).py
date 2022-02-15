n = int(input())
data = list(map(int, input().split()))
data.sort() # 오름차순으로 정렬

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수
for i in data: # 공포도 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if i > count: # 공포도(i)가 인원수가 작으면 그룹 생성 불가.  
        continue    # 인원을 더 채울 수 있음.
    else: 
        result += 1 # 총 그룹의 수 증가
        count = 0 # 현재 그룹의 포함된 모험가의 수 초기화
print(result) # 총 그룹의 수 출력

