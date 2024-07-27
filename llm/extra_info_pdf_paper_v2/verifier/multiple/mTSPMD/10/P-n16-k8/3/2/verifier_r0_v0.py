import math

# Define the coordinates of the cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Robots' tours and reported costs
robot_tours = {
    0: ([0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0], 173.01),
    1: ([1, 10, 12, 15, 4, 11, 3, 8, 13, 9, 7, 5, 14, 6, 2, 0, 1], 183.61),
    2: ([2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 10, 1, 6, 0, 2], 168.69),
    3: ([3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 4, 11, 15, 12, 0, 3], 198.97),
    4: ([4, 11, 15, 12, 3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 0, 4], 170.19),
    5: ([5, 14, 9, 13, 2, 7, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 5], 183.25),
    6: ([6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0, 6], 173.01),
    7: ([7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 6, 0, 7], 175.26),
}

def calculate_distance(p1, p2):
    """ Helper function to calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tours, cities):
    all_visited = set()
    calculated_costs = []
    for robot_id, (tour, reported_cost) in tours.items():
        # Check if starts and ends at its depot
        if tour[0] != tour[-1] or tour[0] != robot_id:
            return "FAIL"
        
        # Calculate the travel cost
        travel_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        calculated_costs.append(travel_cost)
        
        # Check visitation of cities
        visited_cities = set(tour[1:-1])  # exclude the start/end depot which will be counted twice otherwise
        if any(city in all_visited for city in visited_cities):
            return "FAIL"
        all_visited.update(visited_cities)
    
    if len(all_visited) != 16:
        return "FAIL"
    
    # Check cost calculations
    actual_total_cost = sum(calculated_costs)
    expected_total_cost = sum(cost for _, cost in tours.values())
    
    if not math.isclose(actual_total_cost, expected_total_cost, abs_tol=0.1):
        return "FAIL"
    
    # Total cost in report
    reported_total_cost = 1425.99
    if not math.isclose(actual_total_cost, reported_total_cost, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

# Check if the solution is correct
result = verify_solution(robot_tours, cities)
print(result)