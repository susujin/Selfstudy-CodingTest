#Q1 모험가 길드

# [문제]
# 모험가 n명, n명의 모험가 대상으로 '공포도' 측정
# 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가가 그룹에 참여해야 여행을 떠날 수 있음
# 몇 명의 모험가는 마을에 그대로 남아 있을 수 있음.
# 최대 몇개의 모험가 그룹을 만들 수 있나?
# n명의 모험가에 대한 정보가 주어졌을 떄 여행을 떠날 수 있는 그룹의 최댓값을 구하는 프로그램 작성

# [입력]
# 인원수 5
# 각 모험가의 공포도 2 3 1 2 2

n = int(input("모험가의 인원수(n)를 입력해주세요 > "))
score_list = list(map(int, input("각 모험가의 공포도를 입력해주세요 > ").split()))
score_list.sort()

group_count = 0 #만들어진 그룹 수
now_count = 0 #현재 그룹에 들어온 모험가 수

for i in score_list:
    now_count += 1
    if now_count >= i:
        group_count += 1 #그룹 수 +1
        now_count = 0 #현재 그룹에 들어온 모험가 수 초기화

print(group_count)