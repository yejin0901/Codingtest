import heapq
def solution(operations):
    answer = []
    q = []
    for i in operations:
        oper, num = i.split(" ")
        num = int(num)
        if oper == "I":
            heapq.heappush(q, num)
        elif oper == "D" and num == 1:
              if len(q) != 0:
                q.remove(max(q))
        else:
              if len(q) != 0:
                heapq.heappop(q)
    if len(q) == 0:
        answer = [0,0]
    else:
        answer = [max(q), heapq.heappop(q)]
    return answer