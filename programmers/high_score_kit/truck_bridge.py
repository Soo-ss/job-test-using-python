def solution(bridge_length, weight, truck_weights):
    time = 0
    # [0, 0]
    going = [0] * bridge_length
    current_weight = 0

    while truck_weights:
        time += 1
        complete = going.pop(0)
        current_weight -= complete

        if current_weight + truck_weights[0] > weight:
            going.append(0)
        else:
            truck = truck_weights.pop(0)
            going.append(truck)
            current_weight += truck

    while current_weight > 0:
        time += 1
        complete = going.pop(0)
        current_weight -= complete

    return time


print(solution(2, 10, [7, 4, 5, 6]))
