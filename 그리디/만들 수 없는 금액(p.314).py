n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1 # (target - 1) 까지는 모두 만들 수 있다고 가정
for coin in coins:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < coin:
        break
    target += coin

print(target)
""" 
4
1 2 3 8

target = 1
1 + 1 = 2

2 + 2 = 4 = target

3 = 1 + 2

4 + 3 = 7 = target
4
2 + 3 = 5
1 + 2 + 3 = 6

7 + 8 = 15
7은 만들 수 없다. """
