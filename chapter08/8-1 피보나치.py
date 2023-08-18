#예제8-1 피보나치

#함수
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4)) #결과 3

#재귀
d = [0] * 100
def fibo2(x):
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(33)) #결과 3524578