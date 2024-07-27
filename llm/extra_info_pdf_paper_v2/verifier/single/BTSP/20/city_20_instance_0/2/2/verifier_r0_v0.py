import math

# City coordinates
city_coordinates = {
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

# Solution provided
tour = [0, 4, 0]
total_travel_cost = 36.77
max_distance = 18.38

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def test_tour_start_end_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

def test_visit_each_city_once(tour):
    visited = set(tour)
    # Check if contains all cities once except starting point city 0 which is visited twice
    return set(range(20)).issubset(visited) and tour.count(0) == 2

def test_travel_cost(tour, expected_cost):
    actual_cost = sum(calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    return math.isclose(actual_cost, expected_cost, abs_tol=0.01)

def test_max_distance(tour, expected_max_distance):
    actual_max_distance = max(calculate_euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    return math.isclose(actual_max_distance, expected_max_distance, abs_tol=0.01)

# Running tests
if (test_tour_start_end_at_depot(tour) and
    test_visit_each_city_once(tour) and
    test_travel_cost(tour, total_travel_cost) and
    test_max_distance(tour, max_distance)):
    print("CORRECT")
else:
    print("FAIL")