import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_tour(tour, cost):
    # City coordinates
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
        11: (52, 0),  # Added missing cities 11, 18, and 19
        13: (10, 94),
        14: (96, 73),
        15: (14, 47),
        16: (18, 16),
        17: (4, 43),
        18: (53, 76),
        19: (19, 72)
    }
    groups = [
        [4, 10, 13, 17],
        [6, 7, 14],
        [9, 12, 16],
        [2, 5, 15],
        [1, 3, 19],
        [8, 11, 18]
    ]

    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Start or end at depot check
    
    visited_groups = set()
    for city in tour[1:-1]:  # Excluding the depot city
        found_group = False
        for i, group in enumerate(groups):
            if city in group:
                visited_groups.add(i)
                found_group = True
                break
        if not found_group:
            return "FAIL"  # City not found in any group

    if len(visited_groups) != 6:
        return "FAIL"  # Ensure one city per group check

    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(calculated_cost, cost, rel_tol=1e-3):
        return "FAIL"  # Cost calculation check

    return "CORRECT"

# Provided solution details
provided_tour = [0, 13, 6, 15, 3, 18, 0]  # Corrected tour without duplicate city
provided_cost = 170.24

# Run the test
result = test_tour(provided_tour, provided_cost)
print(result)