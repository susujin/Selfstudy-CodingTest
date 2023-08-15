#예제6-6 위에서 아래로 
#수열에 속해 있는 수의 개수 N
#내림차순으로 만들기

n = int(input('수열에 속해 있는 수의 개수를 입력해주세요. > '))
arr = []
for i in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end=' ')