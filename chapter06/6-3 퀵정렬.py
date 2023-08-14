#퀵정렬(Quick Sort)
#정렬 알고리즘 중에 가장 많이 사용되는 알고리즘
#퀵정렬과 비교할 만큼 빠른 알고리즘으로는 '병합정렬'이 있다.
#두 알고리즘은 대부분의 프로그래밍 언어에서 정렬 라이브러리의 근간이 되는 알고리즘이기도 하다.
#퀵정렬은 기준을 설정한 다음 큰수와 작은수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.
#피벗(Pivot)이 사용된다. 큰수와 작은수를 교환할 때, 교환하기 위한 '기준'을 바로 피벗이라고 표현

#예제6-3 퀵정렬
#추가 설명!
#리스트의 첫번째 데이터를 피벗으로 설정한다. '5'
#왼쪽부터 '5'보다 큰 데이터를 선택하므로 '7'선택, 오른쪽에서부터 '5'보다 작은 데이터를 선택하므로 '4'선택
#'7'과 '4'의 위치를 바꾼다.
#다음으로 왼쪽부터 '5'보다 큰 '9'와 오른쪽부터 '5'보다 작은 '2'를 선택하여 위치를 바꾼다.
#5,4,2,0,3,1,6,9,7,8
#이런 방식으로 분할이 끝나면 1,4,2,0,3, 5 ,6,9,7,8
#'5'보다 작은 것은 왼쪽에, 큰것은 오른쪽에 정렬된다. 이런 것을 분할 혹은 파티션이라고 한다.
#!!이상태에서 왼쪽 리스트, 오른쪽 리스트에서도 각각 피벗을 설정하여 동일한 방식으로 정렬을 수행한다.
#이런 식으로 정렬하는 것이 퀵정렬이다.

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: #원소가 하나인 경우
        return
    pivot = start #피벗은 첫번째 원소(인덱스0)
    left = start + 1
    right = end
    while left <= right:
        #피벗보다 큰 값을 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left +=1
        #피벗보다 작은 값을 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        #교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        
    #분할 후 왼족 오른쪽 각각 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)
print(array)

#다른 방법
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort_2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)
print(quick_sort_2(array))