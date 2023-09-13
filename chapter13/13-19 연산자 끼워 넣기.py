#Q19 연산자 끼워넣기 (책참고)

# [문제]
# N개의 수로 이루어진 수열이 주어짐. 수와 수 사이에 끼워 넣을 수 있는 N-1개의 연산자가 주어짐.
# 연산자는 덧셈, 뺼셈, 곱셈, 나눗셈으로만 이루어져있다.

# 수와 수 사이에 연산자를 하나씩 넣어 하나의 수식을 만들수 있는데 주어진 수의 순서를 바꾸면 안됨.

# 예를들어 6개로 이루어진 수열이 1,2,3,4,5,6이고 주어진 연산자가 덧셈 2개, 뺄셈 1개, 곱셈 1개, 나눗셈 1개인경우 총 60가지의 식을 만들 수 있다.

# 식의 계산은 연산자 우선순위를 무시하고 앞에서부터 진행. 
# 나눗셈은 정수 나눗셈 몫만 취함.
# 음수를 양수로 나눌 때는 C++14 기준을 따라, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼것과 같음.

# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들수 잇는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하세요.

# [입력]
n = int(input()) #수의 개수
seq = list(map(int, input().split())) #수열
add,sub,mul,div = map(int, input().split()) #연산자 개수

min_val = 1e9
max_val = -1e9

def cal(index, result):
    global add,sub,mul,div, min_val,max_val

    if index == n: #연산자 전부 사용
        min_val = min(min_val, result)
        max_val = max(max_val, result)
    else: #연산자가 남아있다면
        if add > 0:
            add -= 1
            cal(index+1, result+seq[index])
            add += 1 #??빼고 왜 더함??

        if sub > 0:
            sub -= 1
            cal(index+1, result-seq[index])
            sub += 1 #??빼고 왜 더함??

        if mul > 0:
            mul -= 1
            cal(index+1, result*seq[index])
            mul += 1 #??빼고 왜 더함??

        if div > 0:
            div -= 1
            cal(index+1, int(result/seq[index]))
            div += 1 #??빼고 왜 더함??

cal(1,seq[0])
print(max_val)
print(min_val)