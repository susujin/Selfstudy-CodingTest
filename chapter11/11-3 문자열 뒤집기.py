#Q3 문자열 뒤집기

# [문제]
# 문자열 S는 0과 1로만 이루어짐
# 문자열 S를 모두 같은 숫자로 만드려고함. 
# 예를들어 0001100일때,
# 1. 전체를 뒤집으면 1110011
# 2. 4번째부터 5번째문자까지 뒤집으면 1111111이 되어 두번만에 모두 같은 숫자로 만들수 있다.
# 그러나, 처음부터 4,5번을 0으로 뒤집으면 한번에 0000000을 만들수 있다.
# 뒤집는 최소 횟수 구하기

# [입력]
# 0001100

s = list(map(str, input()))
print(s)

count_0 = 0
count_1 = 0

if s[0] == '0':
    count_1 += 1
else:
    count_0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            count_0 += 1
        else:
            count_1 += 1

print(count_0, count_1)
print(min(count_0, count_1))