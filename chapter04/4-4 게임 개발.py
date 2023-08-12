# 어려움!!! 내 코드로 다시 만들도록!!!

#예제4-4 게임 개발
#캐릭터가 있는 장소는 1*1크기의 정사각형으로 이루어진 N*M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
#맵의 각 칸은(A,B)로 표현, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수
#캐릭터는 동서남북 중 한 곳을 바라본다.
#캐릭터는 상하좌우로 움직일 수 있고, 바다는 갈 수 없음

#매뉴얼
#1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
#2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽방향으로 회전한 다음 왼쪽으로 한칸을 전진한다. 
#   왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
#3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 잇는 칸인 경우에는, 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다.
#   단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

#방향 d => 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽
#맵 정보 => 0:육지, 1:바다

n, m = map(int, input("세로크기 N과 가로크기 M을 입력해주세요 > ").split())
location_a, location_b, direction = map(int, input("캐릭터의 좌표 a,b와 바라보는 방향 d를 입력해주세요 > ").split())
currently_ab = [[0] * m for _ in range(n)] #방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화(?이거 뭐지..?)
currently_ab[location_a][location_b] = 1

map_info = [] #맵 n*m
for i in range(n):
    map_info.append(list(map(int, input().split()))) 

#북동남서
x = [-1,0,1,0] #위아래
y = [0,1,0,-1] #양옆

### 여기부터 이해 못함...뭐지...
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =3
    
count = 1
turn_time = 0
while True:
    turn_left()
    nx = location_a + x[direction]
    ny = location_b + y[direction]

    if currently_ab[nx][ny] == 0 and map_info[nx][ny] == 0:
        currently_ab[nx][ny] = 1
        location_a = nx
        location_b = ny
        count += 1
        turn_time = 0 
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = location_a - x[direction]
        ny = location_b - y[direction]
        if map_info[nx][ny] == 0:
            location_a = nx
            location_b = ny
        else:
            break
        turn_time = 0

print(count)