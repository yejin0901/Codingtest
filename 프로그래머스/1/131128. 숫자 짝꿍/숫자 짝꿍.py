def solution(X, Y):    
    xy = set(X) & set(Y)
    if not xy:
        return "-1"
    
    elif len(xy) ==1 and "0"in xy:
        return "0"

    result = [n * min(X.count(n), Y.count(n)) for n in xy]

    return "".join(sorted(result, reverse=True))