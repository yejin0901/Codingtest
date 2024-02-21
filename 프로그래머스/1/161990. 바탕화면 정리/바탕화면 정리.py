def solution(wallpaper):
    answer = []
    min_y, min_x = len(wallpaper), len(wallpaper[0])
    max_y,max_x=-1,-1
    
    for y_idx, x in enumerate(wallpaper):
        if "#" in x:
            if (y_idx<min_y):
                min_y = y_idx
                
            if(y_idx+1>max_y):
                max_y=y_idx+1
                
            if(x.find("#")<min_x):
                min_x=x.find("#")
                
            if(x.rfind("#")+1 > max_x):
                max_x = x.rfind("#")+1
    return [min_y,min_x,max_y,max_x]