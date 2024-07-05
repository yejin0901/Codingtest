#실내온도와 희망온도가 다르다면 1분 뒤 실내온도가 희망온도와 같아지는 방향으로 1도 상승 또는 하강합니다 a
# 에어컨의 전원을 끄면 실내온도가 실외온도와 같아지는 방향으로 매 분 1도 상승 또는 하강합니다. b
#  에어컨의 소비전력을 최소화
# 탑승중 
def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    k = 1000*100
    t1+= 10
    t2 += 10
    temperature += 10
    
    DP=[[k] * 51 for _ in range(len(onboard))]
    DP[0][temperature] = 0
    
    flag = 1
    if temperature > t2:
        flag = -1
        
    for i in range(1, len(onboard)):
        for j in range(51):
            arr = [k]
            if (onboard[i] == 1 and t1<=j<=t2) or onboard[i] == 0:
                if 0 <= j+flag <=50:
                    arr.append(DP[i-1][j+flag])
                    
                if j == temperature:
                    arr.append(DP[i-1][j])
            
                if 0 <= j-flag <= 50:
                    arr.append(DP[i-1][j-flag]+a)
                
                if t1 <= j <= t2:
                    arr.append(DP[i-1][j] + b)
                
                DP[i][j] = min(arr)
    answer = min(DP[len(onboard)-1])
    return answer 