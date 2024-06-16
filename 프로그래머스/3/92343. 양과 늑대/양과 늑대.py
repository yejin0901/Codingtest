# 양을 모음, 방문 시 양과 늑대 따라옴, 늑대는 야를 잡아먹음(같거나 많음)
# 잡히 먹히지 않도록 최대한 많의 양 수
# 루트로 돌아옴 백트래킹
# 양 늑대, [부모, 자식]
def solution(info, edges):
    answer = []
    visited = [0] * len(info)
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = 0
    visited[0] = 1
    dfs(1,0)
    return max(answer) 
               