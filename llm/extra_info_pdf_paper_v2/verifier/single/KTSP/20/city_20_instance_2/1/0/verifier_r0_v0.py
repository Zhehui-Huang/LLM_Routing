import math

# Coordinates of the cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48),
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Provided tour and total cost
provided_tour = [0, 14, 6, 10, 11, 18, 15, 9, 5, 17, 0]
provided_total_cost = 404.59

def test_tour_start_end_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

def test_tour_length_and_uniqueness(tour):
    return len(set(tour)) == 10 and len(tour) == len(set(tour))

def test_tour_cost(tour, expected_cost):
    total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return math.isclose(total_cost, expected_cost, abs_tol=0.01)

def test_solution():
    if not test_tour_start_end_at_depot(provided_tour):
        return "FAIL"
    if not test_tour_length_and_uniqueness(provided_tour):
        return "FAIL"
    if not test_tour_cost(provided_tour, provided_total_cost):
        return "FAIL"
    return "CORRECT"

# Output the result of all tests
print(test_solution())