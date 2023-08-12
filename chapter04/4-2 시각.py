#예제4-2 시각
#정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지 모든 시각 중에서 
#3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.

n = int(input("숫자 n을 입력하세요 > "))

count = 0
for h in range(n+1): # 0부터 n까지
    for m in range(60): #00분 부터 59분
        for s in range(60): #00초 부터 59초
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)