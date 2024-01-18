

def solution(sizes):

    max_w = max_h = 0

    for size in sizes:
        width, height = size

        max_w = max(max_w, width, height)
        max_h = max(max_h, min(width, height))


    return max_w * max_h
