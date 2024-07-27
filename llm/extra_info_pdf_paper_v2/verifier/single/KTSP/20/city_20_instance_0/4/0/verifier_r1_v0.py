import math

# Test input
tour = [0, 1, 8, 4, 0]
total_cost = 110.08796524611944
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

# Helper function to calculate Euclidean distance
def euclidean(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Check Tour Requirements
def test_solution(tour, total_cost):
    # Check the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check the tour includes exactly 4 different cities (including the depot)
    if len(set(tour)) != 4 + 1:  # +1 because the depot appears twice
        return "FAIL"

    # Check the calculation of the total travel cost
    computed_cost = sum(euclidean(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Run the test
result = test_solution(tour, total_cost)
print(result)