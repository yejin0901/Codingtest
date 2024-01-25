n, m = map(int, input().split())
numbers = [int(x) for x in input().split()]

s = []
numbers.sort()


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n):
        if numbers[i] not in s:
            s.append(numbers[i])
            dfs(i + 1)
            s.pop()


dfs(0)