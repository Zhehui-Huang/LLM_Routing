import math

# Test data
tour = [0, 19, 5, 9, 10, 15, 4, 3, 13, 11, 14, 2, 16, 7, 12, 8, 6, 1, 18, 17, 0]
reported_cost = 631.6378266184994

# City coordinates in form of (x, y) tuples
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def evaluate_tsp_solution(tour, cities, reported_cost):
    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2
    unique_cities_visited = set(tour) - {0}
    if len(unique_cities_visited) != 19:
        return "FAIL"

    # Requirement 3
    computed_cost = sum(calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(computed_cost, reported_cost, rel_tol=1e-5, abs_tol=1e-5):
        return "FAIL"

    # Requirement 4 (impossibility to validate algorithm compliance through testing a single solution output alone)

    return "CORRECT"

# Running unit test
test_result = evaluate_tsp_solution(tour, cities, reported_cost)
print(test_result)