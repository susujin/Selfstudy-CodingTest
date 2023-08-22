#예제9-4 미래 도시
#1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있음
#방문 판매원 A는 현재 1번회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 함
#연결된 2개의 회산느 양방향 이동 가능

#방문 판매원 A는 소개팅도 참석하고자함
#소개팅의 상대는 K번 회사에 존재
#방문 판매원 A는 X번 회사에 가서 물건을 판매하기 전에 K번 회사를 방문하여 소개팅 후 이동

#예를들어 N = 5, X = 4, K = 5, 회사간 도로가 7개이면서 각 도로가 다음과 같이 연결되어 있을 때를 가정
#(1,2) (1,3) (1,4) (2,4) (3,4) (3,5) (4,5)
#이때 방문 판매원 a가 최종적으로 4번회사에 가는 경로를 1,3,5,4로 설정하면 소개팅에도 참석하면서 총 3만큼의 시간으로 이동할 수 있다.
#최소 이동시간은 3

INF = int(1e9)

n, m = map(int, input("전체 회사의 개수 N과 경로의 개수 M을 입력하세요 > ").split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
            