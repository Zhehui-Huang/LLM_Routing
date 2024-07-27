import math

# Function to compute Euclidean distance between two cities by their coordinates
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities coordinates indexed by city number
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Proposed robot tours and their reported costs
robot_tours = [
    ([0, 11, 12], 74.16),
    ([0, 9, 10], 77.87),
    ([0, 3, 13], 78.77),
    ([0, 15, 7], 83.62),
    ([0, 8, 2], 65.52),
    ([0, 5, 1], 61.19),
    ([0, 14, 4], 97.10),
    ([0, 6], 24.08)
]

# Verify Requirement 1: Each robot starts at city 0 and ends at any city
def verify_start_end_points():
    return all(tour[0] == 0 for tour, _ in robot_tours)

# Verify Requirement 2: All cities are visited exactly once
def verify_all_cities_visited_once():
    all_visited_cities = [city for tour, _ in robot_tours for city in tour]
    unique_cities = set(all_visited_cities)
    return len(unique_cities) == 16 and len(all_visited_cities) == len(unique_cities)

# Verify Requirement 3 & 4: Total cost calculation and optimization
def verify_costs():
    total_calculated_cost = 0
    for tour, reported_cost in robot_tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_calculated_cost += tour_cost
        if not math.isclose(tour_cost, reported_cost, abs_tol=0.01):
            return False
    overall_reported_cost = sum(cost for _, cost in robot_tours)
    if not math.isclose(total_calculated_cost, overall_reported_cost, abs_tol=0.01):
        return False
    return True

# Main unit test execution
if verify_start_end_points() and verify_all_cities_visited_once() and verify_costs():
    print("CORRECT")
else:
    print("FAIL")