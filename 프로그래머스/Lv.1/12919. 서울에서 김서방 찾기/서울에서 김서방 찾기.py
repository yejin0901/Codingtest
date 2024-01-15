def solution(seoul):
    cnt =-1
    for i in seoul:
        cnt += 1
        if i == 'Kim':
            return "김서방은 "+ str(cnt)+"에 있다"