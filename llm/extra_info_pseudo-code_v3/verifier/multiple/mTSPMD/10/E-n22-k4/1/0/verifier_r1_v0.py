import math
from collections import Counter

# Define the cities and their coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Define the tours provided
tours = [
    [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 11, 13, 19, 21, 4, 0],
    [1, 6, 8, 10, 9, 7, 5, 12, 15, 18, 20, 17, 21, 19, 16, 14, 13, 11, 4, 1],
    [2, 5, 7, 9, 10, 8, 6, 4, 11, 13, 16, 14, 12, 15, 18, 20, 17, 21, 19, 2],
    [3, 4, 6, 8, 10, 9, 7, 5, 12, 15, 18, 20, 17, 21, 19, 16, 14, 13, 11, 3]
]

# Define the expected travel costs
expected_costs = [344.53, 278.40, 303.54, 257.67]
overall_expected_cost = 1184.14

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_tours():
    city_counter = Counter()
    computed_costs = []
    total_computed_cost = 0

    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i + 1]
            city_counter[city1] += 1
            if i > 0:  # Avoid adding the depot twice
                city_counter[city2] += 1
            cost += calculate_distance(cities[city1], cities[city2])
        computed_costs.append(cost)
        total_computed_cost += cost

        # Check if each tour starts and ends at the same depot
        if tour[0] != tour[-1]:
            return "FAIL"

    # Check if each city is visited exactly once
    if any(count != 2 for city, count in city_counter.items() if city > 3):
        return "FAIL"

    # Check if computed costs are close to expected within a small tolerance
    if not all(math.isclose(computed, expected, rel_tol=0.05) for computed, expected in zip(computed_least_cost, expected_least_cost)):
        return "FAIL"

    # Check the summed cost
    if not math.isclose(total_computed_cost, expected_total_cost, rel_tol=0.05):
        return "FAIL"

    return "CORRECT"

# Validate the solution
print(check_tours())