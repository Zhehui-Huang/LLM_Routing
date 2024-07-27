import math

# Given cities and their coordinates, including depot
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Compute Euclidean distance
def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Solution output
tour = [0, 14, 16, 19, 11, 7, 10, 3, 4, 1, 17, 5, 2, 9, 15, 13, 18, 8, 6, 12, 0]
total_cost_reported = 492.2863052323856

# Unit tests
def test_solution():
    assert tour[0] == 0 and tour[-1] == 0, "Tour must start and end at the depot city 0."
    assert len(set(tour[1:-1])) == 19 and len(tour[1:-1]) == 19, "All cities except depot must be visited exactly once."
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += compute_distance(cities[tour[i]], cities[tour[i+1]])
    assert abs(computed_cost - total_cost_reported) < 1e-3, "Reported total travel cost must match the computed cost."
    print("CORRECT" if all([tour[0] == 0, tour[-1] == 0, len(set(tour[1:-1])) == 19, len(tour[1:-1]) == 19, abs(computed_cost - total_cost_reported) < 1e-3]) else "FAIL")

# Run test
test_solution()