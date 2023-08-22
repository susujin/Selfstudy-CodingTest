#예제9-5 전보
#어떤 나라에는 N개의 도시가 있다.
#각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 ㄱ보내서 다른 도시로 해당 메시지를 전송할 수 있다.
#X도시에서 Y도시로 전보를 보내려면 통로가 있어야한다.

#어느날 C라는 도시에서 위급 상황 발생. C에서 보낸 메시지를 받게된느 도시의 개수는 총 몇 개 이며 도시들이 모두 메시지를 받는데 걸리는 시간은 얼마인가?

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: #큐가 비어 있지 않다면
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

#도달할 수 있는 노드 개수
count = 0
#도달할 수 있는 노드 중 가장 멀리 있는 노드와의 최단거리
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)
