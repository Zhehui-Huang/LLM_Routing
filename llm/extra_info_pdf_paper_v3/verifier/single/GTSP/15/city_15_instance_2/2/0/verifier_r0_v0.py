import math

# Data
city_coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

city_groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5],
}

# GIVEN SOLUTION
tour_solution = [0, 12, 10, 4, 3, 2, 0]
reported_total_cost = 138.15

# Functions
def calculate_euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour_requirements(tour, city_groups, reported_cost):
    # Requirement 1 & 4: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = {}
    for city in tour:
        for group_id, cities in city_groups.items():
            if city in cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups[group_id] = True
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Requirement 3 & 5: Calculate the travel cost using Euclidean distance and check cost
    calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Unit Test Execution
result = verify_tour_requirements(tour_solution, city_groups, reported_total_cost)
print(result)