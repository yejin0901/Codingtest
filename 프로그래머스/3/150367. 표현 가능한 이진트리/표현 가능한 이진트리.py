# 더미노드 0 -> 십진수 변환
# 루트 노드 0111111 1 2 4 8 16 32 64
# 전위 순회 5 101
def search(number):
    length = len(number)
    if length == 1 or '1' not in number or '0' not in number:
        return True
    mid = length//2
    if number[mid] == '0':
        return False
    
    return search(number[:mid]) and search(number[mid+1:])

def solution(numbers):
    answer = []
    bin_numbers = [bin(x)[2:] for x in numbers ]
    bin_list = [2**x -1 for x in range(50)]
    for number in bin_numbers:
        length = len(number)
        for num in bin_list:
            if num >= length:
                number = '0'*(num-length) + number
                break
        answer.append(1 if search(number) else 0)
    return answer