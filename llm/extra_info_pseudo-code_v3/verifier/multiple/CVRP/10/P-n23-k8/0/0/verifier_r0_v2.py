import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tours, total_costs, demands, capacities, coords):
    robot_count = 8
    city_count = len(coords)
    
    if len(tours) != robot_count:
        return "FAIL: The number of tours does not match the number of robots."
    
    used_capacity = [0] * robot_count
    served_demand = [0] * (city_count - 1)
    
    calculated_total_costs = []
    
    for i, tour in enumerate(tours):
        last_city = 0
        tour_cost = 0
        
        for city in tour:
            if city != 0 and used_capacity[i] + demands[city] > capacities[i]:
                return "FAIL: Capacity exceeded for Robot " + str(i)
            if city != 0:
                used_capacity[i] += demands[city]
                served_demand[city - 1] += demands[city]
            
            # Calculate travel cost
            tour_cost += calculate_distance(coords[last_city], coords[city])
            last_city = city
        
        if last_city != 0:
            tour_cost += calculate_distance(coords[last_city], coords[0])
        
        calculated_total_costs.append(round(tour_cost, 2))
        
        if abs(tour_cost - total_costs[i]) > 0.1:
            return f"FAIL: Incorrect total travel cost reported for Robot {i}. Expected around {tour_cost}, reported {total_costs[i]}"
        
    if any(demand != served for demand, served in zip(demands[1:], served_demand)):
        return "FAIL: Not all demands are properly met."
    
    overall_calculated_cost = sum(calculated_total_costs)
    reported_overall_cost = sum(total_costs)
    
    if abs(overall_calculated_cost - reported_overall_cost) > 0.1:
        return f"FAIL: Overall cost mismatch. Calculated: {overall_calculated_cost}, Reported: {reported_overall_cost}"
    
    return "CORRECT"

# Coordinates and demands from task description
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
capacities = [40] * 8  # Each robot's capacity

tours = [
    [0, 21, 16, 1, 10, 13, 0],
    [0, 6, 20, 19, 0],
    [0, 2, 22, 0],
    [0, 4, 11, 9, 0],
    [0, 7, 5, 12, 0],
    [0, 15, 3, 0],
    [0, 14, 18, 0],
    [0, 17, 0]
]

total_costs = [72.09, 101.15, 61.09, 104.9, 95.16, 78.2, 106.5, 63.56]

# Execute the verification
result = verify_solution(tours, total_costs, demands, capacities, coords)
print(result)