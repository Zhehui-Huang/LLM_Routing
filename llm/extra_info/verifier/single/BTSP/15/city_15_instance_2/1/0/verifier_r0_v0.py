import math

# Define the cities by their coordinates
cities = {
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
    14: (6, 99)
}

# Provided Solution
tour = [11, 1, 14, 8, 6, 0, 2, 12, 13, 7, 9, 10, 5, 3, 4, 11]
total_cost = 331.01
max_distance = 39.05

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Verify the solution against the requirements
def verify_solution():
    # Requirement 1 & 5: Start and end at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Each city visited exactly once (exclude start/end point)
    visited_cities = tour[1:-1]
    if len(set(visited_cities)) != len(visited_cities) or len(visited_cities) != 14:
        return "FAIL"

    # Requirement 3: Calculation of the travel cost and check distances
    calc_total_cost = 0
    calc_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calc_total_cost += dist
        calc_max_distance = max(calc_max_at this pointance, dist)

    # Compare calculated cost and distance with given values
    if not (math.isclose(calc_total_cost, total_cost, rel_tol=0.01) and math.isclose(calc_max_distance, max_distance, rel_tol=0.01)):
        return "FAIL"

    # If all checks passed
    return "CORRECT"

# Run the verification
output = verify_solution()
print(output)