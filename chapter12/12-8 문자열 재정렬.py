#Q8 문자열 재정렬

# [문제]
# 알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력으로 주어진다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 출력 후 , 그 뒤에 무든 숫자를 더한 값을 이어 출력

# [입력]
# K1KA5CB7 -> ABCKK13
# AJKDLSI412K4JSJ9D -> ADDIJJJKKLSS20

s = input()
s_list = []
number = 0

for i in s:
    if i.isalpha(): #알파벳인지 확인
        s_list.append(i)
    else: #숫자면 더하기
        number += int(i)

s_list.sort() #알파벳정렬

if number != 0:
    s_list.append(str(number))

print(''.join(s_list)) #리스트를 문자열로 변환