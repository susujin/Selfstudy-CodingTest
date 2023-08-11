#예제3-3 숫자 카드 게임
#min 함수 사용
#행의 개수 N, 열의 개수 M
#뽑고자 하는 카드가 포함되어 있는 행을 선택, 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑는다.
#처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세운다.
n, m = map(int, input("행과 열을 입력해주세요 > ").split()) # 각 변수를 공백으로 구분하여 입력받는다.

min_number = 0
result = []

for i in range(n): #n번 실행하여 한 줄씩 리스트 만들기
    number_list = list(map(int, input("숫자 리스트를 입력해주세요 > ").split()))
    min_number = min(number_list)
    result.append(min_number)

print(max(result))

#2중 반복문 구조 사용
n, m = map(int, input("행과 열을 입력해주세요 > ").split())

result = 0
for i in range(n):
    data = list(map(int, input("숫자 리스트를 입력해주세요 > ").split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value,a)
        result = max(result, min_value)

print(result)