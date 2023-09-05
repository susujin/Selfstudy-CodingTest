#Q14 외벽 점검

#많이 어려움...ㅠㅠ
#100% 책 참고
#다시풀어보기!!

# [문제]
# 레스토랑의 구조는 완전히 동그란 모양이고, 외벽의 총 둘레는 n 미터이며, 외벽의 몇몇 지점은 추위가 심할 경우 손상될 수도 있는 취약한 지점들이 있다.
# 따라서 내부 공사 도중에도 외벽의 취약 지점들이 손상되지 않았는지, 주기적으로 친구들을 보내서 점검하기로 했다.
# 다만, 빠른 공사진행을 위해 점검시간을 1시간으로 제한

# 친구들이 1시간 동안 이동할 수 있는 거리는 제각각, 최소한의 친구들을 투입해 취약 지점 점검하고 나머지 친구들은 내부공사를 돕도록함
# 편의상 레스토랑의 정북 방향 지점을 0으로 나타내며, 취약 지점의 위치는 정북 방향 지점으로 부터 시계방향으로 떨어진 거리로 나타냄
# 또, 친구들은 출발지점부터 시계 혹은 반시계 방향으로 외벽을 따라 이동함.

# 외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간동안 이동할 수 있는거리가 담긴 배열 dist가 매개변수로 주어질때,
# 취약 지점을 점검하기 ㅜ이해 보내야하는 친구 수의 최솟값을 return 하도록 solution 함수 완성하세요

# [입력]
# n       weak            dist            Result
# 12      [1,5,6,10]      [1,2,3,4]       2
# 12      [1,3,4,9,10]    [3,5,7]         1

#파이썬 순열
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        #weak 길이를 2배로 늘리기
        weak.append(weak[i] + n)

    #투입할 친구 수의 최솟값 초기화
    answer = len(dist) + 1 

    for st in range(length):
        for fr in list(permutations(dist,len(dist))):
            count = 1 #투입할 친구 수
            position = weak[st] + fr[count - 1] #친구가 점검할 수 있는 마지막 위치
            
            for a in range(st, st + length):
                #점검위치에서 벗어나는 경우
                if position < weak[a]:
                    count += 1
                    #투입불가
                    if count > len(dist):
                        break
                    position = weak[a] + fr[count - 1]
            answer = min(answer, count) #최솟값
    
    if answer > len(dist):
        return -1
    return answer