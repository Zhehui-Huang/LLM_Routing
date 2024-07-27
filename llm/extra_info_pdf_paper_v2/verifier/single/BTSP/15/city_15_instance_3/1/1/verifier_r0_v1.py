import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def evaluate_tour():
    cities = [
        (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
        (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
        (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
    ]
    tour = [0, 14, 5, 9, 13, 10, 8, 6, 1, 4, 12, 3, 7, 11, 2, 0]
    expected_total_cost = 373.61
    expected_max_distance = 94.11

    # Test 1: Tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Test 2: Each city must be visited exactly once
    tour_without_depot = tour[1:-1]
    unique_cities = set(tour_without_depot)
    if len(unique_cities) != 14 or any(city not in unique_cities for city in range(1, 15)):
        return "FAIL"

    # Test 3: Check max distance against expected maximum distance
    actual_max_distance = max(
        distance(cities[tour[i]], cities[tour[i + 1]])
        for i in range(len(tour) - 1)
    )
    if abs(actual_max_distance - expected_max_distance) > 0.01:
        return "FAIL"
    
    # Test 4: Check total travel cost against expected total cost
    actual_total_cost = sum(
        distance(cities[tour[i]], cities[tour[i + 1]])
        for i in range(len(tour) - 1)
    )
    if abs(actual_total_cost - expected_total_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

print(evaluate_tour())