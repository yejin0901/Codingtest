def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    
    collects = [0,0,0]
    result = []
    
    
    #완전탐색
    for i, answer in enumerate(answers):
        if student1[i%len(student1)] == answer:
            collects[0]+=1
            
        if student2[i%len(student2)] == answer:
            collects[1]+=1
            
        if student3[i%len(student3)] == answer:
            collects[2]+=1
            
    for i, collect in enumerate(collects):
        if max(collects) == collect:
            result.append(i+1)
            
    
    return result