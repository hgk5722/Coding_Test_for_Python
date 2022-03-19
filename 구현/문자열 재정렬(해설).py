data = input()
result = []
sum = 0
# 입력된 문자를 하나씩 확인
for i in data:
    # 문자열이 알파벳인지 확인.
    if i.isalpha(): 
        result.append(i)
    else: # 아니라면 모두 더함
        sum += int(i)
# 추가된 리스트들을 오름차순으로 정리
result.sort()
# sum != 0인 이유는 문자열 data에 숫자가 하나도 없을 경우 sum = 0이 되므로
# 0을 뒤에 붙힐 수는 없어서.
if sum != 0:
    result.append(str(sum))
# 리스트를 공백없이 문자열로 변환해서 출력
print(''.join(result))