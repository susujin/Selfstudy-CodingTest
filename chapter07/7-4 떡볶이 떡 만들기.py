#예제7-4 떡볶이 떡 만들기
#절단기에 높이(H)를 지정하면 줄지어진 떡을 한번에 절단한다.
#높이가 H보다 긴 떡은 H 위의 부분이 잘릴것이고 낮은 떡은 잘리지 않는다.

#예를들어 높이가 19,14,10,17cm인 떡이 나란히 있고 절단기 높이를 15cm으로 지정하면 
#자른뒤의 떡의 높이는 15,14,10,15cm이 될 것이다.
#잘린 떡의 길이는 4,0,0,2cm이다.
#손님은 6cm만큼의 길이를 가져간다.

n,m = map(int,input("떡의 개수 N과 떡의 길이 M을 입력해주세요 > ").split())
height_arr = list(map(int,input().split())) #떡 높이

start = 0
end = max(height_arr)

result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2

    for i in height_arr:
        if i > mid:
            total += i - mid
    
    #떡이 부족한 경우 더 자르기(왼쪽)
    if total < m:
        end = mid - 1
    #떡이 충분한 경우 덜 자르기(오른쪽)
    else:
        result = mid
        start = mid + 1

print(result)

#어렵다...