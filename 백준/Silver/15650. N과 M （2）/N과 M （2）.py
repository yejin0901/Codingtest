#문제 1과 동일하지만, 앞뒤 순서도 같은 집합으로 봄

n, m = map(int, input().split())

s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)