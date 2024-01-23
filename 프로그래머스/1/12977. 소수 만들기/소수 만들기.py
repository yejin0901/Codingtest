def solution(nums):
    answer = []
    make = []

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                make.append(nums[i]+nums[j]+nums[k])
                
                
    for i in make:
        if all(i%j!=0 for j in range(2,i)):
            answer.append(i)
            
            
    return len(answer)
        
            
