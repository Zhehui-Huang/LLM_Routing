import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i-1]]
        x2, y2 = coordinates[tour[i]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return round(total_cost, 2)

def verify_solution():
    cities = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
        4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
        8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
        16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }
    
    # Provided solution details
    robots_tours = {
        0: [0, 16, 19, 21, 17, 20, 18, 12, 0],
        1: [1],
        2: [2, 5, 7, 9, 15, 10, 11, 6, 2],
        3: [3, 8, 14, 13, 4, 3]
    }
    reported_costs = {
        0: 116.30,
        1: 0.00,
        2: 146.44,
        3: 109.34
    }
    overall_total_reported = 372.07

    # Verify all cities are visited exactly once
    visited_cities = set()
    for tour in robots_tours.values():
        visited_cities.update(tour)
    
    # There are 22 cities, considering all should be visited
    if len(visited_cities) != 22:
        return "FAIL"
    
    # Calculate actual costs
    actual_costs = {}
    for robot, tour in robots_tours.items():
        actual_costs[robot] = calculate_tour_cost(tour, cities)
    
    # Compare reported costs with calculated costs
    for robot, cost in reported_costs.items():
        if not math.isclose(cost, actual_costs[robot], abs_tol=0.01):
            print(f"Mismatch in reported cost for robot {robot}: expected {actual_costs[robot]}, got {cost}")
            return "FAIL"
    
    # Check overall total cost
    actual_overall_total = sum(actual_costs.values())
    if not math.isclose(actual_overall_total, overall_total_reported, abs_tol=0.01):
        print(f"Overall costs do not match: expected {actual_overall_total}, got {overall_total_reported}")
        return "FAIL"
    
    return "CORRECT"

# Run tests
output = verify_solution()
print(output)