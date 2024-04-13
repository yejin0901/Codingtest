#순서대로 증가
#배달하는 순서와 택배상자가 실리는 순서가 안맞음
#다른 곳에 보관 -> lifo만 가능, 순서가 안맞으면 pass 4 3 1 2 5 12345
def solution(order):
    stack = []
    answer = 0
    i = 1
    cnt = 0
    
    while i != len(order)+1:
        stack.append(i)
        while stack and stack[-1] == order[cnt]:
            cnt+=1
            stack.pop()
        i+=1
    return cnt