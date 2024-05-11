# 최소 몇 번
from collections import deque
def bfs(board):
    n = len(board)
    m = len(board[0])
    queue = deque()
    dist = [[float('inf')] * m for _ in range(n)]
    
    dx = [-1, 1, 0, 0] #상, 하
    dy = [0, 0, -1, 1] #좌, 우
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                queue.append((i,j,0))
                dist[i][j] = 0
        if queue:
            break
            
    while queue:
        x,y,c = queue.popleft()
        
        if board[x][y] == 'G':
            return c
        
        for i in range(4):
            n_x = x
            n_y = y
            
            while 0<=n_x+dx[i]<n and 0<=n_y+dy[i]<m and board[n_x+dx[i]][n_y+dy[i]] != 'D':
                n_x += dx[i]
                n_y += dy[i]
            
            if dist[n_x][n_y] > c+1:
                dist[n_x][n_y] = c+1
                queue.append((n_x,n_y,c+1))
                
    return -1
def solution(board):    
    answer = bfs(board)
    return answer