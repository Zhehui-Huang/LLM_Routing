import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_and_cost():
    cities = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
        5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
        10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
        15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
    }
    
    city_groups = [
        [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
    ]
    
    proposed_tour = [0, 4, 7, 12, 15, 3, 18, 0]
    reported_cost = 227.40171050114

    # Requirement 1: Start and end at depot city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Include exactly one city from each group
    included_groups = [0 for _ in range(len(city_groups))]
    for city in proposed_tour[1:-1]:
        found_group = False
        for i, group in enumerate(city_groups):
            if city in group:
                if included_groups[i] == 0:
                    included_groups[i] = 1
                    found_group = True
                    break
        if not found_group:
            return "FAIL"
    if sum(included_groups) != len(city_groups):
        return "FAIL"

    # Requirement 3: Correct total travel cost calculation
    calculated_cost = 0
    for i in range(len(proposed_tour) - 1):
        calculated_cost += euclidean_distance(cities[proposed_tour[i]], cities[proposed_tour[i+1]])

    if not math.isclose(calculated_cost, reported_cost, rel_tol=0.001):
        return "FAIL"

    return "CORRECT"

# Running the test
print(test_tour_and_cost())