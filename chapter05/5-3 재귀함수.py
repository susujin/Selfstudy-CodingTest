# 재귀함수(Recursive Function)
# 자기 자신을 다시 호출하는 함수

#예제5-3 재귀함수

# 다음 코드(5~8)는 오류 발생, 파이썬 인터프리터는 호출 횟수 제한이 있는데 이 한계를 벗어났기 때문이다.
# def recursive_function():
#     print('재귀함수 호출')
#     recursive_function()
# recursive_function()

#재귀함수의 종료조건
def recursive_function(i):
    if i == 10:
        return
    print(i,"번째 재귀함수 실행, ",i+1,"번째 재귀함수 호출")
    recursive_function(i+1)
    print(i,"번째 재귀함수 종료")
recursive_function(1)

#재귀함수활용(팩토리얼)
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복적 구현: ',factorial(5))
print('재귀적 구현: ',factorial_recursive(5))