#Q2 곱하기 혹은 더하기

# [문제]
# 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 또는 '+' 연산자를 넣어 결과적으로 가장 큰 수를 만드는 프로그램 작성
# 단, 일반적인 연산과 달리 모든 연산은 왼쪽부터 오른쪽으로!!

# [입력]
# 02984 or 567

num = list(map(int, input()))
hap = 0

for i in range(len(num)):
    if hap + num[i] >= hap * num[i]:
        hap += num[i]
    else:
        hap *= num[i]

print(hap)

#다른 코드
data = input()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)