from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)  
    trucks = deque(truck_weights)
    current_weight = 0  
    
    while trucks:
        answer += 1
        current_weight -= bridge.popleft() 
        if current_weight + trucks[0] <= weight:  
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:  
            bridge.append(0)
    answer += bridge_length  
    return answer