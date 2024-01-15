def solution(n):
    n = sorted([x for x in str(n)], key=lambda x:int(x) ,reverse = True)
    return int("".join(n))
    