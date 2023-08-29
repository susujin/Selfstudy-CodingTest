#Q6 무지의 먹방 라이브

# [문제]
# 회전판에 먹어야할 N개의 음식이 있다. 각 음식에는 1부터 N까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요
# 다음과 같은 방법으로 음식 섭취
# 1. 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓습니다.
# 2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 옵니다.
# 3. 무지는 음식 하나를 1초동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취합니다.
#     다음 음식이란, 아직 남음 음식 중 다음으로 섭취해야할 가장 가까운 번호의 음식을 말합니다.
# 4. 회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정합니다.

# 먹방을 시작한지 K초 후에 네트워크 장애로 인해 방송이 잠시 중단. 네트워크 정상화 후 다시 방송을 이어 갈 때 몇번 음식부터 섭취해야하는지를 알고자 한다.
# 각음식을 모두 먹는데 필요한 시간이 담겨 있는 배열 food_times, 네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하세요.

# [입력]
# food_ times     k   result
# [3,1,2]         5   1

n = int(input("먹어야할 음식 개수 N을 입력해주세요 > "))
food_times = list(map(int, input().split())) #음식을 먹는데 걸리는 시간
k = int(input("방송이 중단된 시간(초) K를 입력해주세요 > "))

# 실패...ㅋㅋㅋㅋㅋ
# def solution(food_times, k):
#     answer = -1
#     change_k = k

#     while change_k != 0:
#         for i in range(len(food_times)):
#             if food_times[i] != 0: #리스트의 요소가 0이 아닐때
#                 food_times[i] -= 1
#                 change_k -= 1 #초 줄이기
#                 answer = 1 #섭취할 것이 있으면 1
#             else:
#                 answer = -1  #섭취할 것이 없으면 -1
#     return answer

# print(solution(food_times, k))
# [결과]
# 정확성: 8.0
# 효율성: 0.0
# 합계: 8.0 / 100.0

# 다시시도
import heapq
def solution(food_times, k):

    #전체 음식을 먹는 시간보다 네트워크 지연 시간이 크거나 같다면
    if sum(food_times) <= k:
        return -1

    #시간이 작은 음식부터 제거하기 위해 우선순위 큐 사용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) #(음식시간, 음식번호) 형태로 삽입

    food_count = len(food_times) #남은 음식 개수
    use_time = 0 #음식을 먹기 위해 사용한 시간
    previous_use_time = 0 #이전 음식을 먹기 위해 사용한 시간

    #음식을 먹기 위해 사용한 시간 + (현재음식 시간 - 이전음식 시간) * 현재음식개수 <= k
    while use_time + ((q[0][0] - previous_use_time) * food_count) <= k:
        now=heapq.heappop(q)[0] #현재음식 제거
        use_time += (now - previous_use_time) * food_count #음식을 먹기 위해 사용한 시간 추가
        food_count -= 1 #남은 음식 개수 -1
        previous_use_time = now #이전 음식 시간 재설정
    
    #남은 음식 중 몇번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x:x[1]) #음식번호 기준으로 정렬
    return result[(k-use_time) % food_count][1]

print(solution(food_times, k))
#성공!! 이지만 어렵다....
#사실 반성공ㅎㅎ 책참고
#heapq사용해야함