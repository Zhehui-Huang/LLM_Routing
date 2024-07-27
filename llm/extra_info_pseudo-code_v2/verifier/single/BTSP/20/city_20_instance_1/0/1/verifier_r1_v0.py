import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_tour(tour, cities):
    # Check if the tour contains all cities exactly once and starts/ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    return "CORRECT"

def check_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_cost += compute_euclidean_distance(x1, y1, x2, y2)
    return total_cost

def check_max_distance(tour, cities):
    max_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        distance = compute_euclidean_distance(x1, y1, x2, y2)
        max_distance = max(max_distance, distance)
    return max_distance

def unit_test(tour, cities, expected_total_cost, max_dist):
    # Check all requirements
    if check_tour(tour, cities) == "FAIL":
        return "FAIL"
    calculated_cost = check_total_travel_cost(tour, cities)
    if abs(calculated_cost - expected_total_cost) > 1e-6:
        return "FAIL"
    calculated_max_distance = check_max_distance(tour, cities)
    if abs(calculated_max_distance - max_dist) > 1e-6:
        return "FAIL"
    return "CORRECT"

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Hypothetical optimal tour (placeholder)
tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]

# Hypothetical total cost and maximum distance (placeholders)
total_cost = 250  # Placeholder
max_distance = 60.41  # The given value

# Run unit test
result = unit_test(tour, cities, total_cost, max_distance)
print(result)