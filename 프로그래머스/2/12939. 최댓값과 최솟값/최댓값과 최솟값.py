def solution(s):
    num = list(map(int,s.split(" ")))
    result = f'{min(num)} {max(num)}'
    return result