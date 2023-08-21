#예제9-2 개선된 다익스트라 알고리즘
# 힙(Heap) 자료구조 사용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

#각 노드에 연결되어 잇는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 
visited = [False] * (n+1)
#최단 거리 테이블 모드 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

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

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

#어렵다...