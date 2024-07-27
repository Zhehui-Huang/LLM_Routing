import math

# City coordinates as given in the description
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand list for each city
demand = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15
]

# Given robot tours
robot_tours = [
    [0, 8, 7, 6, 4, 3, 2, 1, 0],
    [0, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 5, 0]
]

# Robot capacity
robot_capacity = 160

def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def validate_solution(tours, demands, capacity):
    visited = set()
    total_demand_met = 0
    overall_travel_cost = 0
    
    for tour in tours:
        current_demand = 0
        last_city = tour[0]
        
        # Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL due to incorrect start/end at depot"
        
        for city in tour[1:-1]: # Exclude the depot city at the ends
            if city in visited:
                return "FAIL due to city visited more than once"
            
            visited.add(city)
            current_demand += demands[city]
            
            # Calculate travel cost
            overall_travel_cost += calculate_distance(last_city, city)
            last_city = city
        
        # Check last distance back to depot
        overall_travel_cost += calculate_distance(last_city, tour[0])
        
        if current_demand > capacity:
            return "FAIL due to exceeding robot capacity"
        
        total_demand_met += current_demand
        
    all_cities = set(range(1, len(demands))) # Cities indices from 1 to 20 (skip depot)
    if visited != all_cities:
        return "FAIL due to not all cities visited"
    
    # Check demands
    if total_demand_met != sum(demands) - demands[0]:
        return "FAIL due to not all demands being met"
    
    return "CORRECT" if overall_travel_cost == 0 else f"FAIL due to incorrect travel cost: {overall_travel_cost}"

# Run the test
test_result = validate_solution(robot_tours, demand, robot_capacity)
print(test_result)