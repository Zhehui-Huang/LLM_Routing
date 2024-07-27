import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, cities):
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Each city visited once
    if len(set(tour)) != len(cities) or set(tour) != set(range(len(cities))):
        return "FAIL"

    # [Requirement 3] & [Requirement 6] Calculate total travel cost using Euclidean distance
    calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_travel _cost, rel_tol=1e-9):
        return "FAIL"

    # [Requirement 5] Check the format of the output tour
    if not isinstance(tour, list) or not all(isinstance(i, int) for i in tour):
        return "FAIL"

    return "CORRECT"

# Cities coordinates
cities = [
    (8, 11),
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Provided solution
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.1974047195548

# Validation
result = verify_solution(tour, total_travel_cost, cities)
print(result)