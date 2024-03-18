# 중복 수 찾기
N, K = map(int, input().split())
nums = list(map(int,input().split()))

left = 0
right = 0
answer = 0
counter = [0]*(max(nums)+1)
while right < N:
    if counter[nums[right]] < K:
        counter[nums[right]] += 1
        right += 1
        
    else:
        counter[nums[left]] -= 1
        left+=1
    answer = max(answer, right-left)
print(answer)