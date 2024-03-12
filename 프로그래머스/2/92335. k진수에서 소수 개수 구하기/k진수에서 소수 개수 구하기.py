def solution(n, k):
    answer = 0
    temp = ""
    
    while n>0:
        temp = str(n%k)+temp
        n=n//k
        
    temp = temp.split('0')
    
    for t in temp:
        if len(t)==0:
            continue
        if  int(t)<2:
            continue
        flag = True
        for i in range(2,int(int(t)**0.5)+1):
            if int(t)%i == 0: 
                flag = False
                break
        if flag:
            answer+=1
            
    return answer