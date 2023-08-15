#예제6-7 성적이 낮은 순서대로 학생 출력
#학생 수 N, 두번째 부터는 학생이름과 성적을 입력

n = int(input('학생 수를 입력해주세요. > '))

arr = []
for i in range(n):
    student_data = input().split()
    arr.append((student_data[0], int(student_data[1])))

#여기 조금 어렵다..
arr = sorted(arr, key=lambda student:student[1]) 

for i in arr: 
    print(i[0], end=' ')

#lambda 
#lambda 매개변수:표현식

#두수를 더하는 함수는 아래와 같다.
# def plus(x,y):
#     return x+y
# plus(10,20)

#위의 함수를 람다로 표현하면 아래와 같다.
# (lambda x,y:x+y)(10,20)