def convert_to_number(time): #문자열
    if ':' not in time:
        return int(time)
    
    a,b = time.split(':')
    
    return int(a) * 60 + int(b)

def solution(plans):
    p = []
    
    for title,start,time in plans:
        p.append((title, convert_to_number(start), convert_to_number(time)))
    
    p.sort(key=lambda x:x[1])
    ans = []
    stack = []
    for i in range(len(p)): # 시간안에 과제를 못 끝낼경우, 끝낼경우
        if i == len(p)-1: # 마지막 과제에 도달했을 경우
            ans.append(p[i][0])
            for i in range(-1, -len(stack)-1, -1):
                ans.append(stack[i][0])
            break
        extra = p[i+1][1] - (p[i][1]+p[i][2]) # 다음과제시간 - (현재 과제시간 + 과제 진행시간)
        
        if extra >= 0: # 시간 안에 끝낼수 있는경우 추가과제 할수 있으면 한다
            ans.append(p[i][0])
            while stack:
                if stack[-1][1] <= extra: # 여분의 시간이 스택에 남은 시간보다 클 경우
                    k = stack.pop()
                    ans.append(k[0]) # 과제이름
                    extra -= k[1]
                
                else:
                    stack[-1][1] -= extra
                    break
        else: # 다음 과제시간까지 못 끝낸경우
            stack.append([p[i][0], -extra])
    
    return ans