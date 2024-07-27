import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution():
    cities = {
        0: (145, 215),
        1: (151, 264),
        2: (159, 261),
        3: (130, 254),
        4: (128, 252),
        5: (163, 247),
        6: (146, 246),
        7: (161, 242),
        8: (142, 239),
        9: (163, 236),
        10: (148, 232),
        11: (128, 231),
        12: (156, 217),
        13: (129, 214),
        14: (146, 208),
        15: (164, 208),
        16: (141, 206),
        17: (147, 193),
        18: (164, 193),
        19: (129, 189),
        20: (155, 185),
        21: (139, 182)
    }
    
    tours = [
        [0, 10, 8, 6, 3, 4, 11, 0],
        [0, 18, 20, 17, 21, 19, 0],
        [0, 1, 2, 5, 7, 9, 0],
        [0, 12, 15, 14, 16, 13, 0]
    ]

    robot_costs = [99.60668471182551, 108.76088795469096, 111.83855721201843, 77.0605239171631]
    
    overall_cost = 397.266653795698
    calculated_overall_cost = 0
    visited_cities = set([0])  # Include depot initially

    for i, tour in enumerate(tours):
        tour_cost = 0
        for j in range(len(tour) - 1):
            city_from = tour[j]
            city_to = tour[j + 1]
            tour_cost += calculate_euclidean_distance(*cities[city_from], *cities[city_to])
            visited_cities.add(city_to)
        
        # Verify each robot’s total travel cost
        if not math.isclose(tour_cost, robot_costs[i], rel_tol=1e-5):
            return "FAIL"
        
        calculated_overall_cost += tour_cost
    
    # Verify overall cost
    if not math.isclose(calculated_overall_cost, overall_cost, rel_tol=1e-5):
        return "FAIL"

    # Verify that all cities except the depot are visited exactly once
    if len(visited_cities) != 22 or any(tour.count(city) > 1 for tour in tours for city in tour if city != 0):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Run the verification
result = verify_solution()
print(result)