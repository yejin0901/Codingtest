def solution(sequence, k):
    start = 0
    current_sum = 0
    min_length = float('inf')
    result = [-1, -1]

    for end in range(len(sequence)):
        current_sum += sequence[end]
        
        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1
        
        # 합이 k와 일치하면 길이와 시작 인덱스를 확인
        if current_sum == k:
            current_length = end - start + 1
            if current_length < min_length:
                min_length = current_length
                result = [start, end]

    return result