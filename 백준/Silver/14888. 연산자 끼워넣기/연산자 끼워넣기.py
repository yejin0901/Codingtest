n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = float('-inf')  # 최댓값 초기화
min_value = float('inf')   # 최솟값 초기화

def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value
    if i == n:  # 기저 조건: 모든 숫자에 대한 연산이 끝난 경우
        max_value = max(max_value, arr)  # 최댓값 갱신
        min_value = min(min_value, arr)  # 최솟값 갱신
        return

    if add > 0:
        add -= 1
        dfs(i + 1, arr + numbers[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i + 1, arr - numbers[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i + 1, arr * numbers[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i + 1, int(arr / numbers[i]))
        div += 1

dfs(1, numbers[0])
print(max_value)
print(min_value)
