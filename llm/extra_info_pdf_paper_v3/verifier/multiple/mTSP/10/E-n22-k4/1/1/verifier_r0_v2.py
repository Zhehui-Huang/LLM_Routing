import math

# Define the data for cities and their coordinates.
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

# Tours taken by each robot
tours = [
    [0, 14, 16, 12, 13, 10, 0],
    [0, 15, 17, 11, 8, 9, 0],
    [0, 18, 19, 6, 7, 20, 0],
    [0, 21, 5, 4, 3, 2, 1, 0]
]

# Expected travel costs for each tour
expected_costs = [101.65864442938738, 150.40166870539406, 228.23967386853874, 228.75688636631048]
expected_overall_cost = 709.0568733696307

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tours, cities, expected_costs, expected_overall_cost):
    total_computed_cost = 0
    unique_cities = set(range(len(cities)))

    for index, tour in enumerate(tours):
        # Validate starting and ending at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        total_computed_cost += tour_cost
        
        if not math.isclose(tour_cost, expected_costs[index], rel_tol=1e-9):
            return "FAIL"
        
        unique_cities -= set(tour[1:-1])

    if unique_cities != {0}:
        return "FAIL"

    if not math.isclose(total_computed_cost, expected_overall_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Run the verification function and print the result
result = verify_solution(tours, cities, expected_costs, expected_overall_cost)
print(result)