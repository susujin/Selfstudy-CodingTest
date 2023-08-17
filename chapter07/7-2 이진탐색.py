#이진탐색(Sequential Search)
#탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘
#배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
#탐색범위를 절반씩 좁혀가며 데이터를 탐색하는 특정이 있다.
#이진탐색은 위치를 나타내는 변수 3개를 사용하는데 탐색하고자하는 범위의 시적점, 끝점, 중간점이다.
#찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교

#예제7-2 이진탐색

#0 2 4 6 8 10 12 14 16 18
#예를 들어 위의 리스트에서 4를 찾아보자
#시작점 0, 중간점 8, 끝점 18
#중간점 8과 찾으려는 4를 비교, 중간점보다 큰 구간은 확인할 필요가 없다
#0 2 4 6에서 시작점 0, 중간점 2, 끝점 6
#중간점 2와 찾으려는 4를 비교, 중간점보다 작은 구간은 확인할 필요가 없다.
#4 6에서 시작점이자 중간점 4, 끝점 3
#중간점과 4를 비교하니 동일한 데이터, 여기서 탐색 종료

#재귀함수 활용
def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start+end) // 2 #중간값

    if arr[mid] == target:
        return mid
    elif arr[mid] > target: #중간값이 찾으려는 값보다 크면 왼쪽만 확인
        return binary_search(arr, target, start, mid-1)
    else: #중간값이 찾으려는 값보다 작으면 오른쪽만 확인
        return binary_search(arr, target, mid+1, end)
    
n, target = list(map(int,input("원소의 개수 N과 찾고자하는 값 target을 입력해주세요 > ").split()))
arr = list(map(int,input().split()))

result = binary_search(arr, target, 0, n-1)
if result == None:
    print("원소가 없습니다.")
else:
    print(result+1)

#반복문활용
def binary_search2(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2 #중간값

        if arr[mid] == target:
            return mid
        elif arr[mid] > target: #중간값이 찾으려는 값보다 크면 왼쪽만 확인
            end = mid - 1
        else: #중간값이 찾으려는 값보다 작으면 오른쪽만 확인
            start = mid + 1
    return None

n, target = list(map(int,input("원소의 개수 N과 찾고자하는 값 target을 입력해주세요 > ").split()))
arr = list(map(int,input().split()))

result = binary_search(arr, target, 0, n-1)
if result == None:
    print("원소가 없습니다.")
else:
    print(result+1)


#추가 정보!!
#이진탐색문제는 입력데이터가 많거나, 탐색범위가 매우 넓은 편이다.
#input() 함수를 사용하면 동작속도가 느려서 시간 초과로 오답판정을 받을 수 있다.
#이럴땐 sys 라이브러리의 readline() 함수를 사용하는 것이 좋다!

import sys
input_data = sys.stdin.readline().rstrip()
print(input_data) #입력받은 문자열 그대로 출력