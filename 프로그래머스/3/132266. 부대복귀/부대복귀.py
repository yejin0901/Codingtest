# 최단시간 복귀, 경로가 없어질 수 있음
# 지역수, 왕복 길, 부대원 위치, 강철부대 지역
# 최단시간 배열 return 
# 무방향 bfs
from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    costs = [-1 for _ in range(n+1)]
    costs[destination] = 0
    queue = deque([destination])
    
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)
    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if costs[node] == -1:
                queue.append(node)
                costs[node] = costs[x] + 1
    for s in sources:
        answer.append(costs[s])
    return answer