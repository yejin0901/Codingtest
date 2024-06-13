# 단 1개만, 풍선 밀착
# 번호가 작은 풍선은 한번만 그 이후는 번호 큰 풍선만
# 결과 : 어떤 풍선이 최후까지 남기는 개수


def solution(a):
    answer = 0
    result = [False for _ in range(len(a))]
    minFront, minRear = float("inf"), float("inf")
    
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = True
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            result[-1-i] = True
    return sum(result)