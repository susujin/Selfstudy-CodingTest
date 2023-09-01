#Q10 자물쇠와 열쇠

# [문제]
# 잠겨있는 자물쇠는 한칸의 크기가 1*1인 N*N 크기의 정사각 격자 형태이고, 특이한 모양의 열쇠는 M*M 크기인 정사각 격자 형태로 되어 있다.
# 자물쇠에는 홈이 파여있고 열쇠 또한 홈과 돌기 부분이 있다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열림.
# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질때, 
# 열쇠로 자물쇠를 열수 있으면 true, 열수 없으면 false를 return 하도록 solution 함수를 완성하세요

# [입력]
# key                             lock                            result
# [[0,0,0],[1,0,0],[0,1,1]]       [[1,1,1],[1,1,0],[1,0,1]]       true

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

# 키 회전
# 1 2 3        7 4 1        9 8 7         3 6 9
# 4 5 6   ->   8 5 2   ->   6 5 4     ->  2 5 8
# 7 8 9        9 6 3        3 2 1         1 4 7
def rotation_90(key):
    n = len(key)
    rotation_key_list = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotation_key_list[j][n-1-i] = key[i][j]
    return rotation_key_list

#lock이 1인지 아닌지 확인
def check(lock):
    n = len(lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    #자물쇠 크기를 3배로 바꿈
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    #3배가 된 자물쇠 중앙에 기존 자물쇠 넣기
    # □ □ □
    # □ ■ □
    # □ □ □
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotation_90(key) #90도 회전

        for x in range(1,n*2):
            for y in range(1,n*2):

                #자물쇠에 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                #검사
                if check(new_lock):
                    return True
                
                #자물쇠에서 열쇠 제거
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False

print(solution(key,lock))