import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, cities, expected_cost):
    # Requirement 2 & 3: Check if the robot starts and ends at the depot city.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 1: Check if all cities are visited exactly once (except for the start/depot city).
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"

    # Requirement 5: Calculate the total travel cost of the tour
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Requirement 4: Check if the calculated cost is close to the expected cost
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Cities dictionary from the problem statement
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Tour and total travel cost from the solution
solution_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
solution_cost = 349.1974047195548

# Run the verification
print(verify_tour(solution_taur(), [cities[i] for i in range(len(cities))], solution_cost))