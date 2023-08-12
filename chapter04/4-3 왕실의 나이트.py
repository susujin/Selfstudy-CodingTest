#예제4-3 왕실의 나이트
#8*8 좌표 평면
#나이트는 말을 타고 있어 이동할 때는 L자 형태로만 이동할 수 있고, 정원 밖으로는 나갈 수 없다.

#나이트 이동방법 
#1. 수평으로 두칸 이동한 뒤에 수직으로 한 칸 이동하기
#2. 수직으로 두칸 이동한 뒤에 수평으로 한 칸 이동하기

#8*8의 좌표 평면에서 행 위치는 1부터 8로 표현, 열 위치는 a부터 h로 표현
#나이트가 이동할 수 있는 경우의 수 구하기

currently_location = input("나이트의 현재 위치를 입력하세요(예. a1) > ")
possible_move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,2)]
column_list = ('a','b','c','d','e','f','g','h')

row = int(currently_location[1]) #숫자
column = column_list.index(currently_location[0]) + 1 #영어

move_count = 0 # 이동 횟수, 결과
for i in possible_move:
    next_row = row + i[1]
    next_column = column + i[0]

    if next_row >= 1 and next_column >= 1 and next_row <= 8 and next_column <= 8:
        move_count += 1
    
print(move_count)