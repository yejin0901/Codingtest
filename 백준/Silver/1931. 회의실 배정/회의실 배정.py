num = int(input())

time = sorted([tuple(map(int,input().split())) for _ in range(num)], key=lambda x:(x[1], x[0]))
answer = 0

end = 0

for s,e in time:
    if s >= end:
        answer += 1
        end = e
print(answer)