def solution(k, score):
    answer = []
    award =[]
    
    for i in score:
        award.append(i)
        award.sort(reverse=True)
        
        if len(award) > k:
            award.pop()
            
        answer.append(award[-1])
        
    return answer