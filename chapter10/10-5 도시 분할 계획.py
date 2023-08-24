#예제10-5 도시 분할 계획

#마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.
#이장은 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다.
#각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야한다.

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort()
last = 0

for edge in edges:
    cost,a,b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)