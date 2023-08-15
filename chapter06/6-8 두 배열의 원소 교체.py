#예제6-8 두 배열의 원소 교체
#두개의 배열 A,B  |  두 배열은 N개의 원소로 구성, 모두 자ㅏ연수
#최대 K번의 바꿔치기 연산을 수행하는데
#바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
#목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것

n, k = map(int, input("원소의 개수 N과 바꿔치기를 수행할 최대 횟수 K를 입력해주세요 > ").split())
a = list(map(int, input().split())) #배열 a
b = list(map(int, input().split())) #배열 b

a.sort() #오름차순
b.sort(reverse=True) #내림차순

for i in range(k):
    if a[i] < b[i]: #a보다 b가 크면 둘이 교체
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))