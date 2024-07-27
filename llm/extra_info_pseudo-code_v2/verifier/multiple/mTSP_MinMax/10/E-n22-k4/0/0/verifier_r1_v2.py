import math

# Define robot tours
robot_tours = {
    0: [0, 21, 14, 12, 15, 7, 4, 0],
    1: [0, 10, 6, 3, 1, 9, 18, 20, 19, 13, 16, 0],
    2: [0, 8, 17, 2, 0],
    3: [0, 11, 5, 0]
}

# Define the coordinates of the cities
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

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution():
    all_visited = set()
    max_computed_cost = 0

    for robot, tour in robot_tours.items():
        # Requirement 2: Start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Requirement 3 & 6
        for city in tour[1:-1]:
            if city in all_visited:
                return "FAIL"
            all_visited.add(city)

        # Calculate tour cost and update maximum computed cost
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
        max_computed_cost = max(max_computed_cost, tour_cost)

    # Requirement 4: Verify if the actual max tour cost matches provided
    if not math.isclose(max_computed_cost, 233.6460317616323, rel_tol=1e-6):
        return "FAIL"

    # Requirement 1: All cities except depot must be visited exactly once
    if len(all_visited) != 21:
        return "FAIL"

    # All checks are satisfied
    return "CORRECT"

# Run validation and print the result
result = validate_solution()
print(result)