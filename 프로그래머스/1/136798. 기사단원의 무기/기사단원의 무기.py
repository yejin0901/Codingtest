# 약수 구할 떼, 제곱근으로 나누기 -> 타임아웃을 고려한 문제


def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        
        div_num = 0
        
        for j in range(1, int(i**0.5) +1):
            if i % j == 0:
                div_num += 2
                
        if i ** 0.5 % 1 == 0:
            div_num -= 1
            
        if div_num <= limit :
            answer += div_num
            
            
        else:
            answer+= power
            
    return answer
            
            
        
    return answer