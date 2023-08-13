#예제5-7 음료수 얼려 먹기
#DFS활용
#N*M 크기의 얼음 틀
#구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1
#구멍이 뚫려 있는 부분 끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 거승로 간주
#얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램

n, m = map(int, input("세로크기 N과 가로크기 M을 입력해주세요 > ").split())
# 맵 만들기
ice_map = [] 
for i in range(n):
    ice_map.append(list(map(int,input())))

# 4*5의 경우
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

#x,y에서 x는 세로, y는 가로. 즉 x는 4보다 크면 안됨. y는 5보다 크면 안됨

def connect_0(x,y):
    #범위 밖
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    #아직 이동 안함. 즉 방문 안했다면
    if ice_map[x][y] == 0:
        ice_map[x][y] = 1
        connect_0(x-1, y) #상
        connect_0(x+1, y) #하
        connect_0(x, y-1) #좌
        connect_0(x, y+1) #우
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if connect_0(i,j) == True:
            result += 1

print(result)