def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length  # 다리를 건너는 트럭을 표현하는 큐, 초기에는 무게가 0인 트럭으로 채워짐
    current_weight = 0  # 현재 다리 위의 트럭들의 총 무게
    
    while truck_weights or current_weight:  # 대기 트럭이 있거나 다리 위에 트럭이 있는 동안 반복
        time += 1  # 시간을 1초 증가
        if bridge[0] != 0:  # 다리를 건너고 있는 트럭이 다리를 빠져나감
            current_weight -= bridge.pop(0)  # 다리에서 트럭이 나가면서 무게 감소
        else:
            bridge.pop(0)  # 다리 위에 트럭이 없으면 그냥 0을 제거
        
        if truck_weights and current_weight + truck_weights[0] <= weight:  # 다음 트럭이 다리에 올라올 수 있는 경우
            truck = truck_weights.pop(0)  # 대기열에서 트럭을 꺼냄
            bridge.append(truck)  # 다리에 트럭을 추가
            current_weight += truck  # 다리 위의 총 무게 증가
        else:
            bridge.append(0)  # 다음 트럭이 다리에 올라올 수 없는 경우, 무게가 0인 자리를 추가하여 시간 조정
    
    return time
