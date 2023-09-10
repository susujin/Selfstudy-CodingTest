#Q17 경쟁적 전염 (문제를 잘못 이해...ㅎㅎ 다시풀어야함)

# [문제]
# N*N 크기의 시험관
# 시험관은 1*1크기의 칸으로 나누어지며, 특정 위치에는 바이러스 존재
# 바이러스 종류는 1~K번 까지 K가지 있으며, 모든 바이러스는 이 중 하나

# 시험관에 존재하는 모든 바이러스는 1초마다 상,하,좌,우의 방향으로 증식. 매초 번호가 낮은 종류의 바이러스 부터 먼저 증식
# 이미 바이러스가 있다면 그 곳에는 다른 바이러스가 들어갈 수 없음.

# 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램 작성.
# 해당 위치에 바이러스가 없다면 0출력

# [입력]
# 3 3
# 1 0 2
# 0 0 0 
# 3 0 0 
# 2 3 2

n,k = map(int,input().split())

lab = [] #맵 정보
virus_info = [] #바이러스 정보
for i in range(n):
    lab.append(list(map(int,input().split())))
    for j in range(n):
        #바이러스가 있다면 바이러스 번호와 위치을 virus에 넣기
        if lab[i][j] != 0:
            virus_info.append((lab[i][j], i, j))

virus_info.sort() #낮은 바이러스 부터 정렬

#방향 북동남서
dx = [0,1,0,-1]
dy = [-1,0,1,0]

s,find_x,find_y = map(int,input().split())

while s != 0: #s가 0초 일때가지
    for i in range(len(virus_info)):
        for dir in range(4):
            nx = virus_info[i][1] + dx[dir]
            ny = virus_info[i][2] + dy[dir]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if lab[nx][ny] == 0:
                    lab[nx][ny] = virus_info[i][0]
                    
                    if s > 0:
                        s -= 1
                    else:
                        break
    
print(lab[find_x-1][find_y-1])
print(lab)