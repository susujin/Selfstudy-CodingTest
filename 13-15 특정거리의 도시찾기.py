#Q15 특정 거리의 도시 찾기

# [문제]
# 1~N번까지의 도시와 M개의 단방향 도로가 존재
# 모든 도로의 거리는 1
# 이때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시중에서, 최단거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성
# x -> x 거리는 0

# 예를들어 N=4, K=2, X=1일때 
# 1번도시에서 출발하여 도달할 수 있는 도시 중에 최단거리가 2인 도시는 4번뿐
# 2,3번 도시의 경우 최단거리가 1이기때문에 출력X

# 1  →  2
# ↓  ↙  ↓
# 3     4

# [입력]
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

from collections import deque

n,m,k,x = map(int,input().split())
road = [[] for _ in range(n+1)] #도시 개수 만큼 길 리스트 만들기

for i in range(m):
    a,b = map(int, input().split())
    road[a].append(b)

#노드와 노드 사이 거리를 -1로 초기화
distance = [-1] * (n+1) 
#x -> x는 0
distance[x] = 0

start = deque([x]) #시작점

while start:
    #현재도시 뽑고
    now_city = start.popleft()
    #갈수있는곳 찾기
    for next in road[now_city]:
        if distance[next] == -1: #안간곳이면 최단거리로 갱신
            distance[next] = distance[now_city] + 1
            start.append(next)

check = False
for j in range(1,n+1):
    if distance[j] == k: #거리가 k면 출력
        print(j)
        check = True

if check == False:
    print(-1)