def convert_to_number(time): #문자열
    if ':' not in time:
        return int(time)
    
    a,b = time.split(':')
    
    return int(a) * 60 + int(b)

def solution(plans):
    p = []
    answer = []
    
    for title,start,time in plans:
        p.append((title, convert_to_number(start), convert_to_number(time)))
    
    p.sort(key=lambda x:x[1])
    
    stack = []
    stack.append(p[0])
    
    time = p[0][1]
    
    for i in range(1,len(plans)):
        next_time = p[i][1]
        
        while stack:
            job, time_start, time_spend = stack.pop()
            
            if time < time_start:
                time = time_start
            time_finish = time + time_spend
            
            if next_time < time_finish:
                stack.append([job, time_start, time_finish - next_time])
                time = next_time
                break
            else:
                answer.append(job)
                time += time_spend
                
        stack.append(p[i])
    while len(stack):
        answer.append(stack.pop()[0])
    return answer 