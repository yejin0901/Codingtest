n = int(input())
m = list(map(int, input().split()))
answer = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == m[i] and answer[j] == 0:
            answer[j] = i+1
            break;
        elif answer[j] == 0:
            cnt+=1
            
print(*answer)