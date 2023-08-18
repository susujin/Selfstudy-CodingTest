#예제8-3 개미전사

#예를들어 1 3 1 5인 경우
#최소 한 칸 이상 떨어진 식량창고를 약탈해야한다.
#즉 2번째와 4번째를 선택해야 최댓값 8의 식량을 빼앗을 수 있다.

n = int(input("식량창고 개수 N을 입력해주세요 > "))
arr = list(map(int,input().split()))

d = [0] * 100

d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[n-1])