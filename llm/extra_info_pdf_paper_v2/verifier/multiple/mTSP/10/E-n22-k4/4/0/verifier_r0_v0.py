import math

# Define city coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

# Robot tours and their provided costs
robot_tours = {
    0: ([0, 4, 1, 5, 8, 13, 17, 0], 187.87),
    1: ([0, 10, 3, 19, 21, 16, 0], 156.83),
    2: ([0, 12, 2, 7, 9, 20, 0], 163.96),
    3: ([0, 6, 11, 14, 18, 15, 0], 142.33)
}

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(robot_tours):
    visited_cities = set()
    total_calculated_cost = 0.0

    for robot, (tour, provided_cost) in robot_tours.items():
        # Requirement 1: Starts and ends at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate tour cost
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

        # Check with provided cost
        if not math.isclose(tour_cost, provided_cost, rel_tol=1e-2):
            return "FAIL"

        # Collect visited cities (excluding depot)
        visited_cities.update(tour[1:-1])
        total_calculated_cost += tour_cost

    # Requirement 2: All cities visited exactly once
    if visited_cities != set(cities.keys()) - {0}:
        return "FAIL"

    # Check calculated total cost with stated total cost
    stated_total_cost = sum(cost for _, cost in robot_tours.values())
    if not math.isclose(total_calculated_cost, stated_total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Run the tests
result = test_solution(robot_tours)
print(result)