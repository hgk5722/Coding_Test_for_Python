# 총 인원 수 n과 각 모험가의 공포도 입력
n = int(input())
data = list(map(int, input().split()))

count = 0 # 모험가 집단의 수
index = 0 # 리스트의 인덱스
# 모험가를 내림차순으로 정리
data.sort(reverse = True)
# 모험가의 수 n이 양수일때까지 반복
while n > 0:
    # 모험가 인덱스의 값 모험가 수 n에서 빼줌
    n -= data[index]
    # 한번 빼준만큼 모험가 집단 수 증가
    count += 1
    # 인덱스값도 마지막을 가리킴
    index += (1 + n)
print(count)
# 다 끝나고 나면 인덱스는 마지막을 가리킴 == 처음 입력받은 n의 값 -1 
