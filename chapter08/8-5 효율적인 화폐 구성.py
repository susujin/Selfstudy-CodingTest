#예제8-5 효율적인 화폐 구성
#N가지 종류의 화폐
#화폐들의 개수를 최소한으로 그 가치의 합이 M원이 되도록!
#예를들어 2,3원이 있을 때 15원을 만들기위해 3원을 5개 사용하는것이 최소한의 화폐 개수이다.

#불가능할 때는 -1 출력

n,m = map(int,input("화폐 종류 N개와 만들고자하는 값 M원을 입력해주세요 > ").split())
money_unit = [] #화폐 단위
for i in range(n):
    money_unit.append(int(input()))

#왜 10001로 초기화 할까?
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(money_unit[i], m+1):
        if d[j-money_unit[i]] != 10001:
            d[j] = min(d[j], d[j-money_unit[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])