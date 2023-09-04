#Q13 치킨 배달

# [문제]
# 크기가 N*N인 도시가 있고, 도시는 1*1크기의 칸으로 나누어져 있습니다.
# 도시의 각 칸은 빈칸, 치킨집, 집 중 하나
# 도시의 칸은 (r,c)와 같은 형태로 나타내고, r행 c열 또는 위에서 부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미합니다. r과 c는 1부터 시작

# 치킨거리는 집과 가장 가까운 치킨집 사이의 거리입니다. 즉, 치킨 거리는 집 기준 정해지며, 각각의 집은 치킨 거리를 가지고 있습니다.
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합입니다.

# 예시)
# 0 2 0 1 0
# 1 0 1 0 0 
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 0 1 2

# 0은 빈칸 1은 집, 2는 치킨집
# (2,1)에 있는 집과 (1,2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2
# (5,5)에 있는 치킨집과의 거리는 |2-5| + |1-5| = 7입니다. 
# 따라서 (2,1)에 있는 집의 치킨거리는 2입니다.

# 이도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개!
# 도시에 있는 치킨집중 최대 M개를 고르고, 나머지는 폐업
# 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램 작성

# [입력]
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0 
# 0 0 1 0 0 
# 0 0 0 0 2

#파이썬 조합
from itertools import combinations

n,m = map(int,input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [],[]

for r in range(n):
    for c in range(n):
        #집 1
        if city[r][c] == 1:
            house.append((r,c))
        #치킨집 2
        elif city[r][c] == 2:
            chicken.append((r,c))

#치킨집 최대 m개 고르기. 조합 사용. 치킨집을 m개씩 묶기
chicken_list = list(combinations(chicken,m))

def get_chicken_distance(chicken_list):
    value = 0
    for x,y in house:
        distance = 1e9
        for a,b in chicken_list:
            distance = min(distance, abs(x-a) + abs(y-b))
        value += distance
    return value

result = 1e9
for i in chicken_list:
    result = min(result, get_chicken_distance(i))
print(result)