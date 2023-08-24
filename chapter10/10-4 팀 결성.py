#예제10-4 팀 결성

#0부터 N번까지의 번호 부여
#처음에는 모든 학생이 서로 다른팀으로 구분, 총 N+1개의 팀 존재
#1. '팀 합치기' 연산은 두 팀을 합치는 연산
#2. '같은 팀 여부 확인'연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산
#M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인'연산에 대한 연산결과를 출력하는 프로그램 작성

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

n,m = map(int, input().split())
parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('yes')
        else:
            print('no')
    