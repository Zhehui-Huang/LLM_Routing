import math

# Cities data
cities_coordinates = {
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

# Input solution
solution = {
    0: [0, 9, 20, 0],
    1: [0, 8, 3, 2, 5, 7, 6, 18, 17, 21, 16, 13, 11, 0],
    2: [0, 4, 12, 15, 0],
    3: [0, 10, 1, 19, 14, 0]
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verify the solution meets both requirements
def verify_solution(solution):
    visited = set()
    max_travel_cost = 0

    # Check all cities are visited exactly once and calculate distance for each tour
    for robot, tour in solution.items():
        prior_city = tour[0]
        tour_length = 0
        
        for city in tour[1:]:
            if city in visited and city != 0:
                return "FAIL: City visited more than once."
            visited.add(city)
            tour_length += calc_distance(prior_city, city)
            prior_city = city

        if tour[-1] != 0:  # Ensure each tour ends at the depot
            return "FAIL: Tour does not end at the depot."
        
        max_travel_cost = max(tour_length, max_travel_cost)

    # Ensure all cities are visited
    if len(visited) != 21:
        return "FAIL: Not all cities are visited."

    # Calculate maximum travel cost
    if not math.isclose(max_travel_cost, 274.1532670900884, abs_tol=1e-9):
        return f"FAIL: Calculated max travel cost {max_travel_cost} does not match reported cost."

    return "CORRECT"

# Run the verification
result = verify_solution(solution)
print(result)