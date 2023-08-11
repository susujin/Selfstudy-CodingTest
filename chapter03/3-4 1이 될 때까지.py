#예제3-4 1이 될 때까지
#어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복저으로 선택하여 수행하려고 한다.
#단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
#1. N에서 1을 뺀다. 2. N을 K로 나눈다.

n, k = map(int, input("N과 K를 입력해주세요 > ").split()) # 각 변수를 공백으로 구분하여 입력받는다.
count = 0

while n >= k:
    while n % k != 0:
        n = n - 1
        count += 1
    n = n // k
    count += 1
        
while n > 1:
    n -= 1
    count += 1

print(count)

#다른 방법
n, k = map(int, input("N과 K를 입력해주세요 > ").split())
result = 0

while True:
    target = (n//k)*k
    result += (n - target)
    n = target

    if n<k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)