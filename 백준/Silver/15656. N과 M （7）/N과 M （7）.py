n, m = map(int, input().split())
numbers = [int(x) for x in input().split()]

s = []
numbers.sort()


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n):
            s.append(numbers[i])
            dfs(0)
            s.pop()


dfs(0)