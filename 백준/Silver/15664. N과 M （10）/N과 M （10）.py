n, m = map(int, input().split())
numbers = [int(x) for x in input().split()]

s = []

visited = [False] * n



numbers.sort()


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    remember = 0
    for i in range(start,n):
        if not visited[i] and numbers[i] != remember:
            visited[i] = True
            s.append(numbers[i])
            remember = numbers[i]
            dfs(i)
            visited[i] = False
            s.pop()


dfs(0)