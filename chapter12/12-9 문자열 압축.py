#Q9 문자열 압축

# [문제]
# aabbaccc -> 2a2ba3c
# 문자가 반복되지 않아 한번만 나타난 경우 1은 생략
# 그러나 반복되는 문자가 적은 경우 압축률이 낮다는 단점 발생!!
# 그래서 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현하는 방법을 찾아보려함

# ababcdcdababcdcd 
# 2개 단위 -> 2ab2cd2ab2cd
# 8개 단위 -> 2ababcdcd

# abcabcdede
# 2개 단위 -> abcabc2de
# 3개 단위 -> 2abcdede

# 압축할 문자열 s가 매개변수로 주어질 때, 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수 완성하세요

# [입력]
# s                   result
# aabbaccc            7
# ababcdcdababcdcd    9
# abcabcdedede        8

s = input()

def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1): #0부터 문자열길이//2 만큼이 최대길이
        split_s = '' #잘랐을 때 나오는 문자열 저장
        previous_s = s[0:i] #i만큼의 문자열 추출, 다음 문자열과 연속되는지 확인하기 위한
        count = 1 #문자열 연속 확인

        for j in range(i, len(s), i): #i만큼 증가시키면서 이전 문자열과 비교
            if previous_s == s[j:j+i]: #이전과 동일하면 count증가
                count += 1
            else: #이전과 다르면
                if count != 1:
                    split_s += str(count) + previous_s
                else:
                    split_s += previous_s
                
                previous_s = s[j:j+i] #상태 초기화
                count = 1
        
        #남아 있는 문자열 처리
        if count != 1:
            split_s += str(count) + previous_s
        else:
            split_s += previous_s
        answer = min(answer, len(split_s))
    return answer

print(solution(s))