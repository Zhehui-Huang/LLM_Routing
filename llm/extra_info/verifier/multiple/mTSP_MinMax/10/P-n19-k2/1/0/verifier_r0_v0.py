import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tours, costs, max_travel_cost):
    # Coordinates for cities
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Check if all cities are visited exactly once
    visited_cities = set()
    all_cities = set(range(1, 19))  # City 0 is the depot

    for tour in tours:
        # Requirement 2: Each robot starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Add cities visited in this tour (excluding the depot)
        visited_cities.update(tour[1:-1])
        
    # Requirement 1
    if visited_cities != all_cities:
        return "FAIL"
    
    # Requirement 6: Check the travel cost calculations
    calculated_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            city1_idx = tour[i]
            city2_idx = tour[i + 1]
            x1, y1 = coordinates[city1_idx]
            x2, y2 = coordinates[city2_idx]
            cost += calculate_euclidean_distance(x1, y1, x2, y2)
        calculated_costs.append(cost)
    
    for idx, (cost, provided_cost) in enumerate(zip(calculated_costs, costs)):
        if not math.isclose(cost, provided_cost, abs_tol=0.01):
            return "FAIL"
    
    # Requirement 6: Check maximum cost
    if not math.isclose(max(calculated_costs), max_travel_cost, abs_tol=0.01):
        return "FAIL"
    
    # All checks pass
    return "CORRECT"

# Given solution to validate
robot_tours = [
    [0, 1, 10, 8, 16, 17, 3, 12, 14, 11, 4, 0],
    [0, 6, 2, 7, 9, 15, 13, 5, 18, 0, 0]
]
travel_costs = [116.32876651388246, 80.31749999965545]
max_cost = 116.32876651388246

# Run verification
test_result = verify_solution(robot_tours, travel_costs, max_cost)
print(test_result)