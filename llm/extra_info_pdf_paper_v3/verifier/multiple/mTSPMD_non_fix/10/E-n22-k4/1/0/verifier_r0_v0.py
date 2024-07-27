import math

# Define the coordinates for each city
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

# Given tours and costs
tours = {
    0: ([20, 18, 12, 10, 7, 9, 20], 128.68922864389404),
    1: ([9, 15, 17, 21, 19, 11, 9], 153.8646878087496),
    2: ([11, 8, 6, 4, 3, 1, 11], 109.47264375211566),
    3: ([1, 2, 5, 0, 14, 16, 1], 131.13133152249884)
}

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def validate_tours_and_costs(tours):
    all_visited_cities = set()
    total_calculated_cost = 0

    for robot_id, (tour, reported_cost) in tours.items():
        # Check the tour starts from the starting depot
        if tour[0] != tour[-1] or tour[0] != robot_id:
            return "FAIL"

        # Calculate total distance
        tour_cost = 0
        for i in range(len(tour) - 1):
            city_a, city_b = tour[i], tour[i + 1]
            tour_cost += calculate_distance(cities[city_a], cities[city_b])
            
        # Adding to set for city visitation check
        all_visited_cities.update(tour[:-1])

        # Compare calculated cost with reported cost
        if not math.isclose(tour_cost, reported_cost, rel_tol=1e-5):
            return "FAIL"

        total_calculated_cost += reported_cost

    # Check if all cities are visited exactly once
    if all_visited_cities != set(cities.keys()):
        return "FAIL"

    # Verify combined total travel cost
    if not math.isclose(total_calculated_cost, 523.1578917272582, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Checking the correctness of the solution
print(validate_tours_and_costs(tours))