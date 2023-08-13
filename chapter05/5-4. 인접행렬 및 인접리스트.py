#인접 행렬 방식(Adjacency Matrix)
#2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
#연결이 되어 있지 않은 노드끼리는 무한(infinity)의 비용이라고 작성

#인접 리스트 방식(Adjacency List)
#데이터를 어떤 방식으로 저장할까? 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장

#예제5-4 
#인접행렬
INF = 999999999 #무한의 비용
graph =[
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)

#인접리스트
graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)