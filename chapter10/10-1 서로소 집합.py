#예제10-1 서로소 집합

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False #사이클 발생 여부

# for i in range(e):
#     a,b = map(int, input().split())
#     union_parent(parent, a, b)

for i in range(e):
    a,b = map(int, input().split())
    #사이클 발생 여부 확인
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')

print()

print('부모 테이블: ', end = '')
for i in range(1, v+1):
    print(parent[i], end = ' ')

print()

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")


#경로 압축 기법
#위 코드에서 함수만 바꿔주면 됨.
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]