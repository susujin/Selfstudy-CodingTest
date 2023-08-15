#파이썬은 기본 정렬 라이브러리인 sorted() 함수를 제공한다.
#방법1
array1 = [7,5,9,0,3,1,6,2,4,8]
result = sorted(array1)
print(result)

#리스트 객체의 내장 함수인 sort를 이용할 수 있다.
#방법2
array2 = [7,5,9,0,3,1,6,2,4,8]
array2.sort()
print(array2)

#키를 활용한 방법
array3 = [('바나나',2),('사과',5),('당근',3)]
def setting(data):
    return data[1]
result = sorted(array3, key=setting)
print(result)