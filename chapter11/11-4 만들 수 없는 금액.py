#Q4 만들 수 없는 금액

# [문제]
# N개의 동전, 이때 N개의 동전을 이용하여ㅜ 만들 수 없는 양의 정수 금액 중 최솟값을 구해라!
# 예를 들어 N = 5, 각 동전이 각 3원, 2원, 1원, 9원짜리 라고 가정하면 이 때 만들 수 없는 최솟값은 8이다.


# [입력]
# 5
# 3 2 1 1 9

n = int(input("동전 개수 N을 입력해주세요 > "))
money_unit = list(map(int, input().split()))
money_unit.sort()

made_it = 1 #만들어야 하는 값

for i in money_unit:
    if made_it < i: #만들어야하는 값이 i보다 작으면 만들 수 없음
        break
    made_it += i

print(made_it) #만들어야하지만 할수 없는 값 출력