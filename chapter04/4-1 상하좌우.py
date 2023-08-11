#구현
#머릿속에 있는 알고리즘을 정확하고 빠르게 프로그램으로 작성하기
#흔히 문제 해결 분야에서 구현 유형의 문제는 '풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제'를 의미한다.
#완전탐색: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
#시뮬레이션: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행
#파이썬은 다른 언어에 비해서 구현상의 복잡함이 적은 편이지만 데이터 처리량이 많을 때는 꼭 메모리 제한을 고려해야한다!!!

#예제4-1 상하좌우
#N*N 크기의 정사각형
#L:왼쪽으로 한칸이동, R:오른쪽으로 한칸이동, U:위로 한칸이동, D:아래로 한칸이동

n = int(input("숫자 n을 입력하세요 > "))
move = list(map(str, input("방향을 입력해주세요 > ").split()))
location_x, location_y = 1,1

for i in move:
    if location_x == 0 or location_y == 0 or location_x > n  or location_y > n:
        continue
    else:
        if i == "L":
            location_y -= 1
        elif i == "R":
            location_y += 1
        elif i == "U":
            location_x -= 1
        elif i == "D":
            location_x += 1

        if location_x == 0:
            location_x += 1
        elif location_x > n:
            location_x -= 1
    
print(location_x, location_y)

#다른 방법
n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x,y = nx, ny

print(x,y)