#bfs 2번 시작 -> 레버, 레버-> 출구
from collections import deque
def bfs(start, end, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False] *m for _ in range(n)]
    queue = deque()
    flag = False
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                queue.append((i, j, 0))
                visited[i][j] = True
                flag = True;
                break
        if flag: break
        
    while queue:
        x, y, cost = queue.popleft()
        if maps[x][y] == end:
            return cost
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0<= ny <m and 0<= nx < n and maps[nx][ny] != 'X':
                if not visited[nx][ny]:
                    queue.append((nx, ny, cost+1))
                    visited[nx][ny] = True
    return -1
    
def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)
    
    if path1 != -1 and path2 != -1:
        return path1+path2
    return -1