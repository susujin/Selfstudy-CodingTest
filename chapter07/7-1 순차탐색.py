#순차탐색(Sequential Search)
#리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
#보통 정렬되지 않은 리스트에서 데이터를 찾아야할 떄 사용
#리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 원소를 찾을 수 있다는 장점이 있다.

#예제7-1 순차탐색
def sequential_search(n, target, array):
    #n은 원소 개수, target은 찾고자하는 값, array는 배열
    for i in range(n):
        if array[i] == target:
            return i+1 #인덱스는 0부터, 즉 +1해줘야 현재 위치
    
print("원소의 개수 n과 찾고자하는 문자열을 입력해주세요 > ")
data = input().split()
n = int(data[0])
target = data[1]

array = input("{0}개의 문자열을 작성하세요 > ".format(n)).split()

print(sequential_search(n, target, array))