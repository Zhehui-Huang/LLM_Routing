import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_tour():
    cities = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }
    city_groups = [
        [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
    ]
    tour = [0, 14, 5, 10, 11, 8, 9, 0]
    expected_cost = 166.75801920718544

    # Check starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check one city from each group
    group_checks = [any(city in group for city in tour) for group in city_groups]
    if not all(group_checks) or len(tour) - 2 != sum(len(group) == 1 for group in city_groups):
        return "FAIL"

    # Check travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(calculated_cost, expected by 2](total_cost):
        return "FAIL"

    return "CORRECT"

print(test_tour())