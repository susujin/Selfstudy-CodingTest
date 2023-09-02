#Q11 뱀

# [문제]
# 'Dummy'라는 도스게임. 
# 이 게임에는 뱀이 나와서 기어 다니는데, 사과를 먹으면 뱀 길이가 늘어남. 
# 뱀이 이리저리 기어 다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝

# 게임은 N*N 정사각 보드 위에서 진행. 몇몇 칸에는 사과가 놓여져 있다.
# 게임 시작시 뱀은 맨 위 맨 좌측에 위치, 뱀의 길이는 1, 처음에 오른쪽으로 이동
# 뱀은 초마다 이동하는데 다음과 같은 규칙이 있다.
# - 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킵니다.
# - 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않습니다.
# - 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다. 즉, 몸의 길이는 변하지 않습니다.

# 사과의 위치와 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하세요.

# [입력]
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

#예시 맵
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 1 0 0 0
# 0 0 0 0 0 0

#보드의 크기 N
n = int(input())
#사과의 개수 K
k = int(input())

#보드정보
board = [[0] * (n+1) for _ in range(n+1)]
#사과정보 받아서 보드값에 1로 표시
for apple in range(k):
    bo_x,bo_y = map(int, input().split())
    board[bo_x][bo_y] = 1

#방향정보
direction = []
#방향 변환 횟수 L
l = int(input())
#방향정보입력
for way in range(l):
    x,c = input().split()
    direction.append((int(x), c))#x초 후 c('L' or 'D')로 90도 회전

#처음에 뱀머리는 오른쪽 -> (동남서북)
#오른쪽 회전: 동남서북 : +1
#왼쪽 회전: 동북서남 : -1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def rotation_snake(x,c):
    if c == "L":
        x = (x-1) % 4
    elif c == "D":
        x = (x+1) % 4
    return x

def solution():
    i,j = 1,1 #뱀 머리
    board[i][j] = 2 #뱀 머리 위치는 2로 표시
    snake_space = [(i,j)] #뱀이 차지하는 공간
    d = 0 #초기 동쪽 봄 ->
    time = 0 #초기 시간 0초
    next_rotation = 0 #다음 회전 정보
    
    while True:
        nx = i + dx[d]
        ny = j + dy[d]

        #보드 안에 있고, 뱀의 길이가 1이라면
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and board[nx][ny] != 2:
            #사과가 없는 칸이면 이동 후 끝에 -1
            #사과 칸은 1로 표시되어 있음
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                snake_space.append((nx,ny))
                px, py = snake_space.pop(0) #뱀이 차지하는 공간에서 첫번째 위치에 있는 값을 저장
                board[px][py] = 0 #위에서 저장한 값을 0으로 변경, 이자리는 뱀이 있는 자리가 아니기에
            
            #사과가 있는 칸이면 이동 후 끝부분 남겨두기
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                snake_space.append((nx,ny))

        #벽밖으로 나간다면, 즉 벽에 부딪혔다면
        else:
            time += 1
            break

        i,j = nx,ny #다음 위치로 이동
        time += 1

        #회전해야한다면
        if next_rotation < l and time == direction[next_rotation][0]:
            d = rotation_snake(d, direction[next_rotation][1])
            next_rotation += 1

    return time

print(solution())