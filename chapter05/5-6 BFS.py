#    1-----2
#  /  \     \
#  3   \     7
# |  \  \  / |
# 4---5   8  6

#예제5-6 BFS
#1. 시작노드 '1'부터! 큐에 '1' 삽입
#2. '1'과 인접 노드는 '2','3','8'. '1'을 삭제하고, 인접노드 모두 큐에 삽입
#3. 제일 앞에 있는 '2'를 삭제하고, 인접노드 '7' 삽입
#4. '3'을 삭제하고, 인접 노드 '4','5' 모두 큐에 삽입
#5. '8'을 삭제하고, 인접노드가 없으므로 패스
#6. '7'을 삭제하고, 인접노드 '6' 삽입
#7. 남아 있는 노드에 방문하지 않은 인접 노드 없음. 따라서 남아있는 모든 노드를 차례대로 꺼냄. 4,5,6

#결론: 노드의 탐색순서(스택에 넣은 순서)
# 1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6

from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
BFS(graph, 1, visited)