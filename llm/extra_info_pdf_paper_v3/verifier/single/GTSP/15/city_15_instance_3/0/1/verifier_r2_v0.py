import math

# City coordinates and groupings
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Groups of city indices
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Provided solution
tour = [0, 14, 5, 10, 11, 8, 9, 0]
provided_cost = 166.76

def tour_starts_and_ends_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

def each_group_represented_exactly_once(tour, groups):
    found_groups = 0
    for group in groups:
        if any(city in tour for city in group):
            found_groups += 1
    return found_groups == len(groups)

def calculate_euclidean_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def is_cost_correct(tour, cities, provided_cost):
    calculated_cost = calculate_total_distance(tour, cities)
    return math.isclose(calculated_cost, provided_cost, rel_tol=1e-2)

def test_tour():
    if not tour_starts_and_ends_at_depot(tour):
        return "FAIL"
    if not each_group_represented_exactly_once(tour, groups):
        return "FAIL"
    if not is_cost_correct(tour, cities, provided_cost):
        return "FAIL"
    return "CORRECT"

# Run test
result = test_tour()
print(result)