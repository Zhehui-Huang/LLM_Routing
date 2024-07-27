import math

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define city coordinates
cities = {
    0: (8, 11),   # Depot
    1: (40, 6),
    3: (80, 60),
    5: (67, 23),
    11: (40, 87),
    13: (61, 25),
    14: (5, 59),
    19: (93, 15),
    2: (95, 33),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    12: (20, 97),
    15: (62, 88),
    4: (25, 18),
    9: (27, 91),
    10: (91, 46),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63)
}

# Groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# The proposed solution
proposed_tour = [0]
proposed_total_cost = 0.0

# Unit checks
def check_requirements(tour, total_cost, cities, groups):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly one city from each group
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:  # Ignore the depot city
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
                break
    if any(count != 1 for count in visited_groups):
        return "FAIL"

    # Requirement 3: Minimize the total travel cost calculated
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Evaluate the proposed tour and total cost
result = check_requirements(proposed_tour, proposed_total_cost, cities, groups)
print(result)