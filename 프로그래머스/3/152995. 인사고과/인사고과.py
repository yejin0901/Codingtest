# 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번
# 두 점수의 합이 높은 순으로 석차(동석차 건너뜀)
# 근무 태도 점수, 동료 평가 점수
# 원호의 석차
def solution(scores):
    answer = 1
    wanho = scores[0]
    sum_wanho = wanho[0] + wanho[1]
    scores.sort(key = lambda x:(-x[0], x[1]))
    flag = 0
    
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        if flag <= score[1]:
            if sum_wanho < score[0] + score[1]:
                answer+=1
            flag = score[1]
    return answer