def solution(left, right):
    decide_sign = lambda x: -1 if (x ** 0.5).is_integer()  else 1
    return sum([i * decide_sign(i) for i in range(left, right + 1)])
