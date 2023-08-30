#Q7 럭키 스트레이트

# [문제]
# 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황
# 예를 들어, 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1+2+3 = 6, 오른쪽 부분의 각 자릿수의 합의 4+0+2 = 6으로 동일하여 럭키 스트레이트 사용가능
# 점수 N이 주어졌을 때 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지 알려주는 프로그램 작성

# [입력]
# 123402 -> LUCKY
# 7755 READY

n = list(map(int, input("점수 N을 입력해주세요 > ")))
left = 0
right = 0

for i in range(len(n) // 2):
    left += n[i]
    right += n[(i+1)*-1]

if left == right:
    print("LUCKY")
else:
    print("READY")

#다른 코드
n = input()
length = len(n)
summary = 0

for i in range(length//2):
    summary += int(n[i])

for i in range(length//2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")