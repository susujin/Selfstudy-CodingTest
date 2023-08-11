#예제3-2 큰 수의 법칙
#배열의 크기 N, 숫자가 더해지는 횟수 M
#단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음.

n, m, k = map(int, input("N, M, K를 입력해주세요 > ").split()) # 각 변수를 공백으로 구분하여 입력받는다.
number_list = list(map(int, input("숫자 리스트를 입력해주세요 > ").split()))

number_list.sort() #숫자 리스트 정렬
big_first = number_list[n-1]
big_second = number_list[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += big_first
        m -= 1

    if m == 0:
        break
    result += big_second
    m -= 1

print(result)

#위의 문제에서 반복되는 수열에 대해 파악을 해야한다.
#M을 (K+1)로 나눈 몫이 수열의 반복되는 횟수가 된다.
#여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.
#M이 (K+1)로 나누어 떨어지지 않는 겨웅도 고려해야하므로, M을 (K+1)로 나눈 나머지만큼 가장 큰수가 추가로 더해지므로 이를 고려해주어야한다.
# 즉, int(M / (K+1)) * K + M % (K+1)

n, m, k = map(int, input("N, M, K를 입력해주세요 > ").split()) # 각 변수를 공백으로 구분하여 입력받는다.
number_list = list(map(int, input("숫자 리스트를 입력해주세요 > ").split()))

number_list.sort() #숫자 리스트 정렬
big_first = number_list[n-1]
big_second = number_list[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count)*big_first
result += (m-count) * big_second
print(result)