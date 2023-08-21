#예제9-3 플로이드 워셜 알고리즘

INF = int(1e9)

n = int(input("노드의 개수 N을 입력하세요 > "))
m = int(input("간선의 개수 M을 입력하세요 > "))

graph = [[INF] * (n+1) for _ in range(n+1)]

#자기자신에서 자기자신으로 간느 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b], end = ' ')
    print()