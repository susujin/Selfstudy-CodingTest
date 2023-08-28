#Q5 볼링공 고르기

# [문제]
# A와 B가 볼링을 친다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 한다.
# 볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀있고, 공의 번호는 1번부터 순서대로 부여된다.
# 또한 무게가 같은 공이 여러개 있을 수 있지만, 서로 다른 공으로 간주한다.
# 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재

# 예를 들어 N = 5, M = 3, 각각의 무게가 1,3,2,3,2일때
# 볼링공 번호의 조합은 다음과 같다.

# (1,2) (1,3) (1,4) (1,5) (2,3) (2,5) (3,4) (4,5) 8가지
# 볼링공을 고르는 경우의 수 구하기!!

# [입력]
# 5 3
# 1 3 2 3 2

n,m = map(int, input().split())
ball_weight = list(map(int, input().split()))

comb = []

for i in range(len(ball_weight)-1):
    for j in range(len(ball_weight)):
        if i < j:
            if ball_weight[i] != ball_weight[j]:
                comb.append((ball_weight[i], ball_weight[j]))
                print(comb)

print(len(comb))

#다른 코드
n,m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)