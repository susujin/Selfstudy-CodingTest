# 큐(Queue)
# - 대기 줄에 비유할 수 있음
# - 먼저 줄 선 사람이 먼저 들어간다. 늦게 온 사람은 늦게 들어간다.
# - 선입선출(First In First Out) 구조

#예제5-2 큐
#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
#5,2,3,7 순으로 들어가고 먼저 들어간 5삭제, 이어서 1,4순으로 들어가고 이어 맨 앞에 있는 2삭제
#결론적으로 (아래) 3,7,1,4 (위)

#큐 구현을 위한 deque 라이브러리 사용
from collections import deque 

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #삭제, 즉, 5 제거
queue.append(1)
queue.append(4)
queue.popleft() #삭제, 즉, 2 제거

print(queue) #먼저 온 순으로 출력
queue.reverse()
print(queue) #나중에 온 순으로 출력