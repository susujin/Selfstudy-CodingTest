#예제10-6 커리큘럼

#N개의 강의를 듣고자 한다. 
#모든 강의는 1번부터 N번까지의 번호를 가진다. 
#동시에 여러 강의 수강 가능
#N개의 강의에 대하여 수강하기 까지 걸리는 최소 시간을 출력

from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
    
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, v+1):
        print(result[i])
    
topology_sort()