import math
import unittest

# Define city coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32),
    7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25),
    14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# City groups
city_groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Provided solution
provided_tour = [0, 1, 8, 4, 0]
provided_cost = 110.08796524611944

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def test_tour_requirements(tour, expected_cost):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # skip the depot city at the start and end
        for group, cities in city_groups.items():
            if city in cities:
                if group in visited_groups:
                    return "FAIL"
                visited_groups.add(group)
    if len(visited_groups) != 3:
        return "FAIL"

    # Calculate the total cost and compare with expected cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    if not math.isclose(total_cost, expected_cost, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Execute test
result = test_tour_requirements(provided_tour, provided_cost)
print(result)