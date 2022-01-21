n, k = map(int, input().split()) 
a = list(map(int, input().split()))  # 리스트 컴프리핸션 이용해서 값 입력받기
b = list(map(int, input().split()))  

a.sort() # a는 오름차순 정렬
b.sort(reverse=True) # b는 내림차순 정렬 

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: # 정렬이 끝났는데 한번이라도 어긋나면 뒤에 내용은 계산할 필요 없으므로 
        break # break문으로 빠져나온다.

print(sum(a))  # 리스트 a의 합 sum(a)