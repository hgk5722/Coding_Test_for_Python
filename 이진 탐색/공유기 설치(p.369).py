# 떡볶이 떡 만들기와 비슷한 파라메트릭 서치 문제
n, c = list(map(int, input().split(' '))) 
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진 탐색을 위해 정렬

start = 1 # 가능한 최소 거리(min gap) 
end = array[-1] - array[0] # 가능한 최대 거리(max gap) 
result = 0

while start <= end:
    # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미함 
    mid = (start + end) // 2
    value = array[0] # 최신 공유기 설치 위치 
    count = 1 # 공유기의 대수 
    # 현재의 mid값을 이용해 공유기를 설치 
    for i in range(1, n): # 앞에서부터 차근차근 설치 
        if array[i] >= value + mid: # 최신 공유기 설치 위치 + gap <= 현재의 거리값이면
            value = array[i] # 현재위치에 공유기 설치
            count += 1 # 공유기 대수 증가 
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        # 문제조건 : 인접한 공유기의 최대거리를 구해야 함 -> c개 이상 설치 가능(아직은 최적값이 아님) ->
        # -> start값을 늘리면 mid(gap)값 증가 -> 반복하면서 최적gap 구할 수 있음 
        start = mid + 1 
        result = mid # 적어도 C개 이상 설치해야 하니까 그 당시 최적의 값 저장 
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소 
        end = mid - 1
print(result) 