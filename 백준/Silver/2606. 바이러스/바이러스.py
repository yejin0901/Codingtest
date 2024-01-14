from collections import deque
#bfs 너비우선탐색

n = int(input())
v = int(input())

graph = [[]for _ in range(n+1)]

visited=[0]*(n+1)
for i in range(v):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited[1]=1
q=deque([1])

while q:
    c = q.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            q.append(nx)
            visited[nx]=1
print(sum(visited)-1)