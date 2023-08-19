#예제9-1 간단한 다익스트라 알고리즘
#처음에 각 노드에 대한 최단거리를 담는 1차원 리스트 선언
#단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인

import sys
input = sys.stdin.readline
INF =int(1e9) #무한을 의미하는 값으로 10억을 설정

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

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])