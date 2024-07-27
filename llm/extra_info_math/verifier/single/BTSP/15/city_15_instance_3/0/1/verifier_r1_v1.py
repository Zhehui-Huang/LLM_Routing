import math

# City coordinates
cities = [
    (16, 90),  # City 0 - Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Provided solution details
tour = [0, 8, 6, 14, 5, 9, 13, 10, 11, 2, 7, 12, 3, 4, 1, 0]
reported_travel_cost = 358.5855830731137
reported_max_distance = 48.373546489791295

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

def check_all_cities_once(tour):
    return len(set(tour)) == len(cities) and len(tour) == len(cities) + 1

def total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def max_distance_between_consecutive_cities(tour):
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        if dist > max_dist:
            max_dist = dist
    return max_dist

def verify_solution(tour, reported_cost, reported_max_distance):
    if not check_depot(tour):
        return "FAIL: Tour does not start and end at depot."
    if not check_all_cities_once(tour):
        return "FAIL: Each city is not visited exactly once."
    calculated_cost = total_travel_cost(tour)
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-4):
        return f"FAIL: Total travel cost incorrect. Calculated: {calculated_cost}, Reported: {reported_cost}"
    calculated_max_dist = max_distance_between_consecutive_cities(tour)
    if not math.isclose(calculated_max_dist, reported_max_distance, rel_tol=1e-4):
        return f"FAIL: Max distance between consecutive cities incorrect. Calculated: {calculated_max_dist}, Reported: {reported_max_distance}"
    return "CORRECT"

# Run unit tests
result = verify_solution(tour, reported_travel_cost, reported_max_distance)
print(result)