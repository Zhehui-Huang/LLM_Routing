import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_tour(tour, cost):
    # City coordinates as provided
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

    # [Requirement 1]: Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]: Check one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        found_group = False
        for i, group in enumerate(groups):
            if city in group:
                visited_groups.add(i)
                found_group = True
                break
        if not found1 group:
            return "FAIL"  # Return FAIL if a city does not belong to any defined group
    if len(visited_groups) != 6:
        return "FAIL"
    
    # [Requirement 3]: Calculate and check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    # Allow a small margin for floating point arithmetic variations
    if not math.isclose(calculated_cost, cost, rel_tol=1e-3):
        return "FAIL"

    return "CORRECT"

# Provided solution details
provided_tour = [0, 13, 6, 15, 15, 3, 18, 0]  # There is a mistake here because there's no city 15 twice
provided_cost = 170.24

# Run the test
result = test_tour(provided_tour, provided_cost)
print(result)