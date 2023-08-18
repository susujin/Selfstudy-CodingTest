#예제7-3 부품찾기
#부품N개, 각 부품은 정수형태의 고유번호가 있다.
#어느날 손님이 M개 종류의 부품을 대량 구매함. 
#이때 가게에 부품이 모두 있는지를 확인하는 프로그램을 작성해보자

##이진탐색
#7-2에서 작성한 함수
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2 #중간값

        if arr[mid] == target:
            return mid
        elif arr[mid] > target: #중간값이 찾으려는 값보다 크면 왼쪽만 확인
            end = mid - 1
        else: #중간값이 찾으려는 값보다 작으면 오른쪽만 확인
            start = mid + 1
    return None
#

n = int(input("가게에 있는 부품 N개를 입력해주세요 > "))
unique_num_arr = list(map(int, input().split())) #가게에 있는 부품 고유번호
unique_num_arr.sort()

m = int(input("손님이 요청한 부품 M개를 입력해주세요 > "))
request_num_arr = list(map(int, input().split())) #손님이 요청한 부품 고유번호

for i in request_num_arr:
    result = binary_search(unique_num_arr, i, 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')


##계수정렬
n = int(input("가게에 있는 부품 N개를 입력해주세요 > "))
unique_num_arr = [0]*1000001

for i in input().split():
    unique_num_arr[int(i)] = 1

m = int(input("손님이 요청한 부품 M개를 입력해주세요 > "))
request_num_arr = list(map(int, input().split())) #손님이 요청한 부품 고유번호

for i in request_num_arr:
    if unique_num_arr[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')


##집합 자료형
n = int(input("가게에 있는 부품 N개를 입력해주세요 > "))
unique_num_arr = set(map(int,input().split()))
m = int(input("손님이 요청한 부품 M개를 입력해주세요 > "))
request_num_arr = list(map(int, input().split())) #손님이 요청한 부품 고유번호

for i in request_num_arr:
    if i in unique_num_arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')