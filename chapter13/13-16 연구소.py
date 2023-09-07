#Q16 연구소 (에러발생, 다시시도해야함.)

# [문제]
# 연구소는 크기가 N*M인 직사각형으로 나타낼수 있으며, 직사각형은 1*1 크기의 정사각형으로 나누어져있음.
# 연구소는 빈칸, 벽으로 이루어져있으며, 벽은 칸 하나를 가득 차지

# 일부칸에는 바이러스 존재, 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈수 있다. 
# 새로 세울수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야함.

# 0은 빈칸, 1은 벽, 2는 바이러스

# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램 작성

# [입력]
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

#실패ㅠㅠ 메모리
import sys
sys.setrecursionlimit(10**7)

n,m = map(int,input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int,input().split())))

#방향 북동남서
dx = [0,1,0,-1]
dy = [-1,0,1,0]

safe_area = 0
wall_count = 3
new_lab = [[0]*m for _ in range(n)]

# 벽세우기
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            for dir in range(4):
                nx = i + dx[dir]
                ny = j + dy[dir]

                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if wall_count != 0 and lab[nx][ny] == 0:
                        lab[nx][ny] = 1
                        wall_count -= 1

#바이러스 함수
def virus(i,j):
    for dir in range(4):
        nx = i + dx[dir]
        ny = j + dy[dir]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if lab[nx][ny] == 0:
                lab[nx][ny] == 2
                virus(nx,ny) #전파된 곳 주변 또 탐색


for i in range(n):
    for j in range(m):
        #바이러스전파
        if lab[i][j] == 2:
            virus(i,j)
        #안전지역 확인
        if lab[i][j] == 0:
            safe_area += 1         

print(safe_area)



#다시 시도!! 런타임 에러 (RecursionError), 메모리 초과...
n,m = map(int,input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int,input().split())))

new_lab = [[0]*m for _ in range(n)]

#방향 북동남서
dx = [0,1,0,-1]
dy = [-1,0,1,0]

result = 0

#안전지역 확인(함수로 바꿈)
def safe_area_score():
    safe_area = 0
    for i in range(n):
        for j in range(m):
            if new_lab[i][j] == 0:
                safe_area += 1
    return safe_area

#바이러스전파 함수
def virus(i,j):
    for dir in range(4):
        nx = i + dx[dir]
        ny = j + dy[dir]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if new_lab[nx][ny] == 0:
                new_lab[nx][ny] == 2
                virus(nx,ny) #전파된 곳 주변 또 탐색

# 벽세우기(다 고침ㅎㅎ, 책참고)
def wall(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                new_lab[i][j] = lab[i][j]

        #바이러스 전파
        for i in range(n):
            for j in range(m):
                if new_lab[i][j] == 2:
                    virus(i,j)
        
        result = max(result, safe_area_score())
        return
    
    #울타리
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                wall(count)
                lab[i][j] = 0
                count -= 1

wall(0)
print(result)