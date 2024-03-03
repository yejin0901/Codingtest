#슬라이딩 윈도우
s = input()  # 문자열 입력
a = s.count('a')  # 입력된 문자열에서 a의 개수

s += s[0:a-1]  # 원형 문자열 처리
min_val = float('inf')  # 최소값
for i in range(len(s) - (a-1)):
    min_val = min(min_val, s[i:i+a].count('b'))
print(min_val)
