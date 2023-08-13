#예제5-8 미로 탈출
#BFS활용
#N*M 크기의 직사각형 형태의 미로
#현재 위치 (1,1)
#미로 출구 (n,m)
#괴물이 있는 부분은 0, 없는 부분은 1
# 탈출하기 위해 움직여야 하는 최소 칸의 개수

from collections import deque
n, m = map(int, input("세로크기 N과 가로크기 M을 입력해주세요 > ").split())
# 미로 만들기
maze = [] 
for i in range(n):
    maze.append(list(map(int,input())))

#이동방향 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def connect_0(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            ### 여기부터 이해 못함...뭐지...
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
        
    return maze[n-1][m-1]

print(connect_0(0,0))