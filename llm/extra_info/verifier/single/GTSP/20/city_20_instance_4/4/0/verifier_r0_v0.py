import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_travel_cost(tour, cities):
    return sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Coordinates of cities
cities = [
    (26, 60),  # 0
    (73, 84),  # 1
    (89, 36),  # 2
    (15, 0),   # 3
    (11, 10),  # 4
    (69, 22),  # 5
    (28, 11),  # 6
    (70, 2),   # 7
    (47, 50),  # 8
    (60, 29),  # 9
    (29, 26),  # 10
    (85, 68),  # 11
    (60, 1),   # 12
    (71, 73),  # 13
    (82, 47),  # 14
    (19, 25),  # 15
    (75, 9),   # 16
    (52, 54),  # 17
    (64, 72),  # 18
    (14, 89)   # 19
]

# Tour provided
tour = [0, 15, 4, 6, 12, 9, 17, 8, 0]

# Expected groups
groups = [[5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]]

def test_tour_starts_and_ends_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

def test_tour_visits_one_city_from_each_group(tour, groups):
    visited = set(tour[1:-1])  # skip the depot at start and end
    for group in groups:
        if len(visited.intersection(group)) != 1:
            return False
    return True

def test_tour_cost_is_correct(tour, cities, expected_cost):
    calculated_cost = total_travel_cost(tour, cities)
    return math.isclose(calculated_cost, expected_cost, rel_tol=1e-9)

# Expected cost from the solution
expected_cost = 187.15997262302855

# Unit tests
if (test_tour_starts_and_ends_at_depot(tour) and
    test_tour_visits_one_city_from_each_group(tour, groups) and
    test_tour_cost_is_correct(tour, cities, expected_cost)):
    print("CORRECT")
else:
    print("FAIL")