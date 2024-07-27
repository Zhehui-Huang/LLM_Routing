import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, expected_total_cost, city_coordinates, city_groups):
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each city group
    visited = set(tour[1:-1])  # Exclude the depot city at start and end
    counts_per_group = [0] * len(city_groups)
    
    for city in visited:
        for idx, group in enumerate(city_groups):
            if city in group:
                counts_per_group[idx] += 1

    if not all(count == 1 for count in counts_per_group):
        return "FAIL"

    # Requirement 3: Total travel cost matches calculated cost
    calculated_cost = 0.0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    if not math.isclose(calculated_cost, expected_total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Define the city coordinates and groups.
city_coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Tour and cost as claimed in your results
tour = [0, 14, 0]
total_travel_cost = 38.83

# Verify the solution
result = verify_solution(tour, total_travel_cost, city_coordinates, city_groups)
print(result)