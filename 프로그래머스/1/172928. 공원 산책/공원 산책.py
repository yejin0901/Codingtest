def solution(park, routes):
    h = len(park)
    w = len(park[0])
    x,y = 0,0
    
    nav = {
        'S': [0,1],
        'N':[0,-1],
        'W': [-1,0],
        'E':[1,0]
    }
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x = j
                y = i
    
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        flag = 0
        step_x = x
        step_y = y
        for i in range(1,distance+1):
            step_x += nav[direction][0]
            step_y += nav[direction][1]
            
            if step_x >= w or step_x <= -1 or step_y >= h or step_y <= -1 or park[step_y][step_x] == 'X':
                flag = 1
                break
            
        if(flag == 0):
            x += nav[direction][0] * distance
            y += nav[direction][1] * distance
    
    answer = [y,x]
    return answer
