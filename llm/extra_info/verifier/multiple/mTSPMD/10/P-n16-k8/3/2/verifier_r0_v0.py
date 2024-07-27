import math

# Provided tours and costs
robots_info = {
    0: {"tour": [0, 0], "cost": 0.00},
    1: {"tour": [1, 10, 1], "cost": 14.14},
    2: {"tour": [2, 13, 2], "cost": 18.11},
    3: {"tour": [3, 8, 12, 3], "cost": 33.94},
    4: {"tour": [4, 11, 15, 4], "cost": 26.48},
    5: {"tour": [5, 14, 5], "cost": 16.97},
    6: {"tour": [6, 6], "cost": 0.00},
    7: {"tour": [7, 9, 7], "cost": 20.10},
}

overall_cost_claimed = 129.74

# City and coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_solution(robots_info, city_coordinates, overall_cost_claimed):
    all_cities_visited = set(range(16))
    cities_visited = set()
    total_calculated_cost = 0.0
    
    for robot, info in robots_info.items():
        route = info["tour"]
        claimed_cost = info["cost"]
        calculated_cost = 0.0
        
        # Check the tour starts and ends at the robot's depot
        start_end_city = robot
        if route[0] != start_end_city or route[-1] != start_end_city:
            return "FAIL"
        
        # Check each city is visited once and calculate cost
        for i in range(len(route) - 1):
            city1, city2 = route[i], route[i + 1]
            edge_cost = euclidean_distance(city_coordinates[city1], city_coordinates[city2])
            calculated_cost += edge_cost
            if city1 != start_end_city:  # Avoid counting depots twice
                cities_visited.add(city1)
        
        # Final city handling
        if route[-1] != start_end_city:
            cities_visited.add(route[-1])
        
        # Cost validation
        if not math.isclose(calculated_cost, claimed_cost, abs_tol=0.01):
            return "FAIL"
        
        total_calculated_cost += calculated_cost
    
    # Check all cities are visited once and cost aggregation
    if cities_visited != all_cities_visited:
        return "FAIL"
    if not math.isclose(total_calculated_cost, overall_cost_claimed, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Run the verification
verification_result = check_solution(robots_info, city_coordinates, overall_cost_claimed)
print(verification_result)