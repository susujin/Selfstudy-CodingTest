#예제5-1 스택
#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
#5,2,3,7 순으로 들어가고 마지막으로 들어간 7삭제, 이어서 1,4순으로 들어가고 마지막으로 들어간 4삭제
#결론적으로 (아래) 5,2,3,1 (위)

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() #삭제, 즉, 7 제거
stack.append(1)
stack.append(4)
stack.pop() #삭제, 즉, 4 제거

print(stack) #먼저 들어간 것 부터 즉, 아래부터 출력
print(stack[::-1]) #마지막에 들어간 것부터 즉, 위부터 출력