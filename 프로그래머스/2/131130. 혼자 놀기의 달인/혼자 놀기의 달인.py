def solution(cards):
    answer = []
    visited = [False] *( len(cards)+1)
    for v in cards:
        if not visited[v]:
            tmp = []
            while v not in tmp:
                tmp.append(v)
                visited[v] = True
                v = cards[v-1]
                
            answer.append(len(tmp))
    if answer[0] == len(cards):
        return 0
    else:
        answer.sort(reverse=True)
    return answer[0] * answer[1]