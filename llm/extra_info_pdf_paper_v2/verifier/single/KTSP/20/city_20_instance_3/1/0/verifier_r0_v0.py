import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_delta(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def test_solution():
    cities = {
        0: (30, 56),
        1: (53, 42),
        2: (1, 95),
        3: (25, 61),
        4: (69, 57),
        5: (6, 58),
        6: (12, 84),
        7: (72, 77),
        8: (98, 95),
        9: (11, 0),
        10: (61, 25),
        11: (52, 0),
        12: (60, 95),
        13: (10, 94),
        14: (96, 73),
        15: (14, 47),
        16: (18, 16),
        17: (4, 43),
        18: (53, 76),
        19: (19, 72)
    }

    best_tour = [0, 15, 1, 10, 14, 8, 7, 12, 13, 2, 6, 19, 3, 0]
    reported_cost = 319.332462943274

    # [Requirement 1] Start and end at depot city 0
    if best_tour[0] != 0 or best_tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Tour includes exactly 13 cities
    if len(set(best_tour)) - 1 != 13:  # Subtracting 1 as we visit city 0 twice
        return "FAIL"

    # [Requirement 5] Starting and ending at city 0 is checked by Requirement 1 already

    # [Requirement 6] The output must include the cost of the tour
    calculated_cost = calculate_total_cost(best_tour, cities)
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the test
print(test_solution())