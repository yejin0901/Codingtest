def solution(n, info):
    global max_gap, answer
    
    answer = [-1]
    score = [0]*11
    max_gap=0
    
    def is_winner_with_gap(score):
        a=0 # 어피치 점수
        b=0 # 라이언 점수
        
        for i in range(len(info)):
            if info[i] > 0 or score[i] > 0:
                if info[i]>=score[i]:
                    a += (10-i)
                else:
                    b += (10-i)
        return (b > a, abs(a-b))

    def dfs(L, cnt):
        global max_gap, answer
        if L == 11 or cnt == 0:    
            is_winner, gap = is_winner_with_gap(score)
            if is_winner:
                if cnt >= 0: # 화살이 남은 경우
                    score[10] = cnt # 0점에 쏴도 이김
                
                if gap > max_gap: # 갭이 더 큰 경우로 업데이트
                    max_gap = gap
                    answer = score.copy()
                    
                elif gap == max_gap: # 가장 낮은 점수를 많이 맞힌 경우로 업데이트
                    for i in range(len(score)):
                        if answer[i] > 0:
                            max_i_1 = i
                        if score[i] > 0:
                            max_i_2 = i
                    if max_i_2 > max_i_1:
                        answer = score.copy()
                    
            return
        
        # k점을 어피치보다 많이 맞추거나 아예 안맞추거나
        if cnt>info[L]:
            score[L]=info[L]+1
            dfs(L+1, cnt-(info[L]+1))
            score[L]=0
            
        dfs(L+1, cnt)
    
    dfs(0,n)
    
    return answer