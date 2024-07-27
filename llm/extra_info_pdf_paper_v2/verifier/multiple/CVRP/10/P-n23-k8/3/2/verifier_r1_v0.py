import math

# Coordinates and demands as per the task
cities = {
    0: (30, 40, 0), 1: (37, 52, 7), 2: (49, 49, 30), 3: (52, 64, 16), 4: (31, 62, 23),
    5: (52, 33, 11), 6: (42, 41, 19), 7: (52, 41, 15), 8: (57, 58, 28), 9: (62, 42, 8),
    10: (42, 57, 8), 11: (27, 68, 7), 12: (43, 67, 14), 13: (58, 48, 6), 14: (58, 27, 19),
    15: (37, 69, 11), 16: (38, 46, 12), 17: (61, 33, 26), 18: (62, 63, 17), 19: (63, 69, 6),
    20: (45, 35, 15), 21: (32, 39, 5), 22: (56, 37, 10)
}

# Robots tours and costs generated solution
robots_tours = {
    0: ([0, 21, 7, 9, 0], 64.45),
    1: ([0, 16, 5, 18, 0], 100.14),
    2: ([0, 6, 22, 19, 0], 103.29),
    3: ([0, 1, 12, 15, 0], 66.21),
    4: ([0, 20, 14, 0], 61.95),
    5: ([0, 10, 3, 0], 65.57),
    6: ([0, 2, 13, 0], 59.2),
    7: ([0, 4, 11, 0], 57.39)
}

# Function to calculate the Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Check all requirements
def check_solution(robots_tours):
    total_demand_met = {i: 0 for i in range(1, 23)}
    total_travel_cost_all = 0

    for robot, (tour, total_travel_cost) in robots_tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Robot does not start/end at depot."
        
        trip_cost_calculated = 0
        last_city = tour[0]
        total_capacity_used = 0

        for city in tour[1:]:
            total_capacity_used += cities[city][2]
            if total_capacity_used > 40:
                return "FAIL: Capacity exceeded by robot."
            
            trip_cost_calculated += calculate_distance(cities[last_city], cities[city])
            total_demand_met[city] += cities[city][2]
            last_city = city

        if round(trip_cost_calculated, 2) != round(total_travel_cost, 2):
            return "FAIL: Total travel cost mismatch."

        total_travel_cost_all += total_travel_cost

        trip_cost_calculated += calculate_distance(cities[last_city], cities[0])  # Return to depot

    if any(demand != cities[key][2] for key, demand in total_demand_map.items()):
        return "FAIL: Not all demands are met."
    
    # Requirement to check if the overall cost is minimized is not directly verifiable without alternatives
    print(f"Overall Total Travel Cost Calculated: {total_travel_cost_all}")
    
    return "CORRECT"

# Perform check
result = check_solution(robots_tours)
print(result)