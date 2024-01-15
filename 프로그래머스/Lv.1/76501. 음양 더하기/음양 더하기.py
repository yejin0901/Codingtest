def solution(absolutes, signs):
    return sum(x if sign else -x for x, sign in zip(absolutes, signs))