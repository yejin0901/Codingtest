n = int(input())

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
result = 0

for i in A:
    temp = max(B)
    result+=i*temp
    B.pop(B.index(temp))



print(result)
