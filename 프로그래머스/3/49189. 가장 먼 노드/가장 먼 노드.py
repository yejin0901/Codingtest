from collections import deque
INF = int(1e9)

def solution(n, edge):
    graph = {i:[] for i in range(1, n+1)}
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    q = deque([])
    distance = [INF] * (n+1)
    distance[1] = 0
    q.append(1)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == INF:
                distance[i] = distance[now] + 1
                q.append(i)
    return distance[1:].count(max(distance[1:]))