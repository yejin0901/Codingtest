n, m = map(int, input().split())
numbers = [int(x) for x in input().split()]

s = []

numbers.sort()


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    remember = 0
    for i in range(start, n):
        if numbers[i] != remember:
            s.append(numbers[i])
            remember = numbers[i]
            dfs(i)
            s.pop()


dfs(0)