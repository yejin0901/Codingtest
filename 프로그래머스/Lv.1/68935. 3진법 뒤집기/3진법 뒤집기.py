def solution(n):
    res=''
    while n >0:
        res+=str(n%3)
        
        n=n//3
    
    return int(res, 3)  