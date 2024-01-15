def solution(arr, divisor):
    answer = []
    
    result = sorted(list(filter(lambda x:x%divisor==0, arr)))
    
    return result or [-1]